#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# -*- mode: python -*-
"""
Module with some useful objects and functions for programming in python
(e.g. decorators, handy caches, etc)

Copyright (C) 2009,  Daniel Meliza <dmeliza@meliza-laptop-1.uchicago.edu>
Created 2009-06-08
"""

from decorator import decorator

# memoizing functions from http://pypi.python.org/pypi/decorator

def _memoize(func, *args, **kw):
    if kw: # frozenset is used to ensure hashability
        key = args, frozenset(kw.iteritems())
    else:
        key = args
    cache = func.cache # attributed added by memoize
    if key in cache:
        return cache[key]
    else:
        cache[key] = result = func(*args, **kw)
        return result

def memoize(f):
    f.cache = {}
    return decorator(_memoize, f)


# Variables:
# indent-tabs-mode: t
# End:
