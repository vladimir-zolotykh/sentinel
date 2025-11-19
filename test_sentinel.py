#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pytest

from run import Sentinel


class PlainSentinel(Sentinel):
    pass


class SentinelCustomRepr(Sentinel):
    repr = "***SentinelRepr***"


def test_repr():
    assert repr(PlainSentinel) == "PlainSentinel"


def test_cannot_instantiate():
    with pytest.raises(TypeError) as e:
        PlainSentinel()
    msg = "'PlainSentinel' is a sentinel(=singleton) and cannot be instantiated"
    assert msg in str(e.value)
