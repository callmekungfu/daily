import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://uottawa.brightspace.com/d2l/home']

    def start_requests(self):
        return [Request('https://uottawa.brightspace.com', dont_filter=True, callback=self.afterRedirect)]

    def parse(self, response):
        print('\n\nParsing')
        for title in response.css('.d2l-course-selector-item>d2l-course-selector-item-name'):
            yield {'title': title.css('a ::text').get()}
    
    def afterRedirect(self, response):
        # print(response)
        print('\n\nAfter Redirect')
        print(response.url,'\n\n')
        return FormRequest.from_response(
            response,
            formdata={ 'UserName': 'ywang737@uottawa.ca', 'Password': 'Iate#62hotdogs' },
            callback=self.afterLogin,
            clickdata={'id': 'submitButton'}
        )

    def afterLogin(self, response):
        print('\n\nAfter login')
        print('')
        if ("Incorrect user ID or password" in response.text):
            print('Failed to login\n')
            return
        else:
            print('Login Success\n')
            return FormRequest.from_response(
                response,
                callback=self.start_parsing
            )
            

    def start_parsing(self, response):
        print('\n\nParsing began:\n')
        
        yield Request('https://uottawa.brightspace.com/d2l/home')
    