#!/usr/bin/env python3
"""This module implements LRU caching"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This class adds information to a cache using LRU"""

    def __init__(self):
        """This initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.order = []

    def put(self, key, item):
        """This Adds item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
