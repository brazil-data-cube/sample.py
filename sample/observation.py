#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""A class that represents a Observation in SampleDB."""

import json


class Observation(dict):
    """DataSet Class."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(Observation, self).__init__(data or {})

    @property
    def id(self):
        """Return the observation id."""
        return self['id']

    @property
    def user_name(self):
        """Return the observation user name."""
        return self['user_name']

    @property
    def created_at(self):
        """Return the observation created_at."""
        return self['created_at']

    @property
    def updated_at(self):
        """Return the observation updated_at."""
        return self['updated_at']
