import scrapy


class VehicleSpider(scrapy.Spider):
    name = "vehicle"
    start_urls = ["https://www.autoevolution.com/moto/"]

    def parse(self, response):
        brands = response.xpath("//div[@itemscope]")
        for brand in brands:
            yield {
                "brand_name": brand.xpath("a/@title").get(),
                "brand_link": brand.xpath("a/@href").get(),
                "brand_image_link": brand.xpath("a/img/@src").get(),
                "brand_vehicle_in_production": brand.xpath(
                    "following-sibling::div[1]/p[1]/b/text()"
                ).get(),
                "brand_vehicle_discontinued": brand.xpath(
                    "following-sibling::div[1]/p[2]/b/text()"
                ).get(),
            }

    def parse_brand(self, response):
        pass
