#!/usr/bin/env python3
"""simple pagination project """
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """returns a tuple containing the start and end index of a page """
    start_index = int(page_size * (page - 1))
    end_index = int(page * page_size)
    return (start_index, end_index)


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
        """
        gets the page number and page size
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        index = index_range(page, page_size)
        index_start, index_end = index
        dataset = self.dataset()
        return dataset[index_start: index_end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dict
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)
        next_page = page + 1

        if next_page > total_pages:
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        dict = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return dict
