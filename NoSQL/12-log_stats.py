#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB
database: logs, collection: nginx"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

        status_check = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")