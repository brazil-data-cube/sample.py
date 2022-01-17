#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Utility functions for SampleDB library."""
import jinja2
import requests
from pkg_resources import resource_filename

templateLoader = jinja2.FileSystemLoader(searchpath=resource_filename(__name__, 'templates/'))
templateEnv = jinja2.Environment(loader=templateLoader)


class Utils:
    """Utils SampleDB object."""

    @staticmethod
    def _get(url, **params):
        """Query the Sample service using HTTP GET verb and return the result as a JSON document.

        :param url: The URL to query must be a valid Sample endpoint.
        :type url: str

        :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the underlying `Requests`.

        :type params: dict
        :rtype: dict

        :raises ValueError: If the response body does not contain a valid json.
        """
        response = requests.get(url, params=params)

        response.raise_for_status()

        content_type = response.headers.get('content-type')

        if content_type.count('application/json') == 0:
            raise ValueError('HTTP response is not JSON: Content-Type: {}'.format(content_type))

        return response.json()

    @staticmethod
    def render_html(template_name, **kwargs):
        """Render Jinja2 HTML template."""
        template = templateEnv.get_template(template_name)
        return template.render(**kwargs)
