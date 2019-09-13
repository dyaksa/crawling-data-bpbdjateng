import scrapy
from ..items import BpbdItem

class BeritaSpider(scrapy.Spider):
    name = "berita"
    start_urls = [
        "https://bpbd.jatengprov.go.id/category/laporan-bencana/"
    ]

    custom_settings = {
        'ITEM_PIPELINES' : {
            'crawling-data-bpbdjateng.pipelines.BpbdPipeline' : 300
        }
    }


    def parse(self, response):
        items = BpbdItem()
        div_post_type = response.css("div.type-post")

        for kegiatan in div_post_type:
            posted_by = kegiatan.css("p.postmetadataw::text")[0].extract()
            date = kegiatan.css("p.postmetadataw::text")[1].extract()
            title = kegiatan.css("h2.post-title a::text").extract()
            author = kegiatan.css("p.postmetadataw a::text")[0].extract()
            text = kegiatan.css("div.entrytext p::text").extract()
            tag = kegiatan.css("p.postmetadata a::text").extract()
            tag.pop()

            items['title'] = title
            items['text'] = text
            items['tag'] = ",".join(str(x) for x in tag)
            items['autwak'] = posted_by + author + date

            yield items

            next_page = response.css("div#page-nav div.alignright a::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page,callback = self.parse)

