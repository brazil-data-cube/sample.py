#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows how to retrieve and plot a dataset and observations."""
from sample import *

service = SAMPLE('https://brazildatacube.dpi.inpe.br/bdc/geoserver', auth=("user", "password"))

ds = service['LAPIG-Pontos-Visualmente-Inspecionados-Treinamento']

print(ds)

observation = ds.observation

observation.plot(marker='o', color='red', markersize=5, figsize=(20, 20))
