#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This example shows how to retrieve and plot a dataset and observations."""
from sample import *

service = SAMPLE(url='http://127.0.0.1:5001/', access_token='0itRKnWR0qsxrSa0WB59Fydozbb93FRuaWXakCldZ3')

ds = service.dataset(dataset_id=1)

print(ds)

observations = ds.data()
print(observations.dtypes)

print(observations.head())

observation = ds.data(data_id=1)
print(observation.head())