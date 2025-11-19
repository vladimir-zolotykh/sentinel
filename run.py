#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> print(Missing)
Missing
>>> Missing is Missing
True
>>> DELETED is Missing
False
>>> print(CANCELLED)
CANCELLED
>>> Missing()
Traceback (most recent call last):
...
TypeError: 'Missing' is a sentinel(=singleton) and cannot be instantiated
"""


class _SentinelMeta(type):
    def __repr__(cls):
        try:
            return cls.repr
        except AttributeError:
            return cls.__name__


class Sentinel(metaclass=_SentinelMeta):
    def __new__(cls):
        msg = "is a sentinel(=singleton) and cannot be instantiated"
        raise TypeError(f"{cls.__name__!r} {msg}")


class Missing(Sentinel):
    repr = "Missing"


class DELETED(Sentinel):
    repr = "DELETED"


class CANCELLED(Sentinel):
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
