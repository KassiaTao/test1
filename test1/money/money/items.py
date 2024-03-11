# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ForeignexchangeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    currency_name = scrapy.Field()
    spot_purchase_price = scrapy.Field()
    cash_purchase_price = scrapy.Field()
    spot_selling_price = scrapy.Field()
    cash_selling_price = scrapy.Field()
    boc_discounted_price = scrapy.Field()
    release_time = scrapy.Field()