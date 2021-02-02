import scrapy
from ..items import AnguilaItem
import re

class AnguSpider(scrapy.Spider):
    name = 'angu'
    allowed_domains = ['www.republicbankanguilla.com/']
    start_urls = ['http://www.republicbankanguilla.com/message-our-managing-director/',
                  'https://www.republicbankanguilla.com/change-banking-hours'
                  ]

    def parse(self, response):
        article = (response.xpath('(//div[@class="field field--name-field-paragraph-content field--type-text-long field--label-hidden field--item"])[1]//text()').getall())
        articles = ''.join(a for a in article if a not in ' \t\n')
        articles = re.sub("\n","",articles)
        articles = re.sub("\t", "", articles)

        item = AnguilaItem()
        item['articles'] = articles,
        yield item


