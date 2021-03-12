 #!/usr/bin/env bash
#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle sample  setup.py && \
isort --check-only --diff sample setup.py && \
check-manifest --ignore ".drone.yml,.readthedocs.yml" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest && \
pytest