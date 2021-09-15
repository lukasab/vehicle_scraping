# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def tranform_int(value):
    return int(value) if value.isnumeric() else None


def get_first_year(value):
    return value.split("-")[0]


def get_last_year(value):
    return value.split("-")[1]


def space_url(value):
    return value.replace(" ", "%20")


class VehicleBrandScrapingItem(scrapy.Item):
    brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    brand_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    brand_image_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    brand_vehicle_in_production = scrapy.Field(
        input_processor=MapCompose(tranform_int), output_processor=TakeFirst()
    )
    brand_vehicle_discontinued = scrapy.Field(
        input_processor=MapCompose(tranform_int), output_processor=TakeFirst()
    )


class VehicleModelScrapingItem(scrapy.Item):
    brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    brand_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    model_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    model_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    model_image_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    model_in_production = scrapy.Field(output_processor=TakeFirst())
    model_generations = scrapy.Field(
        input_processor=MapCompose(tranform_int), output_processor=TakeFirst()
    )
    model_year_from = scrapy.Field(
        input_processor=MapCompose(get_first_year, str.strip),
        output_processor=TakeFirst(),
    )
    model_year_to = scrapy.Field(
        input_processor=MapCompose(get_last_year, str.strip),
        output_processor=TakeFirst(),
    )
