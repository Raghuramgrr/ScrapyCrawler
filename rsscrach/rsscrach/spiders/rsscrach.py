import scrapy
import pyquery
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pyquery import PyQuery


class rsscarch(CrawlSpider):

    name = 'spiders'

    start_urls = ['http://www.rsscarch.com/project/peters-township-library/']
    rules = [
    Rule(LinkExtractor(allow=['/project/*']),callback='parse',follow=True)
    ]

#--------------------------------------------------------------------------------------------------------

    def parse(self, response):
       
        print('----------------pyquery ------------')
        p = pyquery.PyQuery(response.body)
        for title in p('h2'):
            #print('>>>',title, '<<<')
            txt =p('p').text()
        label = re.findall(r'[A-Za-z]*:',txt)
        label = [x.replace(':','') for x in label ]
        value = [val for val in re.split(r'[A-Za-z]*:',txt) if val is not '']
        description=re.findall(r'\SF(.*)',txt)
        #print(description)
        value[2] = value[2].split()[0]
        #print(value)
        scrapped_info={
        'title':value[0],
        'locaion':value[1],
        'size':value[2],
        'description': description
        }
        print('>>>Title     :',value[0])
        print('>>>Location  :',value[1])
        print('>>>Size      :',value[2])
        print('>>>Description:',description)
        
        
        yield scrapped_info

        

       
# ---------------------------------------------------------------------


