# Dockerfile для Scrapy проекта
FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование requirements.txt и установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Создание директорий для логов и eggs
RUN mkdir -p /app/logs /app/eggs /app/dbs

# Установка переменных окружения для Scrapy
ENV SCRAPY_SETTINGS_MODULE=itemspider.settings
ENV PYTHONPATH=/app

# Экспозиция порта для Scrapyd
EXPOSE 6800

# Команда запуска Scrapyd
CMD ["scrapyd"]