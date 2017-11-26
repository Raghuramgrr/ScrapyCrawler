import scrapy
import pyquery
import re

class rsscarch(scrapy.Spider):

    name = 'spiders'

    start_urls = ['http://www.rsscarch.com/project/peters-township-library/']



    def parse(self, response):
        print('--- pyquery 1 ---')
        p = pyquery.PyQuery(response.body)
        for title in p('h2 '):
            print('>>>', title, title.text, '<<<') # `title.text` gives "\n"

        print('--- pyquery 2 ---')
        p = pyquery.PyQuery(response.body)
        for title in p('h2'):
            print('>>>',title, '<<<')
        #print(p('h2').text())
        #print(p('p').text())
        txt =p('p').text()
        print(txt.split(':'))
        #print(txt.index("client:"))
        #print(txt.split(' ', 5))
        #d = dict(txt.split(':') for s in a)
        #print(d)

        #print(txt.split())

       # print('--- pyquery 3 ---')
        #p = pyquery.PyQuery(response.body).text
        #for title in p('h2 a'):
         #   print('>>>', title, title.text())

# ---------------------------------------------------------------------

from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(rsscarch)
process.start(stop_after_crawl=False)
