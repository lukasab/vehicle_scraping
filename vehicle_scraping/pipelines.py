# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
from vehicle_scraping import items


def item_type(item):
    return type(item).__name__


class MultiCSVItemPipeline(object):
    defined_items = [name for name, _ in items.__dict__.items() if "Item" in name]

    def open_spider(self, spider):
        self.files = dict(
            [
                (name, open("vehicle_scraping/data/" + name + ".csv", "w+b"))
                for name in self.defined_items
            ]
        )
        self.exporters = dict(
            [(name, CsvItemExporter(self.files[name])) for name in self.defined_items]
        )
        [e.start_exporting() for e in self.exporters.values()]

    def close_spider(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

    def process_item(self, item, spider):
        item_name = item_type(item)
        if item_name in set(self.defined_items):
            self.exporters[item_name].export_item(item)
        return item
