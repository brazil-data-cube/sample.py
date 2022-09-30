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
    def _post(url, data=None, json=None, files=None, header=None):
        """Request post method."""
        response = requests.post(url, data=data, files=files, json=json, headers=header)

        response.raise_for_status()

        return response.json()

    @staticmethod
    def _delete(url, params=None):
        """Request delete method."""
        response = requests.delete(url, params=params)

        response.raise_for_status()

        return response

    @staticmethod
    def render_html(template_name, **kwargs):
        """Render Jinja2 HTML template."""
        template = templateEnv.get_template(template_name)
        return template.render(**kwargs)
