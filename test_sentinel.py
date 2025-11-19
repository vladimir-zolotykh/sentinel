#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import pytest
import pickle

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


def test_sentinel_custom_repr():
    assert repr(SentinelCustomRepr) == "***SentinelRepr***"


def test_pickle():
    s = pickle.dumps(SentinelCustomRepr)
    unserialized = pickle.loads(s)
    assert SentinelCustomRepr is unserialized


def test_sentinel_comes_ready_to_use():
    assert repr(Sentinel) == "Sentinel"
    s = pickle.dumps(Sentinel)
    unserialized = pickle.loads(s)
    unserialized is Sentinel
    # assert repr(unserialized) == "Sentinel"
