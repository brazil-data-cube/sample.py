#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for SampleDB."""
import geopandas as gpd
from shapely.geometry import MultiPolygon, Point, Polygon

from .dataset import DataSet
from .wfs import WFS


class sample:
    """Create wfs clients attached to given host addresses.

    See https://github.com/brazil-data-cube/sample.py for more
    information on SampleDB.

    :param wfs:  WFS server URL.
    :type wfs: str
    """

    def __init__(self, **kwargs):
        """Create a WFS client attached to the given host address (an URL)."""
        invalid_parameters = set(kwargs) - {"wfs", "auth"}

        if invalid_parameters:
            raise AttributeError('invalid parameter(s): {}'.format(invalid_parameters))

        self.__auth = None
        if 'auth' in kwargs:
            if kwargs['auth'] is not None:
                if not type(kwargs['auth']) is tuple:
                    raise AttributeError('auth must be a tuple ("user", "pass")')
                if len(kwargs['auth']) != 2:
                    raise AttributeError('auth must be a tuple with 2 values ("user", "pass")')
                self.__auth = kwargs['auth']

        self.__wfs = None
        if 'wfs' in kwargs:
            if type(kwargs['wfs'] is str):
                self.__wfs_server = kwargs['wfs']
                self.__wfs = WFS(kwargs['wfs'], auth=self.__auth)
            else:
                raise AttributeError('wfs must be a string')

    def list_feature(self):
        """List WFS feature."""
        return self.__wfs.list_features()

    def describe_feature(self, ft_name):
        """Describe Feature."""
        return self.__wfs.describe_feature(ft_name)

    def dataset(self, name):
        """Describe dataset."""
        if not name:
            raise AttributeError('Invalid Dataset Name')

        cql_filter = 'name=\'{}\''.format(name)

        features = self.__wfs.get_feature("sampledb:dataset", max_features=1, filter=cql_filter)

        feature = features['features'][0]

        ds = DataSet(self.__wfs, feature['properties'])

        return ds

    @property
    def datasets(self):
        """Return all dataset name in sampledb."""
        features = self.__wfs.get_feature("sampledb:dataset")

        result = list()

        for ft in features['features']:
            result.append(ft['properties']['name'])

        return result

    def save_feature(self, filename: str, gdf: gpd.geodataframe.GeoDataFrame, driver: str = "ESRI Shapefile"):
        """Save GeoDataframe."""
        gdf.to_file(filename, encoding="utf-8", driver=driver)
