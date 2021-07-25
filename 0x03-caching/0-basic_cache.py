#!/usr/bin/env python3
"""basic cache is caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class that inherits from
    BaseCaching and is a caching system"""

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value
        for the key key"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """return the value in self.cache_data
        linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
