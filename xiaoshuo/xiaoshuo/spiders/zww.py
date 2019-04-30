# -*- coding: utf-8 -*-
import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['zwdw.com']
    start_urls = ['http://www.shushu8.com/jiubadao/liemingshichuanqi/1']

    def parse(self, response):
        title=response.xpath('//title/text()').extract()[-1]
        content = ''.join(response.xpath('//pre[@id="content"]/text()').extract())
        next_url = response.xpath("//div[@class='fanye']/a[last()]/@href").extract_first()

        # title=response.xpath('//h1/text()').extract()[0]
        # content = ''.join(response.xpath('//div[@id="content"]/text()').extract())
        # next_url = response.xpath("//div[@class='page_chapter']/ul/li[3]/a/@href").extract_first()

        # content=''.join(response.xpath("//div[@id='content']/text()").extract())
        # next_url = response.xpath("//div[@class='bottem1']/a[3]/@href").extract_first()

        yield {
            'title':title,
            'content':content
        }
        # if next_url=="/book/16664/":
        # if next_url=='/27_27495/':
        if next_url=='/b_2q.htm':
            return
        # base_urls = 'https://www.zwdu.com{}'.format(next_url)
        print(12345)
        yield scrapy.Request(response.urljoin(next_url) ,callback=self.parse,dont_filter=True)



        # print(title,content)
        # with open('元尊2.txt','a',encoding='utf-8') as f:
        #     f.write(title[0]+'\n\n')
        #     f.write(content+'\n\n\n')