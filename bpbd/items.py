# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BpbdItem(scrapy.Item):
    # define the fields for your item here like:
    autwak = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()
    # pass

class KegiatanItem(scrapy.Item):
    title = scrapy.Field()
    autwak = scrapy.Field()
    image = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()

class PpidItem(scrapy.Item):
    no = scrapy.Field()
    judul = scrapy.Field()
    pejabat = scrapy.Field()
    penanggung =scrapy.Field()
    waktu = scrapy.Field()
    jangka = scrapy.Field()
    ringkasan = scrapy.Field()
    keterangan = scrapy.Field()
    kategori = scrapy.Field()
    jdl_tabel = scrapy.Field()
