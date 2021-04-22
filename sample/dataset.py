#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""A class that represents a Dataset in SampleDB."""

import json

import geopandas as gpd
import pyproj

from .utils import Utils


class Dataset(dict):
    """DataSet Class."""

    def __init__(self, wfs, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(Dataset, self).__init__(data or {})
        self.metadata_json = self.prepare_metadata()
        self.__wfs = wfs

    def prepare_metadata(self):
        """Prepare dataset metadata."""
        if self['metadata_json'] is not None:
            m = json.loads(self['metadata_json'])
            metadata_json = DSMetada(m)

            del self['metadata_json']

            return metadata_json
        else:
            return None

    @property
    def id(self):
        """Return the dataset id."""
        return self['id']

    @property
    def classification_system_name(self):
        """Return the dataset classification system name."""
        return self['classification_system_name']

    @property
    def collect_method(self):
        """Return the dataset collect method name."""
        return self['collect_method']

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
    def midias_table_name(self):
        """Return the dataset midias table name."""
        return self['midias_table_name']

    @property
    def name(self):
        """Return the dataset name."""
        return self['name']

    @property
    def identifier(self):
        """Return the dataset identifier."""
        return self['identifier']

    @property
    def is_public(self):
        """Return the dataset is_public."""
        return self['is_public']

    @property
    def version(self):
        """Return the dataset is_public."""
        return self['version']

    @property
    def metadata(self):
        """Return the dataset metadata."""
        return self.metadata_json

    @property
    def observation_table_name(self):
        """Return the dataset observation table name."""
        return self['observation_table_name']

    @property
    def user_name(self):
        """Return the dataset user name (user who performed the insertion of the dataset)."""
        return self['user_name']

    @property
    def created_at(self):
        """Return the dataset created_at date."""
        return self['created_at']

    @property
    def updated_at(self):
        """Return the dataset updated_at date."""
        return self['updated_at']

    @property
    def observation(self):
        """Return the dataset observation dataframe."""
        observation_name = 'sampledb:{}'.format(self['observation_table_name'])

        geometry_name = 'location'

        feature = Utils._get_feature(self.__wfs, name=observation_name, geometry_name=geometry_name)

        df_obs = gpd.GeoDataFrame.from_dict(feature['features'])

        crs = feature['crs']['properties']
        crs = pyproj.crs.CRS(crs['name']).to_epsg()

        df_obs = df_obs.set_geometry(col=geometry_name, crs=f'EPSG:{crs}')

        return df_obs

    def _repr_html_(self):
        """HTML repr."""
        return Utils.render_html('dataset.html', dataset=self)


class DSMetada(dict):
    """DSMetada Class."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(DSMetada, self).__init__(data or {})

    @property
    def id(self):
        """Return the metadata id."""
        return self['id']

    @property
    def version(self):
        """Return the metadata version."""
        return self['version']

    @property
    def titles(self):
        """Return the metadata titles."""
        return self['titles']

    @property
    def relatedIdentifiers(self):
        """Return the metadata relatedIdentifiers."""
        return self['relatedIdentifiers']

    @property
    def contributors(self):
        """Return the metadata contributors."""
        return self['contributors']

    @property
    def creators(self):
        """Return the metadata creators."""
        return self['creators']
