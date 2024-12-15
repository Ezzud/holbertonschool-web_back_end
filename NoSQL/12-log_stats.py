#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def log_infos() -> None:
    """ Provides some stats about Nginx logs stored in MongoDB. """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        client.admin.command('ping')  # Check if the server is available
    except ConnectionFailure:
        print("Server not available")
        return

    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")

    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {nginx.count_documents({'method': method})}")

    print(f"{nginx.count_documents({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    log_infos()