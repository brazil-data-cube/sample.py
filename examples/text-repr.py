#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows how the various text representation for services."""

from sample import *

service = SAMPLE('https://brazildatacube.dpi.inpe.br/bdc/geoserver', auth=("user", "password"))

print(service)
print(str(service))
print(repr(service))
print(service._repr_html_())

