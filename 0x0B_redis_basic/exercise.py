#!/usr/bin/env python3
"""Writing strings to Redis """

import redis
from typing import Union
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
