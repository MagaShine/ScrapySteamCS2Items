# coding: utf-8
import os

# QUICK SETUP - Основные настройки для Docker
SCRAPYDWEB_BIND = '0.0.0.0'
SCRAPYDWEB_PORT = 5000

# Отключаем авторизацию для упрощения
ENABLE_AUTH = False
USERNAME = ''
PASSWORD = ''

# Настройка подключения к Scrapyd в Docker
SCRAPYD_SERVERS = [
    'scrapy:6800',  # Используем имя сервиса из docker-compose
]

CHECK_SCRAPYD_SERVERS = False

# Настройки для работы с логами в Docker
LOCAL_SCRAPYD_SERVER = 'scrapy:6800'
LOCAL_SCRAPYD_LOGS_DIR = '/app/logs'
ENABLE_LOGPARSER = True

# HTTPS отключен
ENABLE_HTTPS = False
CERTIFICATE_FILEPATH = ''
PRIVATEKEY_FILEPATH = ''

# Scrapy проекты
SCRAPY_PROJECTS_DIR = ''

# Scrapyd настройки
SCRAPYD_LOG_EXTENSIONS = ['.log', '.log.gz', '.txt']
SCRAPYD_SERVERS_PUBLIC_URLS = None

# LogParser
BACKUP_STATS_JSON_FILE = True

# Timer Tasks
JOBS_SNAPSHOT_INTERVAL = 300
CHECK_TASK_RESULT_INTERVAL = 300
KEEP_TASK_RESULT_LIMIT = 1000
KEEP_TASK_RESULT_WITHIN_DAYS = 31

# Run Spider настройки
SCHEDULE_EXPAND_SETTINGS_ARGUMENTS = False
SCHEDULE_CUSTOM_USER_AGENT = 'Mozilla/5.0'
SCHEDULE_USER_AGENT = None
SCHEDULE_ROBOTSTXT_OBEY = None
SCHEDULE_COOKIES_ENABLED = None
SCHEDULE_CONCURRENT_REQUESTS = None
SCHEDULE_DOWNLOAD_DELAY = None
SCHEDULE_ADDITIONAL = "-d setting=CLOSESPIDER_TIMEOUT=60\r\n-d setting=CLOSESPIDER_PAGECOUNT=10\r\n-d arg1=val1"

# Page Display
SHOW_SCRAPYD_ITEMS = True
SHOW_JOBS_JOB_COLUMN = True
JOBS_FINISHED_JOBS_LIMIT = 0
JOBS_RELOAD_INTERVAL = 300
DAEMONSTATUS_REFRESH_INTERVAL = 10

# Send Text настройки (отключены для Docker)
SLACK_TOKEN = ''
SLACK_CHANNEL = 'general'
TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = 0

# Email настройки (отключены)
EMAIL_SUBJECT = 'Email from #scrapydweb'
EMAIL_USERNAME = ''
EMAIL_PASSWORD = ''
EMAIL_SENDER = ''
EMAIL_RECIPIENTS = []
SMTP_SERVER = ''
SMTP_PORT = 0
SMTP_OVER_SSL = False
SMTP_CONNECTION_TIMEOUT = 30

# Monitor & Alert (отключены)
ENABLE_MONITOR = False
POLL_ROUND_INTERVAL = 300
POLL_REQUEST_INTERVAL = 10
ENABLE_SLACK_ALERT = False
ENABLE_TELEGRAM_ALERT = False
ENABLE_EMAIL_ALERT = False
ALERT_WORKING_DAYS = []
ALERT_WORKING_HOURS = []

# Triggers (отключены)
ON_JOB_RUNNING_INTERVAL = 0
ON_JOB_FINISHED = False
LOG_CRITICAL_THRESHOLD = 0
LOG_ERROR_THRESHOLD = 0
LOG_WARNING_THRESHOLD = 0
LOG_REDIRECT_THRESHOLD = 0
LOG_RETRY_THRESHOLD = 0
LOG_IGNORE_THRESHOLD = 0

# System настройки для Docker
DEBUG = False
VERBOSE = False
# DATA_PATH = os.environ.get('DATA_PATH', '/app/data')
# DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///app/data/scrapydweb.db')