# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class BpbdPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "crawling-data-bpbdjateng"
        )

        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS berita """)
        self.curr.execute("""create table berita(
                            id INT NULL AUTO_INCREMENT KEY,
                            judul text,
                            autwak text,
                            isi text,
                            tag text
                            
                        )""")

    def store_db(self,item):
        self.curr.execute("""insert into berita (judul,autwak,isi,tag) values(%s,%s,%s,%s)""",(
            item['title'][0],
            item['autwak'],
            item['text'][0],
            item['tag']
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item


class KegiatanPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crawling-data-bpbdjateng"
        )

        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS kegiatan """)
        self.curr.execute("""create table kegiatan(
                            id INT NULL AUTO_INCREMENT KEY,
                            judul text,
                            gambar text,
                            autwak text,
                            isi text,
                            tag text

                        )""")

    def store_db(self, item):
        self.curr.execute("""insert into kegiatan(judul,gambar,autwak,isi,tag) values(%s,%s,%s,%s,%s)""", (
            item['title'][0],
            item['image'],
            item['autwak'],
            item['text'][0],
            item['tag']
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

class PpidPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crawling-data-bpbdjateng"
        )

        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS ppid """)
        self.curr.execute("""create table ppid(
                            id INT NULL AUTO_INCREMENT KEY,
                            judul text,
                            pejabat text,
                            penanggung text,
                            waktu text,
                            jangka text,
                            ringkasan text,
                            keterangan text
                        )""")

    def store_db(self, item):
        self.curr.execute("""insert into ppid(judul,pejabat,penanggung,waktu,jangka,ringkasan,keterangan) values(%s,%s,%s,%s,%s,%s,%s)""", (
            item['judul'],
            item['pejabat'],
            item['penanggung'],
            item['waktu'],
            item['jangka'],
            item['ringkasan'],
            item['keterangan']

        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item