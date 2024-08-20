#!/usr/bin/env python3
""" Function index_range
"""


def index_range(page, page_size):
    """Return a tuple with start index
    and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
