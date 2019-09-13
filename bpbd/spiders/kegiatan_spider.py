import scrapy
from ..items import KegiatanItem


class KegiatanSpider(scrapy.Spider):
    name = "kegiatan"

    start_urls = [
        "https://bpbd.jatengprov.go.id/category/kegiatan/"
    ]

    custom_settings = {
        'ITEM_PIPELINES' : {
            'crawling-data-bpbdjateng.pipelines.KegiatanPipeline' : 400
        }
    }

    def parse(self, response):
        # all_div_kegiatan = response.css("div.type-post")
        # for kegiatan in all_div_kegiatan:
        urls = response.css("h2.post-title a::attr(href)").extract()
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse_detail)

        #pagination link
        next_page = response.css("div#page-nav div.alignright a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)

    def parse_detail(self,response):
        items = KegiatanItem()

        title = response.css("div#content h1.page-title::text").extract()
        posted_by = response.css("div#content p.postmetadataw::text")[0].extract()
        date = response.css("div#content p.postmetadataw::text")[1].extract()
        author = response.css("div#content p.postmetadataw a::text")[0].extract()
        image = response.css("div.entrytext img::attr(src)")[0].extract()
        isi = response.css("div.entrytext p::text").extract()
        tag = response.css("div.up-bottom-border p.postmetadata a::text").extract()
        tag.pop()

        items['title'] = title
        items['image'] = image
        items['tag'] = ','.join(str(x) for x in tag)
        items['text'] = isi
        items['autwak'] = posted_by + author + date

        yield items
