#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python Client Library for SampleDB."""
from .sample import sample
from .version import __version__
from .wfs import WFS

__all__ = ('__version__', 'WFS', 'sample', )