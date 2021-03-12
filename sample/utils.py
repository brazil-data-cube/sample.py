#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Utility functions for SampleDB library."""
import jinja2
from pkg_resources import resource_filename
from shapely.geometry import (LineString, MultiPoint, MultiPolygon, Point,
                              Polygon)

templateLoader = jinja2.FileSystemLoader(searchpath=resource_filename(__name__, 'templates/'))
templateEnv = jinja2.Environment(loader=templateLoader)


class Utils:
    """Utils SampleDB object."""

    @staticmethod
    def _get_feature(wfs, **kwargs):
        """Get feature using wfs and return the result as a JSON document."""
        invalid_parameters = set(kwargs) - {"name", "geometry_name"}

        if invalid_parameters:
            raise AttributeError('invalid parameter(s): {}'.format(invalid_parameters))

        js = wfs.get_feature(kwargs['name'])

        fc = dict()

        fc['features'] = []

        for item in js['features']:

            if item['geometry']['type'] == 'Point':
                feature = {kwargs['geometry_name']: Point(item['geometry']['coordinates'][0],
                                                          item['geometry']['coordinates'][1])}
            elif item['geometry']['type'] == 'MultiPoint':
                points = []
                for point in item['geometry']['coordinates']:
                    points += [Point(point)]
                feature = {kwargs['geometry_name']: MultiPoint(points)}

            elif item['geometry']['type'] == 'LineString':
                feature = {kwargs['geometry_name']: LineString(item['geometry']['coordinates'])}

            elif item['geometry']['type'] == 'MultiPolygon':
                polygons = []
                for polygon in item['geometry']['coordinates']:
                    polygons += [Polygon(lr) for lr in polygon]
                feature = {kwargs['geometry_name']: MultiPolygon(polygons)}

            elif item['geometry']['type'] == 'Polygon':
                feature = {kwargs['geometry_name']: Polygon(item['geometry']['coordinates'][0])}

            else:
                raise Exception('Unsupported geometry type.')

            del item['properties']['bbox']

            feature.update(item['properties'])
            fc['features'].append(feature)

        fc['crs'] = js['crs']

        return fc

    @staticmethod
    def render_html(template_name, **kwargs):
        """Render Jinja2 HTML template."""
        template = templateEnv.get_template(template_name)
        return template.render(**kwargs)
