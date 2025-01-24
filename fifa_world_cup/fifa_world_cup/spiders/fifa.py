import scrapy
from os.path import dirname
import os
import re
import pandas as pd
import html

current_dir = os.path.dirname(__file__)
print(f"current dir: {current_dir}")
top_dir = dirname(dirname(current_dir))
print(f"top dir {top_dir}")
url_path = os.path.join(top_dir, "data/fifa_world_cup.html")
csv_path = os.path.join(top_dir, "data/fifa_world_cup.csv")

class FifaSpider(scrapy.Spider):
    name = "fifa"
    allowed_domains = ["www.topendsports.com"]
    start_urls = [ "file://{}".format(url_path) ]
    #start_urls = ["https://www.topendsports.com/events/worldcupsoccer/winners.htm"]

    def save_csv(self, result):
        df = pd.DataFrame(result)
        df.to_csv(csv_path, index=False)

    def parse(self, response):
        _tr = response.xpath("//table[@class='list']/tr")
        result = []
        for tr in _tr:
            _td = tr.xpath("td").extract()
            # we are expecting three fields of the table (host, winner and score)
            if len(_td) != 3:
                continue

            tag_regex = r"<[^>]*>"
            year = html.unescape(re.sub(tag_regex, "", _td[0]).strip())
            winner = html.unescape(re.sub(tag_regex, "", _td[1]).strip())
            score = html.unescape(re.sub(tag_regex, "", _td[2]).strip())
            result.append({ "year": year, "winner": winner, "score": score })

        self.save_csv(result)
