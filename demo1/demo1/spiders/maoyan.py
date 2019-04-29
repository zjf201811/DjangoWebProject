import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?']

    def parse(self, response):
        names = response.xpath("//div[@class='channel-detail movie-item-title']/@title").extract()
        score_div = response.xpath("//div[@class='channel-detail channel-detail-orange']")

        scores = []
        for score in score_div:
            scores.append(score.xpath('string(.)').extract_first())

        for name, score in zip(names, scores):
            print(name, ":", score)
            yield {'name':name,'score':score}
