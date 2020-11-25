..
    This file is part of Python Client Library for SampleDB.
    Copyright (C) 2019 INPE.

    Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Installation
============

``sample.py`` depends essentially on `Requests <https://requests.readthedocs.io/en/master/>`_ , `Shapely <https://shapely.readthedocs.io/en/stable/manual.html>`_ and `Geopandas <https://geopandas.org/>`_ . Please, read the instructions below in order to install ``sample.py``.

Production installation
-----------------------

**Under Development!**

Development Installation - GitHub
---------------------------------

Clone the Software Repository
+++++++++++++++++++++++++++++

Use ``git`` to clone the software repository::

        $ git clone https://github.com/brazil-data-cube/sample.py.git

Install sample.py in Development Mode
+++++++++++++++++++++++++++++++++++++

Go to the source code folder:

.. code-block:: shell

        $ cd sample.py

Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]

.. note::

    If you want to create a new *Python Virtual Environment*, please, follow this instruction:

    **1.** Create a new virtual environment linked to Python 3.7::

        python3.7 -m venv venv


    **2.** Activate the new environment::

        source venv/bin/activate


    **3.** Update pip and setuptools::

        pip3 install --upgrade pip

        pip3 install --upgrade setuptools

    Or you can use Python Anaconda Environment:

    **1.** Create an virtual environment using conda with Python Interpreter Version +3::

        conda create --name bdc-sample python=3

    **2.** Activate environment::

        conda activate bdc-sample


Run the Tests
+++++++++++++

Run the tests:

.. code-block:: shell

        $ ./run-test.sh


Build the Documentation
+++++++++++++++++++++++

Generate the documentation:

.. code-block:: shell

        $ python setup.py build_sphinx

The above command will generate the documentation in HTML and it will place it under:

.. code-block:: shell

    doc/sphinx/_build/html/