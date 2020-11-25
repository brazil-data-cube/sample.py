#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for SampleDB."""
import json

import geopandas as gpd
import pyproj

from .utils import Utils


class DataSet(dict):
    """DataSet Class."""

    def __init__(self, wfs, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(DataSet, self).__init__(data or {})
        self.metadata_json = self.prepare_metadata()
        self.__wfs = wfs

    def prepare_metadata(self):
        """Refactory metadata."""
        if self['metadata_json'] is not None:
            m = json.loads(self['metadata_json'])
            metadata_json = DSMetada(m)

            del self['metadata_json']

            return metadata_json
        else:
            return None

    @property
    def id(self):
        """:return: id of dataset."""
        return self['id']

    @property
    def classification_system_name(self):
        """:return: classification_system_name of dataset."""
        return self['classification_system_name']

    @property
    def collect_method(self):
        """:return: collect_method of dataset."""
        return self['collect_method']

    @property
    def description(self):
        """:return: description of dataset."""
        return self['description']

    @property
    def end_date(self):
        """:return: end_date of dataset."""
        return self['end_date']

    @property
    def start_date(self):
        """:return: start_date of dataset."""
        return self['start_date']

    @property
    def midias_table_name(self):
        """:return: midias_table_name of dataset."""
        return self['midias_table_name']

    @property
    def name(self):
        """:return: name of dataset."""
        return self['name']

    @property
    def metadata(self):
        """:return: a metada_json."""
        return self.metadata_json

    @property
    def observation_table_name(self):
        """:return: observation_table_name of dataset."""
        return self['observation_table_name']

    @property
    def user_name(self):
        """:return: user_name of dataset."""
        return self['user_name']

    @property
    def created_at(self):
        """:return: created_at of dataset."""
        return self['created_at']

    @property
    def updated_at(self):
        """:return: created_at of dataset."""
        return self['updated_at']

    @property
    def observation(self):
        """Return observation dataframe."""
        observation_name = 'sampledb:{}'.format(self['observation_table_name'])

        geometry_name = 'location'

        feature = Utils._get_feature(self.__wfs, name=observation_name, geometry_name=geometry_name)

        df_obs = gpd.GeoDataFrame.from_dict(feature['features'])

        crs = feature['crs']['properties']
        crs = pyproj.crs.CRS(crs['name']).to_epsg()

        df_obs = df_obs.set_geometry(col=geometry_name, crs=f'EPSG:{crs}')

        return df_obs


class DSMetada(dict):
    """DSMetada Class."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(DSMetada, self).__init__(data or {})

    @property
    def id(self):
        """:return: id of ds metadata."""
        return self['id']

    @property
    def version(self):
        """:return: version of ds metadata."""
        return self['id']

    @property
    def titles(self):
        """:return: titles of ds metadata."""
        return self['titles']

    @property
    def relatedIdentifiers(self):
        """:return: relatedIdentifiers of ds metadata."""
        return self['relatedIdentifiers']

    @property
    def contributors(self):
        """:return: contributors of ds metadata."""
        return self['contributors']

    @property
    def creators(self):
        """:return: creators of ds metadata."""
        return self['creators']
