import scrapy
from scrapy.loader import ItemLoader
from vehicle_scraping.items import (
    VehicleBrandScrapingItem,
    DetailedVehicleScrapingItem,
    DETAILED_FIELDS_NAMES,
)


class MotorcycleVehicleSpider(scrapy.Spider):
    name = "motorcycle"
    start_urls = ["https://www.motorcycle.com/specs/"]
    detailed_fields = DetailedVehicleScrapingItem.fields

    def parse(self, response):
        brands = response.xpath("//span[@class='text manufacturer_list']/ul/li")
        for brand in brands:
            vh_brand = ItemLoader(item=VehicleBrandScrapingItem(), selector=brand)
            vh_brand.add_xpath("brand_name", "./a/text()")
            vh_brand.add_xpath("brand_link", "./a/@href")
            vh_brand_item = vh_brand.load_item()
            yield vh_brand_item

            yield response.follow(
                vh_brand_item["brand_link"], callback=self.parse_brand_years
            )

    def parse_brand_years(self, response):
        years = response.xpath(
            "//div[@class='text_wrapper subnavigation year_menu']/div/ul/li/a"
        )
        yield from response.follow_all(years, callback=self.parse_brand_vehicles)

    def parse_brand_vehicles(self, response):
        vehicle_links = response.xpath("//table[@class='table_info']//td/a")
        for vehicle_link in vehicle_links:
            # instead of going to the site and getting the detail link we just append
            detailed_link = vehicle_link.attrib["href"].replace(".html", "/detail.html")
            yield response.follow(detailed_link, callback=self.parse_vehicle)

    def get_item_field_name(self, key_name):
        for field in DETAILED_FIELDS_NAMES:
            if key_name.strip() in DETAILED_FIELDS_NAMES.get(field):
                return field
        else:
            print("The following key name was not found {}!".format(key_name))
        return None

    def parse_vehicle(self, response):
        trs = response.xpath(
            "//table[@class='table_info']//tr[@class='alt1' or @class='alt2']"
        )
        detailed_vh_loader = ItemLoader(
            item=DetailedVehicleScrapingItem(), response=response
        )
        detailed_vh_loader.add_xpath(
            "brand_name", "//*[@id='main-content']/div/div[2]/a[3]/text()"
        )
        detailed_vh_loader.add_xpath(
            "model_name", "//*[@id='main-content']/div/div[2]/a[4]/text()"
        )
        detailed_vh_loader.add_xpath(
            "vehicle_name", " //*[@id='main-content']/div/div[2]/a[5]/text()"
        )
        detailed_vh_loader.add_value("vehicle_link", response.url)
        detailed_vh_loader.add_xpath(
            "vehicle_image_link", "//span[@class='picture']/img/@src"
        )
        detailed_vh_loader.add_xpath(
            "vehicle_year_from", "//*[@id='main-content']/div/div[2]/a[2]/text()"
        )
        detailed_vh_loader.add_xpath(
            "vehicle_description", "//span[@class='text desciption_text']/text()"
        )
        for tr in trs:
            key = tr.xpath("./td[1]/text()").get()
            value = tr.xpath("./td[2]/text()").get()
            field_name = self.get_item_field_name(key)
            if field_name:
                detailed_vh_loader.add_value(field_name, value)
        yield detailed_vh_loader.load_item()
