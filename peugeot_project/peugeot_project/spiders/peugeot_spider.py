import scrapy
from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class PeugeotSpider(CrawlSpider):
    name = 'peugeot_spider'
    start_urls = ['https://peugeot-pechersk.ilta.ua/used-cars']

    rules = [
        Rule(LinkExtractor(allow=r'/page/\d+/'), callback='parse')
    ]

    def start_requests(self):
        # Override the start_requests method to use SplashRequest instead of regular Request
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 3})

    def parse(self, response):
        # Parse the response using Scrapy Splash
        cars = response.xpath("//div[@class='car-item']") # Select the car elements
        for car in cars:
            # Extract the car attributes
            title = car.xpath(".//h3/text()").get() # Get the car title
            link = car.xpath(".//a/@href").get() # Get the car link
            image_link = car.xpath(".//img/@src").get() # Get the car image link
            price = car.xpath(".//span[@class='price']/text()").get() # Get the car price
            year = car.xpath(".//li[1]/text()").get() # Get the car year
            mileage = car.xpath(".//li[2]/text()").get() # Get the car mileage
            engine = car.xpath(".//li[3]/text()").get() # Get the car engine
            transmission = car.xpath(".//li[4]/text()").get() # Get the car transmission
            drive = car.xpath(".//li[5]/text()").get() # Get the car drive
            yield {
                'title': title,
                'link': link,
                'image_link': image_link,
                'price': price,
                'year': year,
                'mileage': mileage,
                'engine': engine,
                'transmission': transmission,
                'drive': drive
            }
