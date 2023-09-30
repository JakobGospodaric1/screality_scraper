# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityScraperPipeline:
    def __init__(self):
        hostname = 'localhost'
        username = 'postgres'
        password = 'mojeGeslo1'
        database = 'sreality_flats'

        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        self.cur = self.connection.cursor()

        #create table if it doesn't exist
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flats(
            id SERIAL PRIMARY KEY,
            title TEXT,
            images TEXT[]
        )
        """)

    def process_item(self, item, spider):
        #put images into array
        images = []
        for image in item['images']:
            images.append(image['href'])

        #insert data
        self.cur.execute("""
        INSERT INTO flats (title, images) VALUES (%s, %s)
        """,(
            item['title'], 
            images,
        ))

        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


