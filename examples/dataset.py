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

"""This example shows how to retrieve and plot a dataset and observations."""
from sample import *

service = SAMPLE(
    lccs_url='https://brazildatacube.dpi.inpe.br/lccs/',
    url='https://brazildatacube.dpi.inpe.br/sample/',
    access_token='change-me',
    language='en'
)

ds = service.dataset(dataset_id=1)

print(ds)

observations = ds.data()
print(observations.dtypes)

observation = ds.data(data_id=1)
print(observation.head())