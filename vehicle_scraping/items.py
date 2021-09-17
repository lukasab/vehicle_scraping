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
    splitted_values = value.split("-")
    if len(splitted_values) > 1:
        return splitted_values[1]
    return None


def space_url(value):
    return value.replace(" ", "%20")


def replace_empty(value):
    if len(value) == 1 and value == "-":
        return None
    return value


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


class VehicleScrapingItem(scrapy.Item):
    model_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    model_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    vehicle_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    vehicle_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    vehicle_image_link = scrapy.Field(
        input_processor=MapCompose(str.strip, space_url), output_processor=TakeFirst()
    )
    vehicle_year_from = scrapy.Field(
        input_processor=MapCompose(get_first_year, str.strip),
        output_processor=TakeFirst(),
    )
    vehicle_year_to = scrapy.Field(
        input_processor=MapCompose(get_first_year, str.strip),
        output_processor=TakeFirst(),
    )
    vehicle_year_to = scrapy.Field(
        input_processor=MapCompose(get_last_year, str.strip),
        output_processor=TakeFirst(),
    )
    vehicle_description = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    vehicle_segment = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    vehicle_engine_type = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_engine_displacement = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_engine_bore_x_stroke = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_engine_compression_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_engine_horsepower = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_engine_torque = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_engine_fuel_system = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_transmission_gearbox = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_transmission_clutch = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_transmission_primary_drive = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_transmission_final_drive = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_chassis_frame = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_chassis_front_suspension = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_chassis_rear_suspension = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_chassis_front_brake = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_chassis_rear_brake = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_overall_length = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_overall_width = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_seat_height = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_weelbase = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_ground_clearance = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_weight = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_dimension_fuel_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_tyres_front = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_tyres_rear = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_pack = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_nominal_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_maximum_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_charger_type = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_charging_time_normal = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_charging_quick = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
    vehicle_power_range = scrapy.Field(
        input_processor=MapCompose(str.strip, replace_empty),
        output_processor=TakeFirst(),
    )
