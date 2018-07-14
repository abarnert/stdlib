#!/usr/bin/env python3

import importlib
import shelve
import sys

# TODO: pkgresource this!
_db = shelve.open('names', 'r')

def __getattr__(self, name):
    if name not in _db:
        raise AttributeError(name)
    values = _db[name]
    if len(values) > 1:
        possibilities = ', '.join(f"'{mod}.{name}'" for mod, name in values)
        raise AttributeError(f"'{name}' is ambiguous: could be {possibilities}")
    mod, name = values[0]
    try:
        return getattr(importlib.import_module(mod), name)
    except AttributeError:
        pass
    return importlib.import_module(f'{mod}.{name}')

def __dir__(self):
    return [name for name, values in _db.items() if len(values) == 1]
    
if sys.version_info < (3, 7):
    import types
    class DynamicModule(types.ModuleType):
        pass
    DynamicModule.__getattr__ = __getattr__
    DynamicModule.__dir__ = __dir__
    sys.modules[__name__].__class__ = DynamicModule
