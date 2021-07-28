#!/usr/bin/env python3
"""Simple pagination"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with
        default value 1 and page_size with default value 10"""
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        a, b = index_range(page, page_size)
        return self.dataset()[a:b]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary"""
        total = math.ceil(len(self.dataset()) / page_size)
        dictionary = {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total
        }
        return dictionary


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two
    containing a start index and an end index"""
    return ((page - 1) * page_size, page_size * page)
