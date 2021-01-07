# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import collections


try:
    from mock import mock
except ImportError:  # pragma: no cover
    try:
        import mock
    except ImportError:  # pragma: no cover
        from unittest import mock  # noqa # pragma: no cover

try:
    collectionsAbc = collections.abc
except AttributeError:  # pragma: no cover
    collectionsAbc = collections  # noqa # pragma: no cover
