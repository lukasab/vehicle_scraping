import scrapy


class MotorcycleVehicleSpider(scrapy.Spider):
    name = "motorcycle"
    start_urls = ["http://https://www.motorcycle.com/specs/"]

    def parse(self, response):
        pass
