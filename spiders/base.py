# -*- coding: utf-8 -*-
from grab.spider import Spider

from models import Item
from config import Session, SAVE_TO_DB


class BaseHubSpider(Spider):
    initial_urls = ['http://github.com']

    items_total = 0

    def save(self, data):
        if not SAVE_TO_DB:
            return
            
        session = Session()

        if not session.query(Item).filter_by(title=data['title']).first():
            obj = Item(**data)
            session.add(obj)
        session.commit()

    def log_progress(self, str):
        self.items_total += 1
        print "(%d) Item scraped: %s" % (self.items_total, str)