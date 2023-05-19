import scrapy
from ..items import EbayItem

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    page_num = 2
    start_urls = [
        'https://www.ebay.com/b/Samsung/bn_21834655'
    ]

    def parse(self, response):
        words = response.css('#s0-27_2-9-0-1\[0\]-0-0 .clearfix')

        items = EbayItem()

        for word in words:
            title = word.css('.s-item__title::text').extract_first()
            price = word.css('.s-item__price::text').extract_first()
            products_sold = word.css('.NEGATIVE::text').extract_first()
            products_rating = word.css('.b-rating__rating-count span::text').get()

            items['title'] = title
            items['price'] = price
            items['products_sold'] = products_sold
            items['products_rating'] = products_rating

            yield items

            next_page = f'https://www.ebay.com/b/Samsung/bn_21834655?_pgn={EbaySpider.page_num}'
            if EbaySpider.page_num <= 10:
                EbaySpider.page_num +=1
                yield response.follow(next_page, callback=self.parse)
