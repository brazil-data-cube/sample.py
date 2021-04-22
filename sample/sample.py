#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for SampleDB."""
import geopandas as gpd
from shapely.geometry import MultiPolygon, Point, Polygon

from .dataset import Dataset
from .utils import Utils
from .wfs import WFS


class SAMPLE:
    """Create wfs clients attached to given host addresses.

    .. note::
        For more information about coverage definition, please, refer to
        `Sample-DB <https://github.com/brazil-data-cube/sampledb>`_.
    """

    def __init__(self, **kwargs):
        """Create a WFS client attached to the given host address (an URL).

        Args:
            url (str): URL for the sample WFS.
            auth (dict): user and password.
        """
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
                self.__wfs = WFS(kwargs['wfs'], auth=self.__auth)
            else:
                raise AttributeError('wfs must be a string')

    def list_feature(self):
        """Return a list of WFS feature.

        Returns:
            list: A list with the names of available features.
        """
        return self.__wfs.list_features()

    def describe_feature(self, ft_name):
        """Describe Feature."""
        return self.__wfs.describe_feature(ft_name)

    def _get_dataset(self, identifier_version):
        """Get dataset metadata for the given dataset.

        Args:
            identifier_version (str): The dataset key identifier-version.
        Returns:
           dict: The coverage metadata as a dictionary.
        """
        if not identifier_version:
            raise AttributeError('Invalid Dataset')

        identifier, version = identifier_version.split("-V", 2)

        cql_filter = 'identifier=\'{}\' AND version=\'{}\''.format(identifier, version)

        features = self.__wfs.get_feature("sampledb:dataset", max_features=1, filter=cql_filter)

        feature = features['features'][0]

        return Dataset(self.__wfs, feature['properties'])

    def __getitem__(self, key):
        """Get dataset identified by the key (identifier-version).

        Returns:
            Dataset: A dataset object.

        Raises:
            ConnectionError: If the server is not reachable.
            HTTPError: If the server response indicates an error.
            ValueError: If the response body is not a json document.

        Example:
            Get a dataset object named ``bdc_mato_grosso_2017-2018-V001``:
            .. doctest::
                :skipif: SAMPLE_EXAMPLE_URL is None
                >>> from sample import *
                >>> service = SAMPLE(SAMPLE_EXAMPLE_URL)
                >>> service['bdc_mato_grosso_2017-2018-V001']
                dataset...
        """
        return self._get_dataset(key)

    def _list_datasets(self):
        """Return a list of all dataset available.

        Returns:
          list: A list with the available dataset in service.
        """
        features = self.__wfs.get_feature("sampledb:dataset")

        result = list()

        for ft in features['features']:
            result.append(f"{ft['properties']['identifier']}-V{ft['properties']['version']}")

        return result

    @property
    def datasets(self):
        """Return a list of all dataset available.

        Returns:
          list: A list with the available dataset in service.
        """
        return self._list_datasets()

    def __iter__(self):
        """Iterate over collections available in the service.

        Returns:
            A dataset at each iteration.

        """
        for dataset in self.datasets:
            yield self[dataset]

    @staticmethod
    def save_feature(filename: str, gdf: gpd.geodataframe.GeoDataFrame, driver: str = "ESRI Shapefile"):
        """Save observations to file.

        Args:
            filename (str): The path or filename.
            gdf (geodataframe): geodataframe to save.
            driver (str): Drive (type) of output file.
        """
        gdf.to_file(filename, encoding="utf-8", driver=driver)

    @property
    def url(self):
        """Return the WFS server instance URL."""
        return self.__wfs.host

    def __str__(self):
        """Return the string representation of the SAMPLEDB object."""
        text = f'SAMPLEDB:\n\tURL: {self.__wfs.host}'

        return text

    def __repr__(self):
        """Return the SAMPLEDB object representation."""
        text = f'sampledb(url="{self.__wfs.host}")'

        return text

    def _repr_html_(self):
        """HTML repr."""
        ds_list = self._list_datasets()

        html = Utils.render_html('sample.html', url={self.__wfs.host}, datasets=ds_list)

        return html

    def _ipython_key_completions_(self):
        """Integrate key completions for SAMPLE in IPython.

        Returns:
            list: The list of available datasets in the service.

        Raises:
            ConnectionError: If the server is not reachable.
            HTTPError: If the server response indicates an error.
            ValueError: If the response body is not a json document.
        """
        return self._list_datasets()
