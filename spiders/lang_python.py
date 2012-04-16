# -*- coding: utf-8 -*-
from grab.spider import Spider

from spiders.base import BaseHubSpider

class LangPythonSpider(BaseHubSpider):
    initial_urls = ['https://github.com/languages/Python/most_watched']

    def task_initial(self, grab, task):
        repos = grab.xpath_list(
            '//table[@class="repo"]//tr/td[@class="title"]/..')
        for repo in repos:
            data = {
                'author': repo.xpath('./td[@class="owner"]/a/text()')[0],
                'title': repo.xpath('./td[@class="title"]/a/text()')[0],
                'url': grab.make_url_absolute(
                    repo.xpath('./td[@class="title"]/a/@href')[0],
                    resolve_base=True),
                'description': repo.xpath(
                    './following::tr/td[@class="desc"]/text()')[0]
            }

            self.save(data)
            self.log_progress(data['author'] + ' / ' + data['title'])