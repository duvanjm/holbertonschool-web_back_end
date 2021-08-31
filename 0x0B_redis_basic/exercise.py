#!/usr/bin/env python3
"""Writing strings to Redis """

import redis
from typing import Union, Callable
from uuid import uuid4


class Cache():
    """Writing strings to Redis """

    def __init__(self) -> None:
        """init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> Callable:
        """convert the data back to the desired format"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: str) -> str:
        """ parametrize Cache.get with
        the correct conversion function"""
        return str(data.encode('utf-8'))

    def get_int(self, number: int) -> int:
        """ parametrize Cache.get with
        the correct conversion function"""
        return int(number)
