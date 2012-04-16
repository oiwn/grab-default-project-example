# -*- coding: utf-8 -*-
"""
Crawl trendings from http://github.com/explore
"""
from grab.spider import Spider

from spiders.base import BaseHubSpider

class ExploreSpider(BaseHubSpider):
    initial_urls = ['http://github.com/explore']

    def task_initial(self, grab, task):
        repos = grab.xpath_list('//ol[@class="ranked-repositories"]/li')
        for repo in repos[:5]:
            data = {
                'author': repo.xpath('./h3/a[1]/text()')[0],
                'title': repo.xpath('./h3/a[2]/text()')[0],
                'url': grab.make_url_absolute(
                    repo.xpath('./h3/a[2]/@href')[0], resolve_base=True),
                'description': repo.xpath(
                    './p[@class="description"]/text()')[0]
            }

            self.save(data)
            self.log_progress(data['author'] + ' / ' + data['title'])