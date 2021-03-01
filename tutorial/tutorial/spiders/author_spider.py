import scrapy

class AuthorSpider(scrapy.Spider):
    name= 'author'

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_link = response.css('li.next a')
        yield from response.follow_all(pagination_link, self.parse)

    def parse_author(self, response):
        yield {
            'name': response.css('h3.author-title::text').get(),
            'birthdate': response.css('span.author-born-date::text').get(),
            'bio': response.css('.author-description::text').get()
        }