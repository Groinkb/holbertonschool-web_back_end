#!/usr/bin/env python3
""" Python function """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    query = {"topics": {"$elemMatch": {"$eq": topic}}}
    result = mongo_collection.find(query)
    return result