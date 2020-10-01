..
    This file is part of Python Client Library for SampleDB.
    Copyright (C) 2019 INPE.

    Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Installation
============

``sample.py`` depends essentially on `Requests <https://requests.readthedocs.io/en/master/>`_ and `Geopandas <https://geopandas.org/>`_ . Please, read the instructions below in order to install ``sample.py``.

Production installation
-----------------------

**Under Development!**

Development installation
------------------------

Clone the software repository:

.. code-block:: shell

        $ git clone https://github.com/brazil-data-cube/sample.py.git

Go to the source code folder:

.. code-block:: shell

        $ cd sample.py

Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]

Run the tests:

.. code-block:: shell

        $ ./run-test.sh

Generate the documentation:

.. code-block:: shell

        $ python setup.py build_sphinx

The above command will generate the documentation in HTML and it will place it under:

.. code-block:: shell

    doc/sphinx/_build/html/