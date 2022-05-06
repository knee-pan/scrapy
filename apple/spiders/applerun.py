# Ayse GUNDUZ
#  scrapy genspider applerun https://www.apple.com/tr/shop/buy-mac/macbook-pro
import json

import scrapy
from apple.items import AppleItem


class ApplerunSpider(scrapy.Spider):
    name = 'applerun'
    allowed_domains = ['www.apple.com']
    start_urls = ['https://www.apple.com/tr/shop/buy-mac/macbook-pro']
    delimiter = ";"
    quotechar = "'"
    headers = ["product_name", "product_color", "product_price", "product_imagelink"]

    def parse(self, response):
        items = AppleItem()
        json_data = json.loads(response.xpath('//script[@type="application/json"]/text()').extract_first())
        # items['shot'] = json_data['data']
        items['product_name'] = [data['name'] for data in json_data['data']['products']]
        items['product_category'] = [data['category'] for data in json_data['data']['products']]
        items['sku'] = response.xpath(
            '//input[contains(@class,"colornav-value rc-dimension-colornav-input")]/@value').extract()
        items['product_price'] = response.css('.rc-prices-fullprice').css('::text').extract()
        json_img = response.xpath('//script[contains(@type,"application/ld+json")]/text()').getall()
        items['product_imagelink'] = [json.loads(json_img).get('image') for json_img in json_img]

        yield items
