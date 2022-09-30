#
# This file is part of Python Client Library for SAMPLE-WS.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#
"""Unit-test for Sample Client."""
import json
import os
import re
from pathlib import Path

import pytest
from click.testing import CliRunner
from pkg_resources import resource_filename, resource_string

import sample
from sample.cli import Config

url = os.environ.get('SAMPLE_SERVER_URL', 'http://localhost:5000')
match_url = re.compile(url)


@pytest.fixture
def requests_mock(requests_mock):
    requests_mock.get(re.compile('https://geojson.org/'), real_http=True)
    yield requests_mock


@pytest.fixture(scope='session')
def sample_objects():
    directory = resource_filename(__name__, 'jsons/')
    files = dict()
    for path in Path(directory).rglob('*.json'):
        path = str(path)
        s = path.split('/')

        file_path = '/'.join(s[-2:])

        print(file_path)

        file = json.loads(resource_string(__name__, file_path).decode('utf-8'))
        if s[-2] in files:
            files[s[-2]][s[-1]] = file
        else:
            files[s[-2]] = {s[-1]: file}

    return files


@pytest.fixture(scope='module')
def runner():
    return CliRunner()


@pytest.fixture
def config_obj():
    config = Config()
    config.url = url
    config.service = sample.SAMPLE(url)

    return config


class TestSample:
    def test_sample(self):
        service = sample.SAMPLE(url)
        assert service.url == url
        assert str(service) == f'SAMPLE:\n\tURL: {url}'
        assert repr(service) == f'sample(url="{url}")'

    def test_list_datasets(self, sample_objects, requests_mock):
        for k in sample_objects:
            s = sample.SAMPLE(url)
            requests_mock.get(match_url, json=sample_objects[k]['list_datasets.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            response = s.datasets

            assert type(response) == list
            assert response == [{'id': 4, 'name': 'bdc-go-test-area', 'version': '1'},
                                {'id': 6, 'name': 'bdc-all-test-area', 'version': '1'},
                                {'id': 3, 'name': 'bdc-ba-test-area', 'version': '1'}]

    def test_describe_dataset(self, sample_objects, requests_mock):
        for k in sample_objects:
            s = sample.SAMPLE(url)

            requests_mock.get(match_url, json=sample_objects[k]['describe_dataset.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            requests_mock.get(re.compile('https://brazildatacube.dpi.inpe.br/lccs/classification_systems'), real_http=True)

            ds = s.dataset(dataset_id=4)

            assert ds == sample_objects[k]['describe_dataset.json']
            assert ds['classification_system_id'] == 1
            assert ds['classification_system_name'] == 'BDC'
            assert ds['classification_system_version'] == '1.0'
            assert ds['collect_method_id'] == 2
            assert ds['collect_method_name'] == 'VISUAL'
            assert ds['dataset_table_id'] == 648621
            assert ds['id'] == 4
            assert ds['version'] == '1'
            assert ds['name'] == 'bdc-go-test-area'

    def test_dataset_data(self, sample_objects, requests_mock):
        for k in sample_objects:
            import geopandas as gpd
            s = sample.SAMPLE(url)

            requests_mock.get(re.compile('https://brazildatacube.dpi.inpe.br/lccs/classification_systems'),
                              real_http=True)
            requests_mock.get(match_url, json=sample_objects[k]['describe_dataset.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            ds = s.dataset(dataset_id=4)

            requests_mock.get(match_url, json=sample_objects[k]['dataset_data.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            observations = ds.data(data_id=1)

            assert type(observations) == gpd.GeoDataFrame


class TestCli:
    def test_datasets(self, sample_objects, requests_mock, runner, config_obj):
        for k in sample_objects:
            requests_mock.get(match_url, json=sample_objects[k]['list_datasets.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            result = runner.invoke(sample.cli.datasets, obj=config_obj)

            assert result.exit_code == 0
            assert 'id' in result.output
            assert 'name' in result.output

    def test_describe(self, sample_objects, requests_mock, runner, config_obj):
        for k in sample_objects:
            requests_mock.get(re.compile('https://brazildatacube.dpi.inpe.br/lccs/classification_systems'),
                              real_http=True)
            requests_mock.get(match_url, json=sample_objects[k]['describe_dataset.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            result = runner.invoke(sample.cli.describe_dataset, ['--dataset_id', '4'], obj=config_obj)

            assert result.exit_code == 0
            assert 'classification_system_id' in result.output
            assert 'classification_system_name' in result.output
            assert 'classification_system_version' in result.output
            assert 'collect_method_id' in result.output
            assert 'collect_method_name' in result.output
            assert 'end_date' in result.output
            assert 'start_date' in result.output
            assert 'id' in result.output
            assert 'is_public' in result.output
            assert 'version' in result.output


if __name__ == '__main__':
    import pytest

    pytest.main(['--color=auto', '--no-cov'])