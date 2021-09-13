import scrapy
from scrapy.loader import ItemLoader
from vehicle_scraping.items import VehicleBrandScrapingItem


class VehicleSpider(scrapy.Spider):
    name = "vehicle"
    start_urls = ["https://www.autoevolution.com/moto/"]

    def parse(self, response):
        brands = response.xpath("//div[@itemscope]")
        for brand in brands:
            vh_brand = ItemLoader(item=VehicleBrandScrapingItem(), selector=brand)
            vh_brand.add_xpath("brand_name", "a/@title")
            vh_brand.add_xpath("brand_link", "a/@href")
            vh_brand.add_xpath("brand_image_link", "a/img/@src")
            vh_brand.add_xpath(
                "brand_vehicle_in_production", "following-sibling::div[1]/p[1]/b/text()"
            )
            vh_brand.add_xpath(
                "brand_vehicle_discontinued", "following-sibling::div[1]/p[2]/b/text()"
            )
            vh_brand_item = vh_brand.load_item()
            yield vh_brand_item

            yield response.follow(vh_brand_item["brand_link"], self.parse_brand_models)

    def parse_brand_models(self, response):
        production_models = response.xpath("//div[@class='carmod clearfix ']")
        for production_model in production_models:
            yield {"production_model_link": production_model.xpath(".//a/@href").get()}
        discontinued_models = response.xpath("//div[@class='carmod clearfix disc']")
        for discontinued_model in discontinued_models:
            yield {
                "discontinued_model_link": discontinued_model.xpath(".//a/@href").get()
            }
