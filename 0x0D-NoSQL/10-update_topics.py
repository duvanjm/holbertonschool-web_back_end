#!/usr/bin/env python3
"""Change school topics """


def update_topics(mongo_collection, name, topics):
    """function that changes all
    topics of a school document"""
    mongo_collection.update_many({"name": name},
                                 {"$set":
                                 {"topics": topics}})
