from scrapy import cmdline
from job51.spiders.job_51 import key

cmd="scrapy crawl %s"%key
cmdline.execute(cmd.split())
