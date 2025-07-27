import re
import os
from os import environ

import scrapy
from fake_useragent import UserAgent
from scrapy import Request
from scrapy.http import HtmlResponse
from yarl import URL

from itemspider.items import SteamItem


# todo СДЕЛАТЬ DOCKER-COMPOSE FILE ДЛЯ BACKEND, FRONTEND, DB ЧТОБЫ ИЗ КОРОБКИ МОЖНО БЫЛО ЗАПУСТИТЬ.

class SteamspiderSpider(scrapy.Spider):
    name = "steamspider"
    allowed_domains = ["steamcommunity.com"]
    ua = UserAgent()

    def start_requests(self):
        yield Request(
            (URL("https://steamcommunity.com/market/search/render/")
            % {
                "query": "",
                "start": 4000,
                "count": 100,
                "search_descriptions": 0,
                "sort_column": "price",
                "sort_dir": "desc",
                "appid": 730,
            }).human_repr()
        )

    # p2_popular_desc
    def parse(self, response: HtmlResponse):
        data = response.text
        proxy= os.getenv('PROXY')
        count = re.findall(r"\"total_count\":(\d+)", data)
        qty = re.findall(r"data-qty=\\\"(\d+)\\\"", data)
        steam_url = URL("https://steamcommunity.com/market/listings/730/")
        next_page = URL("https://steamcommunity.com/market/search/render/") % {
            "query": "",
            "start": 0,
            "count": 100,
            "search_descriptions": 0,
            "sort_column": "price",
            "sort_dir": "desc",
            "appid": 730,
        }
        buying_prices = re.findall(r'data-price=\\"(\d+)', data)
        href = re.findall(r"market\\/listings\\/730\\/([\w%.\-]+)", data)
        for i in range(len(href)):
            if float(qty[i]) != 0:
                price = float(buying_prices[i]) / 100
                if 1 <= price <= 100:
                    next_item_page = str(steam_url.joinpath(href[i], encoded=True))
                    yield response.follow(
                        next_item_page,
                        callback=self.parse_item_page,
                        meta={"buying_price": buying_prices[i],
                              'proxy': proxy},
                        headers={"User-Agent": self.ua.random}
                    )
                else:
                    print("out of price")
                #     return None
                # (math.ceil(int(count[0])/10))
        for i in range(5000, 7000, 100):
            yield response.follow(
                str(next_page.update_query({"start": i})),
                callback=self.parse,
                headers={"User-Agent": self.ua.random},
                meta={'proxy': proxy}
            )
#'https://tl-0ade6b79ad1035b33f36c9a279f7f5510e3204d1be0e00e8dd13ef85c7f30ca0-country-us-session-2eb63:xgbfiqxmi1ox@proxy.toolip.io:31114'
    # headers = {"User-Agent": self.ua.random}
    # f"https://steamcommunity.com/market/listings/730/{i}"

    def parse_item_page(self, response: HtmlResponse):
        steamitem = SteamItem()
        data = response.text
        scripts =  response.xpath("//script[@type='text/javascript'][contains(text(), 'var g_rgAppContextData')]/text()").get()
        buying_price = response.meta.get("buying_price")
        selling_price = re.findall(
            r"\D+\d+ \d+ \d+: \+\d\",(\d+.\d+),\"\d+\"\]\];", scripts
        )
        if selling_price == []:
            print("selling_price 0")
            return None
        else:
            profit = (float(selling_price[0]) - (float(buying_price) / 100)) * 0.9
            if profit != 0.0:
                steamitem["profit"] = round(profit, 2)
                steamitem["selling_price"] = selling_price
                steamitem["buying_price"] = buying_price
                steamitem["url"] = response.url
                yield steamitem

