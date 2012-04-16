# -*- coding: utf-8 -*-
from grab.spider import Spider

from models import Item
from config import Session


class BaseHubSpider(Spider):
    initial_urls = ['http://github.com']

    items_total = 0

    def save(self, data):
        session = Session()

        if not session.query(Item).filter_by(title=data['title']).first():
            obj = Item(**data)
            session.add(obj)
        session.commit()

    def log_progress(self, str):
        self.items_total += 1
        print "Item scraped: %s" % str