# Ayse GUNDUZ
#  scrapy genspider applerun https://www.apple.com/tr/shop/buy-mac/macbook-pro
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
        # product name iconic+text olarak verilmiş
        items['product_name'] = response.css('.rc-productbundle-title::text').extract()
        items['product_color'] = response.css('.rc-productbundle-activecolorlabel::text').extract()
        items['product_price'] = response.css('.rc-prices-fullprice').css('::text').extract()
        items['product_imagelink'] = response.css('.rc-productbundle , img.rc-productbundle-image').css('::attr(src)').extract()
        # iki renk için iki defa gösteriyor sonucu
        yield items
