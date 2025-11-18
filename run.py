#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class _SentinelMeta(type):
    def __repr__(cls):
        try:
            return cls.repr
        except AttributeError:
            return cls.__name__


class Sentinel(metaclass=_SentinelMeta):
    def __new__(cls):
        msg = f"{cls} is singleton and cannot be instantiated"
        raise TypeError(msg)


class Missing(Sentinel):
    repr = "Missing"


class DELETED(Sentinel):
    repr = "DELETED"


if __name__ == "__main__":
    print(Missing)
