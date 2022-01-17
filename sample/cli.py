#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-20201 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Command line interface for the SampleDB client."""

import click

from .sample import SAMPLE


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialize of Config decorator."""
        self.url = None
        self.service = None
        self.lccs_url = None
        self.access_token = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', default='http://127.0.0.1:5000/',
              help='The Sample-WS address (an URL).')
@click.option('--access-token', default=None, help='Personal Access Token of the BDC Auth')
@click.option('--lccs_url', type=click.STRING, default='https://brazildatacube.dpi.inpe.br/lccs',
              help='The LCCS-WS address (an URL).')
@click.version_option()
@pass_config
def cli(config, url, lccs_url, access_token=None):
    """Sample on command line."""
    config.url = url
    config.service = SAMPLE(url=url, access_token=access_token, lccs_url=lccs_url)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def datasets(config: Config, verbose):
    """List available datasets."""
    if verbose:
        click.secho(f'WFS: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the list of available datasets... ',
                    bold=False, fg='black')

        for ds in config.service.datasets:
            click.secho(f'\t\t- {ds}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        for ds in config.service.datasets:
            click.secho(f'{ds}', bold=True, fg='green')


@cli.command()
@click.option('--dataset_id', default=None, type=click.STRING, required=False,
              help='The dataset id to return information.')
@click.option('--dataset_name', default=None, type=click.STRING, required=False,
              help='The dataset name to return information.')
@click.option('--dataset_version', default=None, type=click.STRING, required=False,
              help='The dataset version to return information.')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def describe_dataset(config: Config, dataset_id, dataset_name, dataset_version, verbose):
    """Retrieve information of a specific dataset."""
    if dataset_id:
        retval = config.service.dataset(dataset_id=dataset_id)
    elif dataset_name is not None and dataset_version is not None:
        retval = config.service.dataset(dataset_name=dataset_name, dataset_version=dataset_version)
    else:
        click.secho('You must enter the dataset identifier or its name and version !',
                    bold=True, fg='red')
        return

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the describe of dataset... ',
                    bold=False, fg='black')

        click.secho(f'\t- {retval}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        click.secho(f'{retval}', fg='green')


@cli.command()
@click.option('--dataset_id', default=None, type=click.STRING, required=False,
              help='The dataset id to return information.')
@click.option('--dataset_name', default=None, type=click.STRING, required=False,
              help='The dataset name to return information.')
@click.option('--dataset_version', default=None, type=click.STRING, required=False,
              help='The dataset version to return information.')
@click.option('--filename', type=click.STRING, required=True, help='File path or file handle to write to')
@click.option('--limit', default=None, type=click.INT,
              help='The maximum number of results to return (page size). Defaults to None')
@click.option('--page', default=None, type=click.INT, help='The page number of results..')
@click.option('--driver', type=click.STRING, required=False, default='ESRI Shapefile',
              help='The OGR format driver used to write the vector file')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def export_data(config: Config, dataset_id, dataset_name, dataset_version, limit, page, filename, driver, verbose):
    """Save dataset data of a specific dataset."""
    if dataset_id:
        retval = config.service.dataset(dataset_id=dataset_id)
    elif dataset_name is not None and dataset_version is not None:
        retval = config.service.dataset(dataset_name=dataset_name, dataset_version=dataset_version)
    else:
        click.secho('You must enter the dataset identifier or its name and version !',
                    bold=True, fg='red')
        return

    filter = {
        'limit': limit,
        'page': page
    }

    gdf = retval.data(filter=filter)

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tSave dataset data..',
                    bold=False, fg='black')

        config.service.save_feature(filename, gdf, driver)

        click.secho(f'\t- Saved dataset in {filename}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        config.service.save_feature(filename, gdf, driver)

        click.secho(f'Saved dataset in {filename}', fg='green')


@cli.command()
@click.option('--name', type=click.STRING, required=True, help='The dataset name.')
@click.option('--title', type=click.STRING, required=True, help='The dataset title')
@click.option('--version', type=click.STRING, required=True, help='The dataset version.')
@click.option('--description', type=click.STRING, required=True, help='The dataset description.')
@click.option('--start_date', type=click.STRING, required=True, help='The dataset start date.')
@click.option('--version_predecessor', type=click.STRING, required=False, help='The dataset version predecessor.', default=None)
@click.option('--version_successor', type=click.STRING, required=False, help='The dataset version successor.', default=None)
@click.option('--end_date', type=click.STRING, required=True, help='The dataset end date.')
@click.option('--classification_system_id', type=click.STRING, required=True,
              help='The dataset classification system id.')
@click.option('--collect_method_id', type=click.STRING, required=True, help='The dataset collect method id.')
@click.option('--public/--no-public', required=True, default=False, help='Is this dataset public?.')
@click.option('--metadata', type=click.Path(exists=True, readable=True), help='A JSON metadata file.',
              required=False)
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def add_dataset(config: Config, name, metadata, start_date, end_date, classification_system_id, collect_method_id,
                public, version, title, description, version_predecessor, version_successor, verbose):
    """Add a new dataset."""
    import json

    metadata_file = None

    if metadata:
        with open(metadata, "r") as f:
            metadata_file = json.load(f)

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tAdding new classification system ... ', bold=False, fg='black')

    config.service.add_dataset(name=name, metadata=metadata_file, start_date=start_date, end_date=end_date,
                               classification_system_id=classification_system_id,
                               collect_method_id=collect_method_id, is_public=public, version=version, title=title,
                               description=description, version_predecessor=version_predecessor,
                               version_successor=version_successor, )

    click.secho('\tFinished!', bold=False, fg='black')


@cli.command()
@click.option('--dataset_id', type=click.INT, required=False, help='The dataset id.')
@click.option('--dataset_name', type=click.STRING, required=False, help='The dataset name.')
@click.option('--dataset_version', type=click.STRING, required=False, help='The dataset version.')
@click.option('--samples', type=click.Path(exists=True, readable=True), required=False,
              default=None,help='Mappings used for location columns in file.')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def insert_dataset_data(config: Config, dataset_id, dataset_name, dataset_version, samples, verbose):
    """Insert data into dataset."""
    import json

    with open(samples, "r") as f:
        sample_file = json.load(f)

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tAdding new classification system ... ', bold=False, fg='black')

    config.service.add_dataset_data(dataset_id=dataset_id, dataset_name=dataset_name, dataset_version=dataset_version,
                                    samples=sample_file)
