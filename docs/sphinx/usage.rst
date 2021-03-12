..
    This file is part of Python Client Library for Sample Database Model.
    Copyright (C) 2020-2021 INPE.

    Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.



Running sample Client in the Command Line
=========================================

List the available datasets::

    sample-cli --url 'https://brazildatacube.dpi.inpe.br/bdc/geoserver' --user 'user' datasets

The above command will return a list of dataset names as:

.. code-block:: shell

    ['BDC Sample Dataset - Test Area',
     'Amostras Campo Verde MT (Campo Verde Database)',
     'Insitu Mato Grosso State (Brazil) Land Use and Land Cover Samples 1.8K',
     'Insitu Mato Grosso State (Brazil) Land Use and Land Cover Samples 2K']

Retrieve the information given a dataset name::

    sample-cli --url 'https://brazildatacube.dpi.inpe.br/bdc/geoserver' --user 'user' describe-dataset 'BDC Sample Dataset - Test Area'

The above command will return a JSON document as:

.. code-block:: shell

    {'classification_system_name': 'BDC',
     'collect_method': 'VISUAL',
     'created_at': '2020-04-17T13:37:53.016Z',
     'description': 'Brazil Data Cube samples of study areas',
     'end_date': '2019-08-31Z',
     'id': 6,
     'midias_table_name': None,
     'name': 'area_bdc_all',
     'observation_table_name': 'area_bdc_all_observations',
     'start_date': '2018-09-01Z',
     'updated_at': '2020-04-17T13:37:53.016Z',
     'user_name': 'Fabiana Zioti',
     'version': '1'}

Retrieve the metadata given a dataset name::

    sample-cli --url 'https://brazildatacube.dpi.inpe.br/bdc/geoserver' --user 'user' dataset-metadata 'BDC Sample Dataset - Test Area'

The above command will return a JSON document as:

.. code-block:: shell

    {'agency': 'INPE',
     'contributors': [{'@type': 'Person',
                       'familyName': 'Picoli',
                       'givenName': 'Michelle'},
                      {'@type': 'Person',
                       'familyName': 'Simoes',
                       'givenName': 'Rolf'},
                      {'@type': 'Person',
                       'familyName': 'Chaves',
                       'givenName': 'Michel'}],
     'creators': [{'@type': 'Person',
                   'familyName': 'Picoli',
                   'givenName': 'Michelle'},
                  {'@type': 'Person', 'familyName': 'Simoes', 'givenName': 'Rolf'},
                  {'@type': 'Person',
                   'familyName': 'Chaves',
                   'givenName': 'Michel'}],
     'dates': [{'date': '2019', 'dateType': 'Issued'}],
     'descriptions': [{'description': 'This dataset include samples for the three '
                                      'test sites used by the Brazilian Data Cube '
                                      'project.',
                       'descriptionType': 'Abstract',
                       'lang': 'en'}],
     'formats': [],
     'fundingReferences': [{'awardNumber': '17.2.0536.1',
                            'awardTitle': 'Brazil Data Cube project',
                            'funderName': 'Amazon Fund through the financial '
                                          'collaboration of the Brazilian '
                                          'Development Bank (BNDES), and the '
                                          'Foundation for Science, Technology and '
                                          'Space Applications (FUNCATE) (process '
                                          'number 17.2.0536.1, Brazil Data Cube '
                                          'project)'},
                           {'awardNumber': '88887.351470/2019-00',
                            'funderName': 'Coordination for the Improvement of '
                                          'Higher Education Personnel (CAPES) '
                                          '(process number 88887.351470/2019-00)'}],
         'geoLocations': [],
         'id': 'test_sites_bdc',
         'language': 'en',
         'rightsList': [{'rights': 'Creative Commons Attribution 4.0 International',
                         'rightsUri': 'https://creativecommons.org/licenses/by/4.0/'}],
         'schemaVersion': 'http://datacite.org/schema/kernel-4',
         'sizes': [],
         'state': 'findable',
         'subjects': [{'lang': 'en', 'subject': 'Brazil Data Cube'},
                      {'lang': 'en', 'subject': 'sutdy areas'},
                      {'lang': 'en', 'subject': 'Cerrado'}],
         'titles': [{'lang': 'en', 'title': 'Brazil Data Cube samples of study areas'}],
         'types': {'bibtex': 'misc',
                   'citeproc': 'dataset',
                   'resourceType': 'Dataset',
                   'resourceTypeGeneral': 'Dataset',
                   'ris': 'DATA',
                   'schemaOrg': 'Dataset'},
         'version': '1.0'}


Save a observation given a observation table name and a filename option (File path or file handle to write to)::

    sample-cli --url 'https://brazildatacube.dpi.inpe.br/bdc/geoserver' --user 'reader' save-observations 'area_bdc_all_observations' --filename '/home/data/observation_name.shp'

Save a observation given a observation table name and driver (The OGR format driver used to write the vector file). See all format type [#f1]_. ::

    sample-cli --url 'https://brazildatacube.dpi.inpe.br/bdc/geoserver' --user 'reader' save-observations 'area_bdc_all_observations' --filename '/home/data/observation_name.geojson' --driver 'GeoJSON'



.. rubric:: Footnotes

.. [#f1] Supported formats type: ESRI Shapefile, GeoJSON, CSV, GML.