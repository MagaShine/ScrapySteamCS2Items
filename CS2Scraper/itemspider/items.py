# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

def serializer_prise(value):
    return f"${str(value)}"

class SteamItem(scrapy.Item):
    url = scrapy.Field()
    profit = scrapy.Field()
    selling_price = scrapy.Field()
    buying_price = scrapy.Field()

