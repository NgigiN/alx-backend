#!/usr/bin/env python3
"""This module contains a simple helper function"""


def index_range(page, page_size):
    """This function returns a tuple of size 2 containing
    a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
