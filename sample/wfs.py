#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""This class implements the WFS client."""

import json
from http.client import responses
from xml.dom import minidom

import requests

WFSFormats = {
    'shp': 'shape-zip',
    'kml': 'kml',
    'csv': 'csv',
    'json': 'application/json'
}


class WFS:
    """A class that describes a WFS."""

    def __init__(self, host, **kwargs):
        """Create  a WFS client attached to the given host address.

        Args:
            host (URL): The WFS url.
            kwargs (dict): The user and password.
        """
        self.host = host
        self.base_path = "wfs?service=wfs&version=1.0.0"
        self.__debug = False

        invalid_parameters = set(kwargs) - {"auth"}
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

    def _get(self, uri):
        """Query the WFS service.

        Args:
            uri (str): URL for the WFS server.
        """
        response = requests.get(uri, auth=self.__auth)

        if response.status_code != 200:
            raise Exception("Request Fail: {} ".format(responses[response.status_code]))

        return response.content.decode('utf-8')

    def list_features(self):
        """Return the list of features."""
        url = "{}/{}&request=GetCapabilities&outputFormat=application/json".format(self.host, self.base_path)

        doc = self._get(url)

        xmldoc = minidom.parseString(doc)
        itemlist = xmldoc.getElementsByTagName('FeatureType')

        features = dict()
        features[u'features'] = []

        for s in itemlist:
            features[u'features'].append(s.childNodes[0].firstChild.nodeValue)

        return features

    def describe_feature(self, ft_name):
        """Return features metadata."""
        if not ft_name:
            raise ValueError("Missing feature name.")

        url = "{}/{}&request=DescribeFeatureType&typeName={}&outputFormat=application/json". \
            format(self.host, self.base_path, ft_name)

        doc = self._get(url)

        js = json.loads(doc)

        feature = dict()
        feature['name'] = js['featureTypes'][0]['typeName']
        feature['namespace'] = js['targetPrefix']
        feature['full_name'] = "{}:{}".format(feature['namespace'], feature['name'])

        feature['attributes'] = []
        supported_geometries = ['gml:MultiPolygon', 'gml:Point', 'gml:Polygon']
        for prop in js['featureTypes'][0]['properties']:
            attr = {'name': prop['name'], 'localtype': prop['localType'], 'type': prop['type']}
            feature['attributes'].append(attr)
            if prop['type'] in supported_geometries:
                feature['geometry'] = attr

        return feature

    def get_feature(self, ft_name, **kwargs):
        """Return the feature."""
        if not ft_name:
            raise ValueError("Missing feature name.")

        url = "{}/{}&request=GetFeature&typeName={}".format(self.host, self.base_path, ft_name)

        if 'max_features' in kwargs:
            url += "&maxFeatures={}".format(kwargs['max_features'])

        if 'bbox' in kwargs:
            url += '&bbox={}'.format(kwargs['bbox'])

        if 'filter' in kwargs:
            url += "&cql_filter={}".format(kwargs['filter'])

        output = "application/json"

        if 'output' in kwargs:
            output = "{}".format(WFSFormats[kwargs['output']])

        url += "&outputFormat={}".format(output)

        doc = self._get(url)

        js = json.loads(doc)

        return js
