#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure, PyMongoError


def log_infos() -> None:
    """ Provides some stats about Nginx logs stored in MongoDB. """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        client.admin.command('ping')  # Check if the server is available
    except ConnectionFailure:
        print("Server not available")
        return
    except PyMongoError as e:
        print(f"An error occurred: {e}")
        return

    try:
        nginx = client.logs.nginx

        print(f"{nginx.count_documents({})} logs")

        print("Methods:")
        for method in methods:
            print(f"\tmethod {method}: {nginx.count_documents({'method': method})}")

        print(f"{nginx.count_documents({'method': 'GET', 'path': '/status'})} status check")
    except OperationFailure as e:
        print(f"Database operation failed: {e}")
    except PyMongoError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    log_infos()