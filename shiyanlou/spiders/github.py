# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import GithubItem

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for github in response.css('li.public'):
            item = GithubItem({
                'name': github.css('div.mb-1 a::text').extract_first().strip(),
                'update_time': github.css('relative-time ::attr(datetime)').extract_first()
            })
            yield item

