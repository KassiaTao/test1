# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ForeignexchangePipeline(object):
    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('result.txt', 'a', encoding='utf-8')
        print('result.txt文件已打开')

    def process_item(self, item, spider):
        line = f"{item['currency_name']}\t{item['spot_purchase_price']}\t{item['cash_purchase_price']}\t{item['spot_selling_price']}\t{item['cash_selling_price']}\t{item['boc_discounted_price']}\t{item['release_time']}\n"
        self.file.write(line)
        print('数据已写入result.txt文件')
        return item

    def close_spider(self, spider):
        self.file.close()
        print('result.txt文件已关闭')


