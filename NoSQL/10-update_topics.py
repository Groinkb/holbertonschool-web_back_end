#!/usr/bin/env python3
""" Python function """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a document on the name
    """
    name = {"name": name}
    topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(name, topics)