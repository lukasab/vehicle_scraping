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


def remove_new_line(value):
    return value.replace("\n", "")


def remove_tab(value):
    return value.replace("\t", "")


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


class DetailedVehicleScrapingItem(scrapy.Item):
    model_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
    )
    brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip), output_processor=TakeFirst()
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
    vehicle_description = scrapy.Field(
        input_processor=MapCompose(remove_new_line, remove_tab, str.strip),
        output_processor=TakeFirst(),
    )
    vehicle_identification_model_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=["Model Type"],
    )
    vehicle_identification_base_msrp = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=["BASE MSRP(US)"],
    )
    vehicle_identification_dealers = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=["Dealers"],
    )
    vehicle_identification_warranty = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=["Warranty"],
    )
    vehicle_identification_insurance = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_finance = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=["Engine Type"],
    )
    vehicle_engine_cylinders = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_stroke = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_horsepower_bhp_kW = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_horsepower_rpm = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_torque_ft = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_torque_rpm = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_cooling = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_valves = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_valves_per_cylinder = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_valves_per_configuration = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_bore = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_stroke = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_displacement = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_compression_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_starter = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_fuel_requirements = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_us_miles_per_gallon = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_can_liters_per_kilometer = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_fuel_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_turbocharged = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_supercharged = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_fuel_injector = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_carburetor = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_carburetion_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_number_of_speeds = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_overdrive = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_primary_drive_rear = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_primary_drive_engine = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_gear_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_reverse = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_brand = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_transmission_heel_toe_shifter = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_composition = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_tube_tubeless = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_chromed = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_front_wheel_width = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )

    vehicle_wheels_rear_wheel_width = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_front_tire_width = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_front_aspect_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_front_speed_rating = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_front_diameter = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_rear_tire_width = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_rear_aspect_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_rear_speed_rating = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_rear_diameter = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_front_spec = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wheels_rear_spec = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_brakes_front_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_brakes_rear_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_brakes_anti_lock = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_front_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_front_travel = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_front_central_strut = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_steering_damper = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_rear_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_rear_adjustable_shock = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_rear_adjustable_rebound_damping = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_number_rear_shock_absorbers = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_rear_suspension_material = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_suspension_air_adjustable = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_steering_control = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_length = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_width = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_height = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_wheelbase = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_ground_clearance = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_lenght_ft_ft = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_length_ft_in = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_dry_weight = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_wet_weight = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_fuel_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_technical_specs_engine_displacement_weight = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_adjustable = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_material = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_location = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_folding = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_height = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_number = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_detachable_passenger_seat = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seats_grab_rail_strap = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_frame = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_hand_grips = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_foot_peg_location = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_chain_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_drive_shaft_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_tank_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_belt_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_hand_guards = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_brush_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_heel_guards = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_light_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_side_cover = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_front_fender = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_rear_fender = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_top_crown = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_pocket = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_stand_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_handlebars = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_upper_fairing = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_license_plate = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_digital_instrumentation = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_clock = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_tachometer = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_trip_odometer = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_speedometer = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_fuel_level_warning_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_instrumentation_serive_reminder = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_pricing_warranty_condition = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_pricing_destination_charge = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_pricing_battery_warranty_months = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_generic_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_manufacturer_country = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_introduction_year = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_recommend_minimum_age = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_parent_company = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_identification_display_name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_mounts_side_case = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_mounts_windshield = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_paint_finish_paint = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_glass_folding = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_glass_windshield_lowers = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_glass_height_adjustable = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_glass_tinted = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_glass_height = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_side_case_material = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_number_side_cases = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_location = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_side_storage_mount = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_lockable = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_lights_headlight_mounts = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_lights_headlight = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_lights_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_convenience_engine_immobilizer_brand = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_convenience_keyless_ignition = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_convenience_power_outlet = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_convenience_cruise_control = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_convenience_handlebar_lock = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_warranty = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_basic_warranty = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_front_brake_diamater = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_brake_diamater = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_front_suspension_size = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_front_adjustable_fork_pre_load = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_front_adjustable_rebound_damping = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_travel = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_backrest_logo_plate = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_backrest_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_backrest_location = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_lumbar_adjustment = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_floor_board_location = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_saddle_bag_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exterior_covers = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_wind_deflector = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_metallic = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_tire_brand = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rearview_mirros = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_underseat_storage = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_rack_storage_material = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_rack_storage_trim = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_helmet_storage = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_halogen_headlight = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_immobilizer = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_final_drive_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_gvwr = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_carburetion_brand = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_number_carburetors = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_carburetor_size = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_suspension_size = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_engine_case_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_fork_guards = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_exhaust_guard = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_body_material = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_chassis_protectors = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_fuel_tank_cover = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_spoiler = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_decal_kit = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_temperature_warning = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_fuel_level_warning = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_maximum_range = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_fuel_capacity_reserve = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_brake_brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_suspension_brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_front_suspension_brand_name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_payload_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_performance = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_trip_computer = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_radiator_cover = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_heated_seat = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_horsepower_bhp = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_torque_ft = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_lower_fairing = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_speed_governor = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_top_crown = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_number_of_speakers = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_satellite = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_number_of_discs = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_fuel_injector = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_hard_side = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_rack = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_helmet_locks = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_fog_lights = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_us_miles = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_passing_lamps = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_linked_brake = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_heated_hand = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_adjustable_levers = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_capacities = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_temperature_warning_type = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_skid_plate = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_multi_lingual = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_country = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_glove_box = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_us_miles = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_can_liters = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_photo_gallery = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_rear_rack_storage = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_handlebar_pads = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_adjustable_throttle = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_turning_radius = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_storage_capacity = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_radio = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_cb_intercom = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_headset = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_cassette_player = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_adjustable_headlights = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seat_rail = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_shift_light = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_seat_tail_cover = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )
    vehicle_adjustable_handlebars = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst(),
        name_on_site=[""],
    )


DETAILED_FIELDS_NAMES = {
    "vehicle_identification_model_type": ["Model Type"],
    "vehicle_identification_base_msrp": ["BASE MSRP(US)"],
    "vehicle_identification_dealers": ["Dealers"],
    "vehicle_identification_warranty": ["Warranty"],
    "vehicle_identification_insurance": ["Insurance"],
    "vehicle_identification_finance": ["Finance"],
    "vehicle_engine_brand_name": ["Engine Brand Name"],
    "vehicle_engine_type": ["Engine Type"],
    "vehicle_engine_cylinders": ["Cylinders"],
    "vehicle_engine_stroke": ["Engine Stroke"],
    "vehicle_engine_torque_ft": ["Torque (Ft Lbs/Nm)", "Torque (Ft Lbs)"],
    "vehicle_engine_torque_rpm": ["Torque RPM"],
    "vehicle_engine_cooling": ["Cooling"],
    "vehicle_engine_valves": ["Valves"],
    "vehicle_engine_valves_per_cylinder": ["Valves Per Cylinder"],
    "vehicle_engine_valves_per_configuration": ["Valve Configuration"],
    "vehicle_engine_bore": ["Bore (mm/in)"],
    "vehicle_stroke": ["Stroke (mm/in)"],
    "vehicle_engine_displacement": ["Displacement (cc/ci)"],
    "vehicle_engine_compression_ratio": ["Compression Ratio"],
    "vehicle_engine_starter": ["Starter"],
    "vehicle_engine_fuel_requirements": ["Fuel Requirements"],
    "vehicle_engine_us_miles_per_gallon": ["US Miles Per Gallon (Combined)"],
    "vehicle_engine_can_liters_per_kilometer": ["CAN Liters Per Kilometer (Combined)"],
    "vehicle_engine_fuel_type": ["Fuel Type"],
    "vehicle_engine_turbocharged": ["Turbocharged"],
    "vehicle_engine_supercharged": ["Supercharged"],
    "vehicle_engine_fuel_injector": ["Fuel Injector"],
    "vehicle_engine_carburetor": ["Carburetor"],
    "vehicle_engine_carburetion_type": ["Carburetion Type"],
    "vehicle_transmission_type": ["Transmission Type"],
    "vehicle_transmission_number_of_speeds": ["Number Of Speeds"],
    "vehicle_transmission_overdrive": ["Overdrive"],
    "vehicle_transmission_primary_drive_rear": ["Primary Drive (Rear Wheel)"],
    "vehicle_transmission_primary_drive_engine": [
        "Primary Drive (Engine / Transmission)"
    ],
    "vehicle_transmission_gear_ratio": [
        "Gear Ratio (1/2/3/4/5/6)",
        "Gear Ratio (1/2/3/4/5)",
        "Gear Ratio (1/2/3/4)",
    ],
    "vehicle_transmission_reverse": ["Reverse"],
    "vehicle_transmission_brand": ["Transmission Brand"],
    "vehicle_transmission_heel_toe_shifter": ["Heel Toe Shifter"],
    "vehicle_wheels_composition": ["Wheels Composition"],
    "vehicle_wheels_chromed": ["Chromed"],
    "vehicle_wheels_front_tire_width": ["Front Tire Width"],
    "vehicle_wheels_front_aspect_ratio": ["Front Tire Aspect Ratio"],
    "vehicle_wheels_front_speed_rating": ["Front Tire Speed Rating"],
    "vehicle_wheels_front_diameter": ["Front Wheel Diameter"],
    "vehicle_wheels_rear_tire_width": ["Rear Tire Width"],
    "vehicle_wheels_rear_aspect_ratio": ["Rear Tire Aspect Ratio"],
    "vehicle_wheels_rear_speed_rating": ["Rear Tire Speed Rating"],
    "vehicle_wheels_rear_diameter": ["Rear Wheel Diameter"],
    "vehicle_wheels_front_spec": ["Front Tire (Full Spec)"],
    "vehicle_wheels_rear_spec": ["Rear Tire (Full Spec)"],
    "vehicle_brakes_front_type": ["Front Brake Type"],
    "vehicle_brakes_rear_type": ["Rear Brake Type"],
    "vehicle_brakes_anti_lock": ["Anti-Lock Brakes"],
    "vehicle_suspension_front_type": ["Front Suspension Type"],
    "vehicle_suspension_front_travel": ["Front Travel (in/mm)"],
    "vehicle_suspension_front_central_strut": ["Front Central Suspension Strut"],
    "vehicle_suspension_steering_damper": ["Steering Damper"],
    "vehicle_suspension_rear_type": ["Rear Suspension Type"],
    "vehicle_suspension_rear_adjustable_shock": [
        "Rear Adjustable Shock / Spring Pre-Load"
    ],
    "vehicle_suspension_rear_adjustable_rebound_damping": [
        "Rear Adjustable Rebound Damping"
    ],
    "vehicle_suspension_number_rear_shock_absorbers": ["Number Rear Shock Absorbers"],
    "vehicle_suspension_rear_suspension_material": ["Rear Suspension Material"],
    "vehicle_suspension_air_adjustable": ["Air Adjustable"],
    "vehicle_steering_control": ["Steering Control"],
    "vehicle_technical_specs_length": ["Length (ft)"],
    "vehicle_technical_specs_width": ["Width (in/mm)"],
    "vehicle_technical_specs_height": ["Height (in/mm)"],
    "vehicle_technical_specs_wheelbase": ["Wheelbase (in/mm)"],
    "vehicle_technical_specs_ground_clearance": ["Ground Clearance (in/mm)"],
    "vehicle_technical_specs_lenght_ft_ft": ["Length (ft/ft)"],
    "vehicle_technical_specs_length_ft_in": ["Length (ft/in)"],
    "vehicle_technical_specs_dry_weight": ["Dry Weight (lbs/kg)"],
    "vehicle_technical_specs_wet_weight": ["Wet Weight (lbs/kg)"],
    "vehicle_technical_specs_fuel_capacity": ["Fuel Capacity (gal/l)"],
    "vehicle_technical_specs_engine_displacement_weight": [
        "Engine Displacement to Weight (cc)"
    ],
    "vehicle_seats_type": ["Seat Type"],
    "vehicle_seats_adjustable": ["Adjustable"],
    "vehicle_seats_material": ["Seat Material"],
    "vehicle_seats_location": ["Seat Location"],
    "vehicle_seats_folding": ["Folding"],
    "vehicle_seats_height": ["Seat Height (in/mm)"],
    "vehicle_seats_number": ["Number Of Seats"],
    "vehicle_seats_detachable_passenger_seat": ["Detachable Passenger Seat"],
    "vehicle_seats_grab_rail_strap": ["Grab Rail or Strap"],
    "vehicle_exterior_frame": ["Frame"],
    "vehicle_exterior_hand_grips": ["Hand Grips"],
    "vehicle_exterior_foot_peg_location": ["Foot Peg Location"],
    "vehicle_exterior_chain_guard": ["Chain Guard"],
    "vehicle_exterior_drive_shaft_guard": ["Drive Shaft Guard"],
    "vehicle_exterior_tank_guard": ["Tank Guard"],
    "vehicle_exterior_belt_guard": ["Belt Guard"],
    "vehicle_exterior_hand_guards": ["Hand Guards"],
    "vehicle_exterior_brush_guard": ["Brush Guard"],
    "vehicle_exterior_heel_guards": ["Heel Guards"],
    "vehicle_exterior_light_guard": ["Light Guard"],
    "vehicle_exterior_side_cover": ["Side Cover"],
    "vehicle_exterior_front_fender": ["Front Fender"],
    "vehicle_exterior_rear_fender": ["Rear Fender"],
    "vehicle_exterior_top_crown": ["Top Crown"],
    "vehicle_exterior_pocket": ["Pocket"],
    "vehicle_exterior_stand_type": ["Stand Type"],
    "vehicle_exterior_handlebars": ["Handlebars"],
    "vehicle_exterior_upper_fairing": ["Upper Fairing"],
    "vehicle_exterior_license_plate": ["License Plate"],
    "vehicle_instrumentation_digital_instrumentation": ["Digital Instrumentation"],
    "vehicle_instrumentation_clock": ["Clock"],
    "vehicle_instrumentation_tachometer": ["Tachometer"],
    "vehicle_instrumentation_trip_odometer": ["Trip Odometer"],
    "vehicle_instrumentation_speedometer": ["Speedometer"],
    "vehicle_instrumentation_fuel_level_warning_type": ["Fuel Level Warning Type"],
    "vehicle_instrumentation_serive_reminder": ["Service Reminder"],
    "vehicle_pricing_warranty_condition": ["Warranty (Condition)"],
    "vehicle_pricing_destination_charge": ["Destination Charge"],
    "vehicle_pricing_battery_warranty_months": ["Battery", "Battery Warranty (Months)"],
    "vehicle_identification_generic_type": ["Generic Type (Primary)"],
    "vehicle_identification_manufacturer_country": ["Manufacturer Country"],
    "vehicle_identification_introduction_year": ["Introduction Year"],
    "vehicle_identification_recommend_minimum_age": [
        "Manufacturer Recommend Minimum Age"
    ],
    "vehicle_identification_parent_company": ["Parent Company"],
    "vehicle_identification_display_name": ["Display Name"],
    "vehicle_mounts_side_case": ["Side Case Mount"],
    "vehicle_mounts_windshield": ["Windshield Mounts"],
    "vehicle_paint_finish_paint": ["Paint"],
    "vehicle_glass_folding": ["Folding"],
    "vehicle_glass_windshield_lowers": ["Windshield Lowers"],
    "vehicle_glass_height_adjustable": ["Height Adjustable"],
    "vehicle_glass_tinted": ["Tinted"],
    "vehicle_glass_height": ["Height"],
    "vehicle_storage_side_case_material": ["Side Case Material"],
    "vehicle_storage_number_side_cases": ["Number Of Side Cases"],
    "vehicle_storage_location": ["Location"],
    "vehicle_storage_side_storage_mount": ["Side Storage Mount"],
    "vehicle_storage_lockable": ["Lockable Storage"],
    "vehicle_lights_headlight_mounts": ["Headlight Mounts"],
    "vehicle_lights_headlight": ["Headlight (s)"],
    "vehicle_lights_type": ["Type"],
    "vehicle_convenience_engine_immobilizer_brand": ["Engine Immobilizer Brand"],
    "vehicle_convenience_keyless_ignition": ["Keyless Ignition"],
    "vehicle_convenience_power_outlet": ["Power Outlet"],
    "vehicle_convenience_cruise_control": ["Cruise Control"],
    "vehicle_convenience_handlebar_lock": ["Handlebar Lock"],
    "vehicle_wheels_front_wheel_width": ["Front Wheel Width (in)"],
    "vehicle_wheels_rear_wheel_width": ["Rear Wheel Width (in)"],
    "vehicle_engine_horsepower_bhp_kW": [
        "Horsepower (bhp/kW)",
        "Horsepower (bhp)",
        "Horsepower (kW)",
    ],
    "vehicle_engine_horsepower_rpm": ["Horsepower RPM"],
    "vehicle_wheels_tube_tubeless": ["Tube / Tubeless"],
    "vehicle_warranty": ["Warranty (Months/Condition)", "Warranty (Months)"],
    "vehicle_basic_warranty": ["Basic Warranty (Miles)"],
    "vehicle_front_brake_diamater": ["Front Brake Diameter (in/mm)"],
    "vehicle_rear_brake_diamater": ["Rear Brake Diameter (in/mm)"],
    "vehicle_front_suspension_size": ["Front Suspension Size (in/mm)"],
    "vehicle_front_adjustable_fork_pre_load": ["Front Adjustable Fork Pre-Load"],
    "vehicle_front_adjustable_rebound_damping": ["Front Adjustable Rebound Damping"],
    "vehicle_rear_travel": ["Rear Travel (in/mm)"],
    "vehicle_backrest_logo_plate": ["Backrest Logo Plate"],
    "vehicle_backrest_type": ["Backrest Type"],
    "vehicle_backrest_location": ["Backrest Location"],
    "vehicle_lumbar_adjustment": ["Lumbar Adjustment"],
    "vehicle_floor_board_location": ["Floor Board Location"],
    "vehicle_saddle_bag_guard": ["Saddle Bag Guard"],
    "vehicle_exterior_covers": ["Exterior Covers"],
    "vehicle_wind_deflector": ["Wind Deflector"],
    "vehicle_metallic": ["Metallic"],
    "vehicle_tire_brand": ["Tire Brand"],
    "vehicle_rearview_mirros": ["Rearview Mirrors"],
    "vehicle_underseat_storage": ["Underseat Storage"],
    "vehicle_rear_rack_storage_material": ["Rear Rack Storage Material"],
    "vehicle_rear_rack_storage_trim": ["Rear Rack Storage Trim"],
    "vehicle_helmet_storage": ["Helmet Storage"],
    "vehicle_halogen_headlight": ["Halogen Headlight (s)"],
    "vehicle_engine_immobilizer": ["Engine Immobilizer"],
    "vehicle_final_drive_ratio": ["Final Drive Ratio"],
    "vehicle_gvwr": ["GVWR (lbs/kgs)"],
    "vehicle_carburetion_brand": ["Carburetion Brand"],
    "vehicle_number_carburetors": ["Number Of Carburetors"],
    "vehicle_carburetor_size": ["Carburetor Size (mm)"],
    "vehicle_rear_suspension_size": ["Rear Suspension Size (in/mm)"],
    "vehicle_engine_case_guard": ["Engine Case Guard"],
    "vehicle_fork_guards": ["Fork Guards"],
    "vehicle_exhaust_guard": ["Exhaust Guard"],
    "vehicle_body_material": ["Body Material"],
    "vehicle_chassis_protectors": ["Chassis Protectors"],
    "vehicle_fuel_tank_cover": ["Fuel Tank Cover"],
    "vehicle_spoiler": ["Spoiler"],
    "vehicle_decal_kit": ["Decal Kit"],
    "vehicle_temperature_warning": ["Temperature Warning"],
    "vehicle_fuel_level_warning": ["Fuel Level Warning"],
    "vehicle_maximum_range": ["Maximum Range (mi/km)"],
    "vehicle_fuel_capacity_reserve": ["Fuel Capacity Reserve (gal/l)"],
    "vehicle_brake_brand_name": ["Brake Brand Name"],
    "vehicle_rear_suspension_brand_name": ["Rear Suspension Brand Name"],
    "vehicle_front_suspension_brand_name": ["Front Suspension Brand Name"],
    "vehicle_payload_capacity": ["Payload Capacity (lbs/kgs)"],
    "vehicle_performance": ["Performance"],
    "vehicle_trip_computer": ["Trip Computer"],
    "vehicle_radiator_cover": ["Radiator Cover"],
    "vehicle_heated_seat": ["Heated Seat"],
    "vehicle_horsepower_bhp": ["Horsepower (bhp)"],
    "vehicle_torque_ft": ["Torque (Ft Lbs)"],
    "vehicle_lower_fairing": ["Lower Fairing"],
    "vehicle_speed_governor": ["Speed Governor"],
    "vehicle_top_crown": ["Top Crown Material"],
    "vehicle_number_of_speakers": ["Number Of Speakers"],
    "vehicle_satellite": ["Satellite"],
    "vehicle_number_of_discs": ["Number Of Discs"],
    "vehicle_fuel_injector": ["Fuel Injector Size (mm)"],
    "vehicle_hard_side": ["Hard Side Case Capacity (gal/l)"],
    "vehicle_rear_rack": ["Rear Rack"],
    "vehicle_helmet_locks": ["Helmet Locks"],
    "vehicle_fog_lights": ["Fog Lights"],
    "vehicle_us_miles": ["US Miles Per Gallon (Hwy)"],
    "vehicle_passing_lamps": ["Passing Lamps"],
    "vehicle_linked_brake": ["Linked Brake System Front to Rear"],
    "vehicle_heated_hand": ["Heated Hand Grip Location"],
    "vehicle_adjustable_levers": ["Adjustable Levers"],
    "vehicle_storage_capacity": ["Storage Capacity (cuft/gal/l)"],
    "vehicle_capacities": ["Capacities"],
    "vehicle_temperature_warning_type": ["Temperature Warning Type"],
    "vehicle_skid_plate": ["Skid Plate"],
    "vehicle_multi_lingual-": ["Multi-Lingual Instrumentation"],
    "vehicle_country": ["Country"],
    "vehicle_glove_box": ["Glove Box / Dash Storage"],
    "vehicle_us_miles": ["US Miles Per Gallon (Hwy/City)"],
    "vehicle_can_liters": ["CAN Liters Per Kilometer (Hwy/City)"],
    "vehicle_photo_gallery": ["Photo Gallery"],
    "vehicle_rear_rack_storage": ["Rear Rack Storage"],
    "vehicle_handlebar_pads": ["Handlebar Pads"],
    "vehicle_adjustable_throttle": ["Adjustable Throttle"],
    "vehicle_turning_radius": ["Turning Radius (ft)"],
    "vehicle_storage_capacity": ["Storage Capacity (cuft)"],
    "vehicle_radio": ["Radio"],
    "vehicle_cb_intercom": ["CB Intercom"],
    "vehicle_headset": ["Headset"],
    "vehicle_cassette_player": ["Cassette Player"],
    "vehicle_adjustable_headlights": ["Adjustable Headlights"],
    "vehicle_seat_rail": ["Seat Rail"],
    "vehicle_shift_light": ["Shift Light Type"],
    "vehicle_seat_tail_cover": ["Seat Tail Cover"],
    "vehicle_adjustable_handlebars": ["Adjustable Handlebars"],
}
