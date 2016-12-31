from django.db import models

# This file defines the business entities of the recommendation engine.

# class SocialNetwork(models.Model):
#     name = models.CharField(max_length=30)
#     api_token = models.CharField(max_length=100)
#     api_secret = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = 'social_network'
#
# class SocialNetworkAccount(models.Model):
#     access_token = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = 'social_network_account'
#
# class Tag(models.Model):
#     def __init__(self, name, related):
#         self.name = name
#         self.score = 0
#         self.related = list()
#
#     def increment_score(self, increment):
#         self.name += increment
#
#     def decrement_score(self, decrement):
#         self.name -= decrement
#
# class NewsItem(models.Model):
#     def __init__(self, url, date_time, tags):
#         self.url = url
#         self.published = date_time
#         self.tags = tags
#
# class Suggestion(models.Model):
#     def __init__(self, news_item):
#         self.news_item = news_item
#         self.up_voted = False
#         self.down_voted = False
