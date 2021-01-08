# -*- coding: utf-8 -*-
import scrapy
import w3lib.html


class IetfAllSpider(scrapy.Spider):
    name = 'ietf_all'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
            'title': response.xpath('//span[@class="title"]/text()').get(),
            'author_name': response.xpath('//span[@class="author-name"]/text()').get(),
            'email': response.xpath('//span[@class="email"]/text()').get(),
            'phone': response.xpath('//span[@class="phone"]/text()').get(),
            'description': response.xpath('//meta[@name="DC.Description.Abstract"]//@content').get(),
            'date': response.xpath('//span[@class="date"]/text()').get(),
            'text':  w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())

        }
