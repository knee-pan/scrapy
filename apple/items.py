# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AppleItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    sku = scrapy.Field()
    product_price = scrapy.Field()
    product_category = scrapy.Field()
    product_imagelink = scrapy.Field()
    #shot = scrapy.Field()
