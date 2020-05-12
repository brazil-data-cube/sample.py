 #!/usr/bin/env bash
#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle sample && \
isort --check-only --diff --recursive **/*.py && \
check-manifest --ignore ".travis-*" && \
pytest