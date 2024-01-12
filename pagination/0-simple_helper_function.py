#!/usr/bin/env python3
"""function index_range"""


def index_range(page, page_size):
    """
    returns a tuple of size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    find_page = (start_index, end_index)
    return find_page
