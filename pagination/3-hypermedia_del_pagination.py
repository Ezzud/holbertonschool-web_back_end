#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate the data
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Dataset in cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Index of the dataset
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Function get_hyper that return a dict"""
        assert type(index) is int and type(page_size) is int
        assert len(self.indexed_dataset()) > index >= 0
        pages = []
        next_index = index + page_size
        for i in range(index, index + page_size):
            if not self.indexed_dataset().get(i):
                i += 1
                next_index += 1
            pages.append(self.indexed_dataset()[i])
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': pages
        }
