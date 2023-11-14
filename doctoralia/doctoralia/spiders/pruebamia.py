from pathlib import Path
import re
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "doctoralia"

    def start_requests(self):
        urls = [
           "https://www.doctoralia.com.mx/buscar?q=Nutricionista&loc=&filters%5Bspecializations%5D%5B0%5D=60&page=285"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        salida=response.css("h3.h4").css("span::text").extract()
        for sal in salida:
            print(sal.lstrip().rstrip())
            #limp = re.sub(r'[\t\n]', '', sal)
            #if (limp[0]==("\s")):
            #    limp = limp.replace(cadena[0], "", 1)
            #print(limp)