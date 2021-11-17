#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows how to retrieve and plot a dataset and observations."""
from sample import *

service = SAMPLE(url='http://127.0.0.1:5000/', access_token='change-me')

ds = service.dataset(dataset_id=1)

print(ds)

observations = ds.data()
print(observations.dtypes)

print(observations.head())

observation = ds.data(data_id=1)
print(observation.head())