# Scrapy settings for itemspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
BOT_NAME = "itemspider"

SPIDER_MODULES = ["itemspider.spiders"]
NEWSPIDER_MODULE = "itemspider.spiders"
# в FEEDS МОЖНО УКАЗЫВАТЬ КАК ИНФОРМАЦИЯ БУДЕТ СОХРАНЯТЬСЯ
# FEEDS = {
#     'itemsdata.json' : {'format':'json', 'overwrite':True},
# }
# PROXY = 'http://localhost:8080'
# ROTATING_PROXY_LIST = [
# '103.8.115.27:48644',
# '87.248.129.32:80',
# '169.239.45.51:4153'
# ]
# # ROTATING_PROXY_LIST_PATH = '/home/stefan/Downloads/ready_proxy_list(1).txt'
# ROTATING_PROXY_SKIP_INITIAL_CHECK = True
# ROTATING_PROXY_FORCE_ROTATE = True
# ROTATING_PROXY_CLOSE_SPIDER = False
# ROTATING_PROXY_BACKOFF_BASE = 5
# ROTATING_PROXY_LOGSTATS_INTERVAL = 5

# ua = UserAgent()
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = ua.random

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DUPEFILTER_DEBUG = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 3
# CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   # "Accept-Language": "en",
    "Accept": "text/html",
    "Accept-Encoding": "gzip, deflate"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   "itemspider.middlewares.ItemspiderSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "itemspider.middlewares.ItemspiderDownloaderMiddleware": 543,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    # 'itemspider.middlewares.HaProxyMiddleware': 745,
    # "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    # "rotating_proxies.middlewares.BanDetectionMiddleware": 620
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "itemspider.pipelines.ItemspiderPipeline": 300,
    "itemspider.pipelines.SaveToPostgreSQLPipeLine": 400,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 10
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 0.5
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False # Все сделанные запросы будут сохраняться в кеш
HTTPCACHE_GZIP = False
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = [429] #Запросы с таким кодом не будут добавлены в кеш
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
