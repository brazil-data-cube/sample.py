..
    This file is part of Python Client Library for Sample Database Model.
    Copyright (C) 2020-2021 INPE.

    Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

Pre-Requirements
----------------

``sample.py`` depends essentially on:

- `Requests <https://requests.readthedocs.io/en/master/>`_  Requests is a simple, yet elegant HTTP library.

- `Shapely <https://shapely.readthedocs.io/en/stable/manual.html>`_ Shapely is a BSD-licensed Python package for manipulation and analysis of planar geometric objects..

- `Geopandas <https://geopandas.org/>`_  GeoPandas is an open source project to make working with geospatial data in python easier.

Please, read the instructions below in order to install ``sample.py``.

Development Installation - GitHub
---------------------------------

Clone the Software Repository
+++++++++++++++++++++++++++++

Use ``git`` to clone the software repository::

        $ git clone https://github.com/brazil-data-cube/sample.py.git

Install sample.py in Development Mode
+++++++++++++++++++++++++++++++++++++

Go to the source code folder::

    cd sample.py

Install in development mode::

    pip3 install -e .[all]

.. note::

    If you want to create a new *Python Virtual Environment*, please, follow this instruction:

    **1.** Create a new virtual environment linked to Python 3.7::

        python3.7 -m venv venv


    **2.** Activate the new environment::

        source venv/bin/activate


    **3.** Update pip and setuptools::

        pip3 install --upgrade pip

        pip3 install --upgrade setuptools

    For more information, see [#f1]_.

    Or you can use Python Anaconda Environment:

    **1.** Create an virtual environment using conda with Python Interpreter Version +3::

        conda create --name bdc-sample python=3

    **2.** Activate environment::

        conda activate bdc-sample


Run the Tests
+++++++++++++

Run the tests::

    ./run-test.sh


Build the Documentation
+++++++++++++++++++++++

You can generate the documentation based on Sphinx with the following command::

    python setup.py build_sphinx

The above command will generate the documentation in HTML and it will place it under::

    docs/sphinx/_build/html/


You can open the above documentation in your favorite browser, as::

    firefox docs/sphinx/_build/html/index.html


Production Installation - GitHub
--------------------------------


Install from GitHub::

    pip3 install git+https://github.com/brazil-data-cube/sample.py


.. rubric:: Footnotes

.. [#f1]

    Shapely 1.7 requires GEOS >=3.3, if you have a build message such as the one showed below:

    .. code-block::

        OSError: /path/lib/libgeos_c.so: cannot open shared object file: No such file or directory

    You can instruct ``pip`` to look at the right place for header files when building Shapely:

    .. code-block:: shell

        $LD_LIBRARY_PATH="/usr/local/lib/" \
        pip3 install shapely
