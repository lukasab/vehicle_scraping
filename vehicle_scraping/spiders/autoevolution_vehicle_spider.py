import scrapy
from scrapy.loader import ItemLoader
from vehicle_scraping.items import (
    VehicleBrandScrapingItem,
    VehicleModelScrapingItem,
    VehicleScrapingItem,
)


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


class AutoevolutionVehicleSpider(scrapy.Spider):
    name = "autoevolution"
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

            yield response.follow(vh_model_item["model_link"], self.parse_vehicle_model)

        discontinued_models = response.xpath("//div[@class='carmod clearfix disc']")
        for discontinued_model in discontinued_models:
            vh_model_item = get_vh_model_item(
                discontinued_model, False, brand_name, brand_link
            )
            yield vh_model_item

            yield response.follow(vh_model_item["model_link"], self.parse_vehicle_model)

    def parse_vehicle_model(self, response):
        model_link = response.url
        model_name = response.xpath(
            "//*[@id='newscol2']/div[1]/span/span[3]/a/span/text()"
        ).get()

        vehicles = response.xpath(
            "//div[@class='container carmodel clearfix' and @itemscope]"
        )
        for vehicle in vehicles:
            vh_loader = ItemLoader(item=VehicleScrapingItem(), selector=vehicle)
            vh_loader.add_value("model_name", model_name)
            vh_loader.add_value("model_link", model_link)
            vh_loader.add_xpath("vehicle_link", ".//a[@itemprop='url']/@href")
            vh_loader.add_xpath("vehicle_image_link", ".//img/@src")
            vehicle = vh_loader.load_item()

            yield response.follow(
                vehicle["vehicle_link"],
                self.parse_vehicle,
                cb_kwargs=dict(vehicle_item=vehicle),
            )

    def parse_vehicle(self, response, vehicle_item):
        vh_name = response.xpath("//h5[@class='motlisthead']/text()").get()
        vh_years = response.xpath("//h5[@class='motlisthead']/span[2]/text()").get()
        vh_segment = response.xpath(
            "//*[@id='pagewrapper']/div[1]/div[3]/div[1]/p/text()[2]"
        ).get()
        vh_description = " ".join(
            filter(
                None,
                [
                    response.xpath(
                        "//*[@id='pagewrapper']/div[1]/div[3]/div[2]/div/p/text()"
                    ).get()
                ],
            )
        )

        vh_data = response.xpath(
            "//div[@class='col23width fl bcol-white pdbot_60']/div[@class='padcol2']"
        )
        vh_loader = ItemLoader(vehicle_item, selector=vh_data)

        vh_loader.add_value("vehicle_name", vh_name)
        vh_loader.add_value("vehicle_year_from", vh_years)
        vh_loader.add_value("vehicle_year_to", vh_years)
        vh_loader.add_value("vehicle_description", vh_description)
        vh_loader.add_value("vehicle_segment", vh_segment)
        vh_loader.add_xpath(
            "vehicle_engine_type", "//dl[@title='Engine Specs']/dd[1]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_engine_displacement", "//dl[@title='Engine Specs']/dd[2]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_engine_bore_x_stroke", "//dl[@title='Engine Specs']/dd[3]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_engine_compression_ratio",
            "//dl[@title='Engine Specs']/dd[4]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_engine_horsepower", "//dl[@title='Engine Specs']/dd[5]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_engine_torque", "//dl[@title='Engine Specs']/dd[6]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_engine_fuel_system", "//dl[@title='Engine Specs']/dd[7]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_transmission_gearbox",
            "//dl[@title='Transmission Specs']/dd[1]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_transmission_clutch",
            "//dl[@title='Transmission Specs']/dd[2]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_transmission_primary_drive",
            "//dl[@title='Transmission Specs']/dd[3]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_transmission_final_drive",
            "//dl[@title='Transmission Specs']/dd[4]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_chassis_frame", "//dl[@title='Chassis Specs']/dd[1]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_chassis_front_suspension",
            "//dl[@title='Chassis Specs']/dd[2]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_chassis_rear_suspension",
            "//dl[@title='Chassis Specs']/dd[3]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_chassis_front_brake", "//dl[@title='Chassis Specs']/dd[4]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_chassis_rear_brake", "//dl[@title='Chassis Specs']/dd[5]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_dimension_overall_length",
            "//dl[@title='Dimension Specs']/dd[1]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_dimension_overall_width",
            "//dl[@title='Dimension Specs']/dd[2]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_dimension_seat_height",
            "//dl[@title='Dimension Specs']/dd[3]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_dimension_weelbase", "//dl[@title='Dimension Specs']/dd[4]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_dimension_ground_clearance",
            "//dl[@title='Dimension Specs']/dd[5]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_dimension_weight", "//dl[@title='Dimension Specs']/dd[6]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_dimension_fuel_capacity",
            "//dl[@title='Dimension Specs']/dd[7]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_tyres_front", "//dl[@title='Tyres Specs']/dd[1]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_tyres_rear", "//dl[@title='Tyres Specs']/dd[2]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_power_pack", "//dl[@title='Power System Specs']/dd[1]/text()"
        )
        vh_loader.add_xpath(
            "vehicle_power_nominal_capacity",
            "//dl[@title='Power System Specs']/dd[2]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_power_maximum_capacity",
            "//dl[@title='Power System Specs']/dd[3]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_power_charger_type",
            "//dl[@title='Power System Specs']/dd[4]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_power_charging_time_normal",
            "//dl[@title='Power System Specs']/dd[5]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_power_charging_quick",
            "//dl[@title='Power System Specs']/dd[6]/text()",
        )
        vh_loader.add_xpath(
            "vehicle_power_range", "//dl[@title='Power System Specs']/dd[7]/text()"
        )

        yield vh_loader.load_item()
