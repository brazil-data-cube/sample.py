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
"""A class that represents a Dataset in SampleDB."""
from typing import Union

import geopandas as gpd
from lccs import LCCS, ClassificationSystem

from .utils import Utils


class DSMetada(dict):
    """DSMetada Class."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(DSMetada, self).__init__(data or {})

    def _repr_html_(self):
        """HTML repr."""
        return Utils.render_html('metadata.html', metadata=self)


class Dataset(dict):
    """DataSet Class."""

    def __init__(self, dataset, url, data, lccs, token, language=None):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(Dataset, self).__init__(data or {})
        #: Dataset: The associated Dataset.
        self._dataset = dataset
        self.metadata_json = self.prepare_metadata()
        self.__url = url
        self.__lccs_server = LCCS(lccs, access_token=token, language=language)
        self.__language = language

    def prepare_metadata(self) -> Union[None, DSMetada]:
        """Prepare dataset metadata."""
        if isinstance(self['metadata_json'], dict):
            metadata_json = DSMetada(self['metadata_json'])
            return metadata_json
        else:
            return None

    @property
    def id(self) -> str:
        """Return the dataset id."""
        return self['id']
    @property
    def classification_system_identifier(self) -> str:
        """Return the dataset classification system id."""
        return self['classification_system_identifier']

    @property
    def classification_system_title(self) -> str:
        """Return the dataset classification system id."""
        return self['classification_system_title']

    @property
    def classification_system_name(self) -> str:
        """Return the dataset classification system id."""
        return self['classification_system_name']

    @property
    def classification_system_id(self) -> str:
        """Return the dataset classification system name."""
        return self['classification_system_id']

    @property
    def classification_system_version(self) -> str:
        """Return the dataset classification system version."""
        return self['classification_system_version']

    def _get_classification_system(self) -> ClassificationSystem:
        """Return the classification system object."""
        return self.__lccs_server.classification_system(self.classification_system_identifier)

    @property
    def classification_system(self) -> ClassificationSystem:
        """Return the classification system object."""
        return self._get_classification_system()

    @property
    def collect_method(self) -> str:
        """Return the dataset collect method name."""
        return self['collect_method_name']

    @property
    def collect_method_id(self) -> str:
        """Return the dataset collect method id."""
        return self['collect_method_id']

    @property
    def description(self) -> str:
        """Return the dataset description."""
        return self['description']

    @property
    def end_date(self) -> str:
        """Return the dataset end date."""
        return self['end_date']

    @property
    def start_date(self) -> str:
        """Return the dataset start date."""
        return self['start_date']

    @property
    def name(self) -> str:
        """Return the dataset name."""
        return self['name']

    @property
    def title(self) -> str:
        """Return the dataset identifier."""
        return self['title']

    @property
    def is_public(self) -> str:
        """Return the dataset is_public."""
        return self['is_public']

    @property
    def version(self) -> str:
        """Return the dataset version."""
        return self['version']

    @property
    def version_successor(self) -> Union[int, None]:
        """Return the dataset version_successor."""
        return self['version_successor']

    @property
    def version_predecessor(self) -> Union[int, None]:
        """Return the dataset version_predecessor."""
        return self['version_predecessor']

    @property
    def metadata(self) -> Union[DSMetada, None]:
        """Return the dataset metadata."""
        return self.metadata_json

    @property
    def dataset_table_id(self) -> int:
        """Return the dataset table name."""
        return self['dataset_table_id']

    @property
    def user_id(self):
        """Return the dataset user id (user id who performed the insertion of the dataset)."""
        return self['user_id']

    @property
    def created_at(self):
        """Return the dataset created_at date."""
        return self['created_at']

    @property
    def updated_at(self):
        """Return the dataset updated_at date."""
        return self['updated_at']

    @property
    def number_of_features(self):
        """Return the dataset updated_at date."""
        return self['number_of_features']

    def data(self, data_id: int = None, filter: dict = dict()) -> gpd.GeoDataFrame:
        """Return the dataset observation dataframe."""
        url = f'{self._dataset._url}/datasets/data'

        filter["access_token"] = self._dataset._access_token
        filter["language"] =  self.__language
        filter["dataset_id"] = self.id

        if data_id:
            filter["data_id"] = data_id
        else:
            if 'limit' not in filter or filter["limit"] is None:
                filter["limit"] = self.number_of_features

        features = Utils._get(url=url,
                              **filter)
        return gpd.GeoDataFrame.from_features(features["features"])

    def _repr_html_(self):
        """HTML repr."""
        return Utils.render_html('dataset.html', dataset=self)
