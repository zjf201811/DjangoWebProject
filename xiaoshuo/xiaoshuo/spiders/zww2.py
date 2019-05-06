# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'

    allowed_domains = ['shushu8.com']
    start_urls = [r'http://www.shushu8.com/jiubadao/liemingshichuanqi/']
    n=0
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="clearfix dirconone"][1]/ul/li[1]/a'), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="fanye"]/a[last()]'), callback="parse_item", follow=True),
        # 获取对象即可  不需要具体的值
    )

    def parse_item(self, response):
        print(self.n)
        self.n+=1
        title = response.xpath('//title/text()').extract()[-1]
        content = ''.join(response.xpath('//pre[@id="content"]/text()').extract())
        # next_url = response.xpath("//div[@class='fanye']/a[last()]/@href").extract_first()

        # title=response.xpath('//h1/text()').extract()[0]
        # content = ''.join(response.xpath('//div[@id="content"]/text()').extract())
        # next_url = response.xpath("//div[@class='page_chapter']/ul/li[3]/a/@href").extract_first()

        # content=''.join(response.xpath("//div[@id='content']/text()").extract())
        # next_url = response.xpath("//div[@class='bottem1']/a[3]/@href").extract_first()
        print(title,content)
        yield {
            'title': title,
            'content': content
        }
        # if next_url=="/book/16664/":
        # if next_url=='/27_27495/':
        # if next_url == '/b_2q.htm':
        #     return
        # base_urls = 'https://www.zwdu.com{}'.format(next_url)
        # print(12345)
        # yield scrapy.Request(response.urljoin(next_url), callback=self.parse, dont_filter=True)

