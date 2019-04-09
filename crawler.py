import sys
import scrapy
from scrapy.http import Request
from scrapy.http import FormRequest

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    
    email = 'YOUR_EMAIL_HERE'
    password = 'YOUR_PASSWORD_HERE'

    start_urls = ['https://uottawa.brightspace.com/d2l/le/content/102575/Home']

    def start_requests(self):
        return [Request('https://uottawa.brightspace.com', dont_filter=True, callback=self.afterRedirect)]

    def parse(self, response):
        print('\nParsing')
        print(response.text)
        for title in response.css('.d2l-navigation-s-item'):
            print(str({'title': title.css('a ::text').get()}))
    
    def afterRedirect(self, response):
        # print(response)
        print('\nAfter Redirect')
        print(response.url)
        return FormRequest.from_response(
            response,
            formdata={ 'UserName': self.email, 'Password': self.password },
            callback=self.afterLogin,
            clickdata={'id': 'submitButton'}
        )

    def afterLogin(self, response):
        print('\nAfter login')
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
        print('\nParsing began:\n')
        yield Request('https://uottawa.brightspace.com/d2l/home')
    