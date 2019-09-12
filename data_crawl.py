import scrapy
from ..items import DjlxItem



class DjlxSpider(scrapy.Spider):
    #爬虫名称
    name = 'djlx'
    #允许爬取的域名
    allowed_domains = ['lianjia.com']
    #爬虫入口爬取地址
    start_urls = ['https://wh.lianjia.com/ershoufang/']
    #爬虫爬取页数控制初始值
    count = 1
    #爬虫爬取页数 10为只爬取一页
    page_end = 10

    def parse(self, response):

        nodeList = response.xpath(
            "//*[@id='s_position_list']/ul/li")
        for node in nodeList:
            item = DjlxItem()

            item['title'] = node.xpath("div[1]/div[1]/div[1]/a/h3/text()").extract()[0]
            item['company'] = node.xpath("div[1]/div[2]/div[1]/a/text()").extract()[0]
            item['salary'] = node.xpath("div[1]/div[1]/div[2]/div/span/text()").extract()[0]
            item['welfare'] = node.xpath("div[2]/div[2]/text()").extract()[0]
            item['indurstry'] = node.xpath("div[1]/div[2]/div[2]/text()").extract()[0]
            # item['num'] = node.xpath("./td[3]/text()").extract()[0]
            item['address'] = node.xpath("div[1]/div[1]/div[1]/a/span/em/text()").extract()[0]
            item['time'] = node.xpath("div[1]/div[1]/div[1]/span/text()").extract()[0]
            # 根据内页地址爬取
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.detail_parse)

            # 有下级页面爬取 注释掉数据返回
            # yield item

        # 循环爬取翻页
        nextPage = response.xpath("//*[@id='s_position_list']/div[2]/div/a[6]/@href").extract()[0]
        # 爬取页数控制及末页控制
        if self.count < self.page_end and nextPage != 'javascript:;':
            if nextPage is not None:
                # 爬取页数控制值自增
                self.count = self.count + 1
                # 翻页请求
                yield scrapy.Request(self.base_url + nextPage, callback=self.parse)
        else:
            # 爬虫结束
            return None
    def detail_parse(self,response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        # 一级内页数据提取
        item['zhize'] = \
            response.xpath("//*[@id='job_detail']/dd[2]/div/ul[1]").xpath('string(.)').extract()[0]
        item['yaoqiu'] = \
            response.xpath("//*[@id='job_detail']/dd[2]/div/ul[2]").xpath('string(.)').extract()[0]
        # 二级内页地址爬取
        yield scrapy.Request(item['url'] + "&123", meta={'item': item}, callback=self.detail_parse2)
        # 有下级页面爬取 注释掉数据返回
        # return item
    def detail_parse2(self,response):
        # 接收上级已爬取的数据
        item = response.meta['item']
        # 二级内页数据提取
        item['test'] = "111111111111111111"
        # 最终返回数据给爬虫引擎
        return item
