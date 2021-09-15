import scrapy
from scrapy.loader import ItemLoader
from vehicle_scraping.items import VehicleBrandScrapingItem, VehicleModelScrapingItem


def get_vh_model_item(selector, in_production, brand_name, brand_link):
    vh_model = ItemLoader(item=VehicleModelScrapingItem(), selector=selector)
    vh_model.add_value("brand_name", brand_name)
    vh_model.add_value("brand_link", brand_link)
    vh_model.add_xpath("model_name", ".//h4/text()")
    vh_model.add_xpath("model_link", ".//a/@href")
    vh_model.add_xpath("model_image_link", ".//img/@src")
    vh_model.add_value("model_in_production", in_production)
    vh_model.add_xpath("model_generations", ".//div[@class='col3width fl']/p/b/text()")
    vh_model.add_xpath("model_year_from", ".//div[@class='col3width fl']/span/text()")
    vh_model.add_xpath("model_year_to", ".//div[@class='col3width fl']/span/text()")
    return vh_model.load_item()


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
        brand_name = response.xpath("//*[@id='newscol2']/h1/a/b/text()").get()
        brand_link = response.url
        production_models = response.xpath("//div[@class='carmod clearfix ']")
        for production_model in production_models:
            vh_model_item = get_vh_model_item(
                production_model, True, brand_name, brand_link
            )
            yield vh_model_item

        discontinued_models = response.xpath("//div[@class='carmod clearfix disc']")
        for discontinued_model in discontinued_models:
            vh_model_item = get_vh_model_item(
                discontinued_model, False, brand_name, brand_link
            )
            yield vh_model_item
