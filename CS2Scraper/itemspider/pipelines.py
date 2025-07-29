# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os



class ItemspiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('selling_price') != []:
            value = adapter.get('selling_price')
            adapter['selling_price'] = float(value[0])

        if adapter.get('buying_price') != []:
            value = adapter.get('buying_price')
            adapter['buying_price'] = float(value) / 100




        return item

class SaveToPostgreSQLPipeLine:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'postgres'),
            port=os.environ.get('DB_PORT', '5432'),
            dbname=os.environ.get('DB_NAME', 'items'),
            user=os.environ.get('DB_USER', 'admin'),
            password=os.environ.get('DB_PASSWORD', 'admin123')
        )
        print("Connected to PostgreSQL. SaveToPostgreSQLPipeLine working.")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS SteamCSGO2items (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL UNIQUE,  
            profit DECIMAL NOT NULL,
            buying_price DECIMAL NOT NULL,
            selling_price DECIMAL NOT NULL
            );
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cur.execute("""
                INSERT INTO SteamCSGO2items (url, profit, buying_price, selling_price)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (url) DO UPDATE SET
                    profit = EXCLUDED.profit,
                    buying_price = EXCLUDED.buying_price,
                    selling_price = EXCLUDED.selling_price;
            """, (item['url'], item['profit'], item['buying_price'], item['selling_price']))
            self.conn.commit()
            return item
        except Exception as e:
            print(f"Error {e}")
            self.conn.rollback()
            return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
        print("Closet connection to PostgreSQL ")

    def stop_spider(self,spider):
        spider.logger.info("Database connection closed")
        self.cur.close()
        self.conn.close()