#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""A class that represents a Dataset in SampleDB."""
from typing import Union

import geopandas as gpd
from lccs import LCCS

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

    def __init__(self, dataset, url, data, lccs):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(Dataset, self).__init__(data or {})
        #: Dataset: The associated Dataset.
        self._dataset = dataset
        self.metadata_json = self.prepare_metadata()
        self.__url = url
        self.__lccs_server = LCCS(lccs)

    def prepare_metadata(self) -> Union[None, DSMetada]:
        """Prepare dataset metadata."""
        if isinstance(self['metadata_json'], dict):
            metadata_json = DSMetada(self['metadata_json'])
            return metadata_json
        else:
            return None

    @property
    def id(self):
        """Return the dataset id."""
        return self['id']

    @property
    def classification_system_name(self):
        """Return the dataset classification system id."""
        return self['classification_system_name']

    @property
    def classification_system_id(self):
        """Return the dataset classification system name."""
        return self['classification_system_id']

    @property
    def classification_system_version(self):
        """Return the dataset classification system version."""
        return self['classification_system_version']

    def _get_classification_system(self):
        """Return the classification system object."""
        system_id = f"{self['classification_system_name']}-{self['classification_system_version']}"
        return self.__lccs_server.classification_system(system_id)

    @property
    def classification_system(self):
        """Return the classification system object."""
        return self._get_classification_system()

    @property
    def collect_method(self):
        """Return the dataset collect method name."""
        return self['collect_method_name']

    @property
    def collect_method_id(self):
        """Return the dataset collect method id."""
        return self['collect_method_id']

    @property
    def description(self):
        """Return the dataset description."""
        return self['description']

    @property
    def end_date(self):
        """Return the dataset end date."""
        return self['end_date']

    @property
    def start_date(self):
        """Return the dataset start date."""
        return self['start_date']

    @property
    def name(self):
        """Return the dataset name."""
        return self['name']

    @property
    def title(self):
        """Return the dataset identifier."""
        return self['title']

    @property
    def is_public(self):
        """Return the dataset is_public."""
        return self['is_public']

    @property
    def version(self):
        """Return the dataset version."""
        return self['version']

    @property
    def version_successor(self):
        """Return the dataset version_successor."""
        return self['version_successor']

    @property
    def version_predecessor(self):
        """Return the dataset version_predecessor."""
        return self['version_predecessor']

    @property
    def metadata(self):
        """Return the dataset metadata."""
        return self.metadata_json

    @property
    def dataset_table_id(self):
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

    @property
    def data(self):
        """Return the dataset observation dataframe."""
        features = Utils._get(url=f'{self._dataset._url}/datasets/data',
                              **dict(access_token=self._dataset._access_token, dataset_id=self.id, limit=self.number_of_features))

        return gpd.GeoDataFrame.from_features(features["features"])

    def _repr_html_(self):
        """HTML repr."""
        return Utils.render_html('dataset.html', dataset=self)
