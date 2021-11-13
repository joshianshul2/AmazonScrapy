import scrapy
from ..items import AmazonscrapyItem
import pandas as pd
import os
# n=1

class AmazonScrap(scrapy.Spider):
    name = 'amazon'
    n = 1
    # start_urls =[
    #     # 'https://quotes.toscrape.com'
    #     # 'https: // www.amazon. in / Apple - iPhone - 13 - 256GB - Starlight / dp / B09G9BFKZN / ref = sr_1_4?keywords = iphone + 13 & qid = 1636577482 & sr = 8 - 4'
    #     # 'https://www.amazon.in/dp/B089MS7D8F/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=VY17PK5WN2TKMK73SSPF&pf_rd_t=101&pf_rd_p=c72a5fc5-b047-4381-a508-8e89492aff17&pf_rd_i=20303904031&th=1'
    #     # 'https://www.amazon.in/Bigmuscles-Nutrition-Chocolate-Concentrate-Glutamic/dp/B084H8LWC3?ref_=Oct_DLandingS_D_c1701101_60&smid=AT95IG9ONZD7S',
    #     'https://www.amazon.in/TCL-inches-Certified-Android-55P615/dp/B08FD3269H?th=1',
    #     'https://www.amazon.in/Sony-Bravia-inches-KD-65X80J-Compatibility/dp/B091N3MQ92?th=1'
    #
    #     # 'http://' + 'www.amazon. in / Apple - iPhone - 13 - 256GB - Starlight / dp / B09G9BFKZN / ref = sr_1_4?keywords = iphone + 13 & qid = 1636577482 & sr = 8 - 4'.encode('idna').decode('utf-8')
    # ]


    def start_requests(self):
        df = pd.read_csv('aj.csv')
        #Here fileContainingUrls.csv is a csv file which has a column named as 'URLS'
        # contains all the urls which you want to loop over.
        urlList = df['URLS'].to_list()

        for i in urlList:
             yield scrapy.Request(url = i, callback=self.parse)

    def parse(self,response):
        # title = response.css('title').extract()
        items = AmazonscrapyItem()
        # header = ["Product Name", "Price"]
        # df1 = pd.DataFrame()

        product_name = response.css('#productTitle::text').extract()
        product_price = response.css('#priceblock_ourprice').css('::text').getall()
        # product_details = response.css('.a-size-base').css('::text').getall()
        # yield {'titletext': title}

        items['product_name'] = product_name
        items['product_price'] = product_price
        # items['product_details'] = product_details


        yield items
        print("Anshul joshi")

        print("Rishiii", items['product_name'], items['product_price'])
        dict = {'product_name':items['product_name'], 'product_price':items['product_price']}
        # lst=[ items['product_name'] , items['product_price'] ]

        # dict["Age"].append(30)
        # print(lst)

        df = pd.DataFrame(dict)
        print("hi from csv")
        # result = df.loc[:, ['items['product_name']', 'items['product_price']']]
        # os.remove('example.csv')


        # saving the dataframe
        # df.to_csv('rishu.csv')
        # header = ["product_name","product_price"]
        # df.to_csv('my_csv.csv', mode='a')
        df.to_csv("test1.csv",mode='a',index=False)


