# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from typing import Mapping


try:
    from mock import mock
except ImportError:  # pragma: no cover
    try:
        import mock
    except ImportError:  # pragma: no cover
        from unittest import mock  # noqa # pragma: no cover

try:
    from collections.abc import Mapping
except ImportError:  # pragma: no cover
    import collections.Mapping as Mapping