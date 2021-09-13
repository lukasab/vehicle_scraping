# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def tranform_int(value):
    return int(value) if value.isnumeric() else None


class VehicleBrandScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    brand_name = scrapy.Field(
        input_processor=MapCompose(str.lstrip), output_processor=TakeFirst()
    )
    brand_link = scrapy.Field(
        input_processor=MapCompose(str.lstrip), output_processor=TakeFirst()
    )
    brand_image_link = scrapy.Field(
        input_processor=MapCompose(str.lstrip), output_processor=TakeFirst()
    )
    brand_vehicle_in_production = scrapy.Field(
        input_processor=MapCompose(tranform_int), output_processor=TakeFirst()
    )
    brand_vehicle_discontinued = scrapy.Field(
        input_processor=MapCompose(tranform_int), output_processor=TakeFirst()
    )
