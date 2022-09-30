..
    This file is part of Python Client Library for SAMPLE-WS.
    Copyright (C) 2022 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.



Running sample Client in the Command Line
=========================================

List the available datasets::

    sample-cli --url 'http://127.0.0.1:5000/' --access-token 'change-me' datasets

The above command will return a list of dataset names as::

    {'id': 4, 'name': 'bdc-go-test-area', 'version': '1'}
    {'id': 3, 'name': 'bdc-ba-test-area', 'version': '1'}
    {'id': 6, 'name': 'bdc-all-test-area', 'version': '1'}
    {'id': 3, 'name': 'bdc-ba-test-area', 'version': '1'}

Retrieve the information given a dataset name::

    sample-cli --url 'http://127.0.0.1:5000/' --access-token 'change-me' describe-dataset  --dataset_id 3

The above command will return a JSON document as::

    {
        'classification_system_id': 1,
        'classification_system_name': 'BDC',
        'classification_system_version': '1.0',
        'collect_method_id': 2,
        'collect_method_name': 'VISUAL',
        'metadata_json': {'agency': 'INPE', 'contributors': .....},
        'end_date': '2019-08-31T00:00:00Z',
        'id': 3,
        'is_public': True,
        'version': '1',
        .....
     }

Save a observation given a observation table name and a filename option (File path or file handle to write to)::

    sample-cli --url 'http://127.0.0.1:5000/' --access-token 'change-me' export-data  --dataset_id 3 --filename '/home/data/observation_name.shp'


Save a observation given a observation table name and driver (The OGR format driver used to write the vector file). See all format type [#f1]_. ::

    sample-cli --url 'http://127.0.0.1:5000/' --access-token 'change-me' export-data  --dataset_id 3 --filename '/home/data/observation_name.shp' --driver 'GeoJSON'

Create new dataset::

    sample-cli --url 'http://127.0.0.1:5000/' --access-token 'change-me' add-dataset \
                --name 'bdc-dataset' \
                --title 'Brazil Data Cube Dataset' \
                --description "Description of dataset" \
                --version '1' \
                --classification_system_id 1 \
                --collect_method_id 2 \
                --start_date '2017-07-01' \
                --end_date '2018-08-31'

Insert data into dataset::

    sample-cli --url 'http://127.0.0.1:5001/' --access-token 'change-me' insert-dataset-data \
                --dataset_id 20 \
                --samples examples/add_sample.json


.. rubric:: Footnotes

.. [#f1] Supported formats type: ESRI Shapefile, GeoJSON, CSV, GML.