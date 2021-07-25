#!/usr/bin/env python3
"""FIFOCache is caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class that inherits from
    BaseCaching and is a caching system"""

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary the
        item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for k, v in self.cache_data.items():
                print('DISCARD:', list(self.cache_data.keys())[0])
                break
            self.cache_data.pop(k)

    def get(self, key):
        """return the value in
        self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
