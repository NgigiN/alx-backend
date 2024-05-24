#!/usr/bin/env python3
"""This implements a basic cache"""

baseCaching = __import__('base_caching').BaseCaching


class BasicCache(baseCaching):
    """Represents objects that store and retrieve times
    from a dictionary.
    """

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrives items using key"""
        return self.cache_data.get(key, None)
