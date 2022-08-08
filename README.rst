..
    This file is part of Python Client Library for Sample Database Model.
    Copyright (C) 2020-2022 INPE.

    Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


============================================
Python Client Library for Sample Web Service
============================================


.. image:: https://img.shields.io/badge/license-MIT-green
        :target: https://github.com//brazil-data-cube/sample.py/blob/master/LICENSE
        :alt: Software License

.. image:: https://drone.dpi.inpe.br/api/badges/brazil-data-cube/sample.py/status.svg
        :target: https://drone.dpi.inpe.br/brazil-data-cube/sample.py
        :alt: Build Status

.. image:: https://codecov.io/gh/brazil-data-cube/sample.py/branch/master/graph/badge.svg?token=KCJM9B3058
        :target: https://codecov.io/gh/brazil-data-cube/sample.py
        :alt: Code Coverage Test

.. image:: https://readthedocs.org/projects/sample/badge/?version=latest
        :target: https://lccs.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/lifecycle-experimental-orange.svg
        :target: https://www.tidyverse.org/lifecycle/#experimental
        :alt: Software Life Cycle

.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord

About
=====

Currently, several projects systematically provide information on the dynamics of land use and cover. Well known projects include PRODES, DETER and TerraClass. These projects are developed by INPE and they produce information on land use and coverage used by the Brazilian Government to make public policy decisions. Besides these projects there are other initiatives from universities and space agencies devoted to the creation of national and global maps.

These data products are generated using different approaches and methodologies. In this context, the data set used in the sample and validation plays a fundamental role in the classification algorithms that generate new land use and coverage maps. A classified map’s accuracy depends directly on the quality of the training samples used by the machine learning methods.

Land use and cover samples are collected by different projects and individuals, using different methods, such as in situ gathering in fieldwork and visual interpretation of high-resolution satellite images. An important requirement is to be able to describe samples with proper metadata that characterize their differences and organize them in a shared database to facilitate the reproducibility of experiments. It is also important to develop tools to easily discover, query, access, and process this shared sample database.

The SAMPLE-DB (Sample Database) provides a data model representing the land use and land cover samples collected by different projects and individuals. SAMPLE-DB-UTILS, has utility functions that perform the transformation of different data formats to be stored by SAMPLE-DB and SAMPLE-WS (Sample Web Service) provides a high-level interface to perform access to stored data.


To facilitate access to samples of land use and land cover stored in the database, a Python package called **SAMPLE.py** was developed. This package retrieves the land use and land cover samples that were made available by the Sample Web Service.

This package is related to other softwares in the Brazil Data Cube project:

- `SAMPLE-DB <https://github.com/brazil-data-cube/sample-db>`_: Sample Database Model.

- `SAMPLE-DB-UTILS <https://github.com/brazil-data-cube/sample-db-utils>`_: Utility Functions for the SAMPLE-DB.

- `SAMPLE-WS <https://github.com/brazil-data-cube/sample-db>`_: Sample Web Service.

- `SAMPLE.py <https://github.com/brazil-data-cube/sample.py>`_: Python Client Library for SAMPLE-WS.

- `LCCS-DB <https://github.com/brazil-data-cube/lccs-db>`_: Land Cover Classification System Database Model.

- `LCCS-WS-SPEC <https://github.com/brazil-data-cube/lccs-ws-spec>`_: Land Cover Classification System Web Service specification.

- `LCCS-WS <https://github.com/brazil-data-cube/lccs-ws>`_: Land Cover Classification System Web Service implementation.

- `LCCS.py <https://github.com/brazil-data-cube/lccs.py>`_: Python Client Library for Land Cover Classification System Web Service.

Installation
============


Install from GitHub::

    pip3 install git+https://github.com/brazil-data-cube/sample.py


Documentation
=============


See https://samplepy.readthedocs.io/en/latest/


License
=======

.. admonition::
    Copyright (C) 2020-2022 INPE.

    Python Client Library for Sample Database Model. is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.