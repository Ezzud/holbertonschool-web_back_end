#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB.
"""
import pymongo

def log_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.

    The function connects to the MongoDB database, retrieves the total number of logs,
    counts the number of documents for each HTTP method (GET, POST, PUT, PATCH, DELETE),
    and counts the number of GET requests to the /status path. It then prints these statistics
    in a specified format.
    """
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
