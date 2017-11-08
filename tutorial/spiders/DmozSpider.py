from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class DmozSpider(BaseSpider):
   name = "dmoz"
   allowed_domains = ["blog.csdn.net"]
   start_urls = [
       "http://blog.csdn.net/qq_31518899"
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.path('//fieldset/ul/li')
       #sites = hxs.path('//ul/li')
       items = []
       for site in sites:
           item = DmozItem()
           item['title'] = site.path('a/text()').extract()
           item['link'] = site.path('a/@href').extract()
           item['desc'] = site.path('text()').extract()
           items.append(item)
       return items