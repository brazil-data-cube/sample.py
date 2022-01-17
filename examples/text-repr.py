#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows how the various text representation for services."""

from sample import *

service = SAMPLE(url='http://127.0.0.1:5000/', access_token='change-me')

print(service)
print(str(service))
print(repr(service))
print(service._repr_html_())

