# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from datetime import datetime
from scrapy.exporters import CsvItemExporter
from vehicle_scraping import items


def item_type(item):
    return type(item).__name__


class MultiCSVItemPipeline(object):
    defined_items = [name for name, _ in items.__dict__.items() if "Item" in name]
    time_str = datetime.now().strftime("_%Y-%m-%d_%H_%M_%S")

    def open_spider(self, spider):
        self.files = dict()
        self.exporters = dict()

    def close_spider(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

    def create_exporter(self, item_name, spider):
        if item_name not in self.exporters:
            self.files[item_name] = open(
                os.path.join(
                    "vehicle_scraping",
                    "data",
                    spider.name + "_" + item_name + self.time_str + ".csv",
                ),
                "w+b",
            )
            self.exporters[item_name] = CsvItemExporter(self.files[item_name])
            self.exporters[item_name].start_exporting()

    def process_item(self, item, spider):
        item_name = item_type(item)
        if item_name in set(self.defined_items):
            self.create_exporter(item_name, spider)
            self.exporters[item_name].export_item(item)
        return item
