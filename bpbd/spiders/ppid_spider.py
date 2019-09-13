import scrapy
from ..items import PpidItem

class PpidSpider(scrapy.Spider):
    name = "ppid"
    allowed_domains = ['crawling-data-bpbdjateng.jatengprov.go.id']
    start_urls = [
        'http://bpbd.jatengprov.go.id/PPID/informasi-serta-merta/',
        'http://bpbd.jatengprov.go.id/PPID/informasi-berkala/',
        'http://bpbd.jatengprov.go.id/PPID/informasi-setiap-saat/',
        'http://bpbd.jatengprov.go.id/PPID/informasi-dikecualikan/'
    ]

    custom_settings = {
        'ITEM_PIPELINES' : {
            'crawling-data-bpbdjateng.pipelines.PpidPipeline' : 500
        }
    }

    def parse(self, response):
        items = PpidItem()
        for p in response.xpath('//tbody/tr'):
            items['kategori'] = response.css('h1.entry-title::text').get()
            items['no'] = p.xpath('td[1]/text()').get()
            items['judul'] = p.xpath('td[2]/text()').get()
            items['pejabat'] = p.xpath('td[3]/text()').get()
            items['penanggung'] = p.xpath('td[4]/text()').get()
            items['waktu'] = p.xpath('td[5]/text()').get()
            # format1 = p.xpath('td[6]/text()').get()
            items['jangka'] = p.xpath('td[7]/text()').get()
            items['ringkasan'] = p.xpath('td[8]/text()').get()
            # items['jdl_tabel'] = p.xpath('./td/strong').get()
            # 'jdl_tabel': p.css('tbody > tr > td > strong').extract_first()

            if items['kategori'] == "Informasi Dikecualikan":
                items['keterangan'] = p.xpath('td[9]/text()').get()
            else:
                items['keterangan'] = p.xpath('td[9]/a/text()').get()

            yield items
