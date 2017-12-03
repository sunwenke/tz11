# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Github, engine

class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(
                item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Github(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

