#!/usr/bin/env python3
"""MRUCache is caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class that inherits from
    BaseCaching and is a caching system"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.lst = []

    def put(self, key, item):
        """assign to the dictionary the
        item value for the key key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.lst.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.lst.pop(-2)
            print('DISCARD:', last)
            del self.cache_data[last]

    def get(self, key):
        """return the value in
        linked to key"""
        if key in self.cache_data:
            self.lst.append(key)
        if key in self.cache_data:
            return self.cache_data[key]
