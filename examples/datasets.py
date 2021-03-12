#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows the list of datasets in a service."""

from sample import *

service = SAMPLE('https://brazildatacube.dpi.inpe.br/bdc/geoserver', auth=("user", "password"))

print(service.datasets)
