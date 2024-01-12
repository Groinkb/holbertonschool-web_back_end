#!/usr/bin/env python3
""" Python function """
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    returns lists of all docs in collection
    """
    return [doc for doc in mongo_collection.find()]