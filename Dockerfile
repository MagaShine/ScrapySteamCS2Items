FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir scrapydweb

WORKDIR /app

RUN mkdir -p /app/data /app/app/data

ENV DATA_PATH=/app/data
ENV DATABASE_URL=sqlite:////app/data/scrapydweb.db

COPY ./CS2Scraper/scrapydweb_settings_v11.py /app/

EXPOSE 5000

ENV SCRAPYDWEB_SETTINGS_MODULE=scrapydweb_settings_v11

CMD ["scrapydweb"]