#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for SampleDB."""
from typing import List

import geopandas as gpd
import requests

from .dataset import Dataset
from .utils import Utils


class SAMPLE:
    """Create wfs clients attached to given host addresses.

    .. note::
        For more information about coverage definition, please, refer to
        `Sample-DB <https://github.com/brazil-data-cube/sample-db>`_.
    """

    def __init__(self, url, access_token=None, lccs_url=None):
        """Create a WLTS client attached to the given host address (an URL).

        Args:
            url (str): URL for the WLTS server.
            access_token (str, optional): Authentication token to be used with the WLTS server.
        """
        self._url = url.rstrip('/')
        self._access_token = access_token
        self._lccs_url = lccs_url if lccs_url else 'https://brazildatacube.dpi.inpe.br/lccs'

    def _describe_dataset(self, dataset_id: str = None, dataset_name: str = None, dataset_version: str = None) -> dict:
        """Describe a give collection.

        :param dataset_id: The collection name.
        :type dataset_id: str.
        :returns: Collection description.
        :rtype: dict
        """
        return Utils._get(
            f'{self._url}/datasets?dataset_id={dataset_id}&dataset_name={dataset_name}&dataset_version={dataset_version}',
            **dict(access_token=self._access_token))

    def dataset(self, dataset_id: int = None, dataset_name: str = None, dataset_version: str = None) -> Dataset:
        """Return the given collection.

        :param dataset_id: A id for a given dataset.
        :type dataset_id: str
        :param dataset_name: A id for a given dataset.
        :type dataset_name: str
        :param dataset_version: A id for a given dataset.
        :type dataset_version: str
        """
        try:
            ds_metadata = self._describe_dataset(dataset_id, dataset_name, dataset_version)
        except requests.HTTPError as e:
            raise KeyError(f'Could not retrieve information for dataset!')
        return Dataset(self, url=self._url, data=ds_metadata, lccs=self._lccs_url)

    def _list_datasets(self) -> List[dict]:
        """Return a list of all dataset available.

        Returns:
          list: A list with the available dataset in service.
        """
        features = Utils._get(url=f'{self._url}/datasets', **dict(access_token=self._access_token))

        return features["datasets"]

    @property
    def datasets(self) -> List[dict]:
        """Return a list of all dataset available.

        Returns:
          list: A list with the available dataset in service.
        """
        return self._list_datasets()

    @staticmethod
    def save_feature(filename: str, gdf: gpd.geodataframe.GeoDataFrame, driver: str = "ESRI Shapefile") -> None:
        """Save dataset data to file.

        Args:
            filename (str): The path or filename.
            gdf (geodataframe): geodataframe to save.
            driver (str): Drive (type) of output file.
        """
        gdf.to_file(filename, encoding="utf-8", driver=driver)

    def add_dataset(self, name: str, title: str, description: dict, start_date: str, end_date: str,
                    classification_system_id: int, is_public: bool, collect_method_id: str, version: str,
                    version_predecessor: int = None, version_successor: int = None,
                    metadata: dict = None) -> dict:
        """Add a new dataset."""
        url = f'{self._url}/datasets'
        header = {"x-api-key": self._access_token}

        data = dict()
        data["name"] = name
        data["title"] = title
        data["version"] = version
        data["description"] = description
        data["start_date"] = start_date
        data["end_date"] = end_date
        data["classification_system_id"] = classification_system_id
        data["is_public"] = is_public
        data["collect_method_id"] = collect_method_id

        if metadata:
            data["metadata"] = metadata

        if version_predecessor:
            data["version_predecessor"] = version_predecessor

        if version_successor:
            data["version_successor"] = version_successor

        try:
            retval = Utils._post(url, json=data, header=header)
        except RuntimeError as e:
            raise ValueError(f'Could not insert dataset {title}!')

        return retval

    def add_dataset_data(self,  samples: dict, dataset_id: int = None, dataset_name: str = None, dataset_version: str = None) -> dict:
        """Add a new dataset."""
        url = f'{self._url}/datasets/data'
        if dataset_id:
            url += f"?dataset_id={dataset_id}"
        elif dataset_name and dataset_version:
            url += f"?dataset_name={dataset_name}&dataset_version={dataset_version}"
        else:
            raise ValueError(f'You must inform the dataset!')

        header = {"x-api-key": self._access_token}

        try:
            retval = Utils._post(url, json=samples, header=header)
        except RuntimeError as e:
            raise ValueError(f'Could not insert data into dataset!')

        return retval

    @property
    def url(self) -> str:
        """Return the Server instance URL."""
        return self._url

    @property
    def lccs_url(self) -> str:
        """Return the LCCCS server instance URL."""
        return self._lccs_url

    def __iter__(self) -> str:
        """Iterate over collections available in the service.

        Returns:
            A dataset at each iteration.

        """
        for dataset in self.datasets:
            yield self.dataset(dataset["id"])

    def __str__(self) -> str:
        """Return the string representation of the SAMPLE object."""
        text = f'SAMPLE:\n\tURL: {self.url}'

        return text

    def __repr__(self) -> str:
        """Return the SAMPLE object representation."""
        text = f'sample(url="{self.url}")'

        return text

    def _repr_html_(self) -> str:
        """HTML repr."""
        ds_list = self._list_datasets()

        html = Utils.render_html('sample.html', url={self.url}, datasets=ds_list)

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
