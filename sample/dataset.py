#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for SampleDB."""

class DataSet(dict):
    """DataSet Class."""

    def __init__(self, data):
        """Initialize instance with dictionary data.

        :param data: Dict with class system metadata.
        """
        super(DataSet, self).__init__(data or {})

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