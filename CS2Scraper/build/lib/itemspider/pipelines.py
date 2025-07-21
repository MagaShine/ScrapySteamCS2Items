# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# КОНСТРУКЦИЯ adapter.get('selling_price') ЗАБИРАЕТ ТЕКУЩЕЕ ЗНАЧЕНИЕ ITEMA
# adapter['selling_price'] = float(value[0]) А ЭТОЙ СТРОЧКОЙ МЫ ОБРАБАТЫВАЕМ ПРЕДМЕТ, КАК НАМ УГОДНО И
# ПЕРЕЗАПИСЫВАЕМ ЕГО ЗНАЧЕНИ НА ТО, КАКОЕ НАМ НУЖНО

class ItemspiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('selling_price') != []:
            value = adapter.get('selling_price')
            adapter['selling_price'] = float(value[0])

        if adapter.get('buying_price') != []:
            value = adapter.get('buying_price')
            adapter['buying_price'] = float(value) / 100



        # field_names = adapter.field_names()
        # for field_name in field_names:
        #     if field_name == 'buying_price':
        #         if adapter.get(field_name) != []:
        #             value = adapter.get(field_name[0])
        #             adapter[field_name] = value.replace('--','')

        return item

class SaveToPostgreSQLPipeLine:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="maindb",
            user="admin",

            password="admin123"
        )
        print("Подключение к PostgreSQL установлено. SaveToPostgreSQLPipeLine инициализирован.")
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
    def process_item(self,item,spider):

        self.cur.execute(f"""INSERT INTO SteamCSGO2items (url, profit, buying_price, selling_price)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (url) DO UPDATE 
        SET profit = EXCLUDED.profit,
            buying_price = EXCLUDED.buying_price,
            selling_price = EXCLUDED.selling_price
         """,
        (
        # item["item_nameid"],
        item["url"],
        item["profit"],
        item["selling_price"],
        item["buying_price"]
        )
        )
        self.conn.commit()  # Важно делать коммит после каждой вставки
        spider.logger.info(f"Успешно сохранен item с url: {item.get('url')}")
        return item

    def close_spider(self,spider):
        spider.logger.info("Закрываю соединение с БД")
        self.cur.close()
        self.conn.close()

    def stop_spider(self,spider):
        spider.logger.info("Закрываю соединение с БД")
        self.cur.close()
        self.conn.close()