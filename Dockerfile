# Dockerfile для ScrapydWeb
FROM python:3.13-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Установка ScrapydWeb
RUN pip install --no-cache-dir scrapydweb

# Создание рабочей директории
WORKDIR /app

# Создание директории для данных
RUN mkdir -p /app/data /app/app/data

# Установка переменных окружения
ENV DATA_PATH=/app/data
ENV DATABASE_URL=sqlite:////app/data/scrapydweb.db

# Копирование настроек ScrapydWeb (если есть)
COPY ./CS2Scraper/scrapydweb_settings_v11.py /app/

# Экспозиция порта
EXPOSE 5000

# Установка рабочей директории для настроек
ENV SCRAPYDWEB_SETTINGS_MODULE=scrapydweb_settings_v11

# Команда запуска ScrapydWeb
CMD ["scrapydweb"]