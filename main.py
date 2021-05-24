import requests
from bs4 import BeautifulSoup
from pandas import read_excel
import gspread
import time

def ReadingExcel(constant_url):
    print("[+] Links are testing for validation ")
    file_name = 'databrovski.xlsx'  # assigning the path and file name at the same time super lol !
    df = read_excel(file_name)  # reading the excel file
    new_list= df.values.tolist() #returning to list
    only_links=[]
    for i in range(len(new_list)): #appending links to array
        only_links.append(new_list[i][0])
    real_working_links=[]
    for i in range(len(only_links)):
        r = requests.get(constant_url+only_links[i])
        soup = BeautifulSoup(r.content, 'html.parser')
        if (soup.find("div", {"class": "detay-indirim"}) != None): #eliminating the useless links respect to having a discount or not
            real_working_links.append(only_links[i])
            print(only_links[i])
            #time.sleep(2) might need if we have so much traffic on the server responses. (Check Arp comings or 3-way-handshakes to detailly plan )
    if(real_working_links!=0):
        print("[+] Links are created and controlled ")
        print("[info] ", len(real_working_links), "URL's are valid to detect elements")
    else:
        print("[-] No valid links found ! Check the .xlsx file ")
    return real_working_links

def SkuParser(item): #parser for the SKU for each product
    list=item.split(" ")
    index_dot=list[len(list)-1].find(".")
    new_parsed_sku=list[len(list)-1][index_dot-14:]
    return new_parsed_sku

def IdentifyingProductName(list,constant_url):
    print("[+] Items started to drop in the Product Name List")
    product_names=[]
    for i in range(len(list)):
        r = requests.get(constant_url+list[i])
        soup =BeautifulSoup(r.content,'html.parser')
        name=soup.find("h1",{"id":"product-name"}).text
        namee=name.split()
        namee.pop(0)
        new_name = ' '.join(str(e) for e in namee)
        product_names.append(new_name)
        print(new_name)
    if (len(product_names) != 0):
        print("[+] Items Dropped to the Product Name List")
    else:
        print("[-] Items Can't Dropped to the Product Name List")
    return product_names
def IdentifyingProductOfferPrice(list,constant_url):
    print("[+] Items started to drop in the Product Offer List ")
    product_offer_price = []
    for i in range(len(list)):
        r2 = requests.get(constant_url + list[i])
        soup = BeautifulSoup(r2.content,'html.parser')
        product_offer_price.append(str(soup.find("div", {"class": "detay-indirim"}).text))
        print(str(soup.find("div", {"class": "detay-indirim"}).text))
    if (len(product_offer_price) != 0):
        print("[+] Items Dropped to the Product Offer List ")
    else:
        print("[-] Items Can't Dropped to the Product Offer List ")
    return product_offer_price

def IdentifyingProductPrice(list,constant_url):
    print("[+] Items started to drop in the Product Price List ")
    product_price = []
    for i in range(len(list)):
        r3 = requests.get(constant_url + list[i])
        soup = BeautifulSoup(r3.content,'html.parser')
        product_price.append(str(soup.find("span", {"class": "currencyPrice discountedPrice"}).text))
        print(str(soup.find("span", {"class": "currencyPrice discountedPrice"}).text))
    if (len(product_price) != 0):
        print("[+] Items Dropped to the Product Price List ")
    else:
        print("[-] Items Can't Dropped to the Product Price List ")
    return product_price

def IdentifyingProductSalePrice(list,constant_url):
    print("[+] Items started to drop to the Product Sale List ")
    product_sale_price = []
    for i in range(len(list)):
        r4 = requests.get(constant_url + list[i])
        soup = BeautifulSoup(r4.content,'html.parser')
        product_sale_price.append(str(soup.find("span", {"class": "product-price"}).text))
        print(str(soup.find("span", {"class": "product-price"}).text))
    if (len(product_sale_price) != 0):
        print("[+] Items Dropped to the Product Sale List ")
    else:
        print("[-] Items Can't Dropped to the Product Sale List ")
    return product_sale_price

def IdentifyingProductStocks(list,constant_url):
    print("[+] Items started to drop in Product Stock's List")
    product_stocks = []
    for i in range(len(list)):
        r5 = requests.get(constant_url + list[i])
        soup = BeautifulSoup(r5.content,'html.parser')
        total_options=len(soup.find_all("a", {"data-group-id": "2"}))
        counter_avaible=0
        for link in soup.find_all("a", {"class": "col box-border"}):
            counter_avaible=counter_avaible+1
        real_avaibility=float(counter_avaible/total_options)*100
        append="{:.1f}".format(real_avaibility)
        product_stocks.append(append)
        print(append)
    if(len(product_stocks)!=0):
        print("[+] Items Dropped to the Product Stock's List")
    else:
        print("[-] Items Can't Dropped to the Product Stock's List")
    return product_stocks

def IdentifyingProductSKU(list,constant_url):
    print("[+] Items started to drop in Product SKU List ")
    product_sku = []
    for i in range(len(list)):
        r6 = requests.get(constant_url + list[i])
        soup = BeautifulSoup(r6.content,'html.parser')
        div = soup.find('div', {'class': 'product-feature-content'}).text
        parsed_sku=SkuParser(div)
        product_sku.append(parsed_sku)

        print(parsed_sku)
    if (len(product_sku) != 0):
        print("[+] Items Dropped to the Product SKU List ")
    else:
        print("[-] Items Can't Dropped to the Product SKU List ")
    return product_sku

def ExcelDone(product_names,product_offer_price,product_price,product_sale_price,product_stocks,product_sku,whole_list,constant_url_main):
    print("[+] Starting to write rows to Excel...")
    gc = gspread.service_account(filename='keys.json')
    sh = gc.open_by_key('1vY6aAdGZ5wOF8peHqiS-qhmSjcesh_w9ER-IX0gApj8')
    worksheet = sh.sheet1
    for i in range(len(whole_list)):
        sh = gc.open_by_key('1vY6aAdGZ5wOF8peHqiS-qhmSjcesh_w9ER-IX0gApj8')
        worksheet = sh.sheet1
        user = [str(constant_url_main+whole_list[i]) ,str(product_sku[i]) ,str(product_names[i]) ,(str(product_stocks[i])) , product_price[i] , str(product_offer_price[i]), str(product_sale_price[i])]
        worksheet.insert_row(values=user)
        time.sleep(2)
        if(i==len(whole_list)-1):
            user = ['URL', 'SKU', 'Product Name', 'Avaibility', 'Product Price', 'Price offer', 'Product Sale Price']
            worksheet.insert_row(values=user)
    print("[+] Writing Excel Successful ...")

def MainFunction(): #Main function running the slow bea$t :(
    print("CaseStudy Demo for AnalyticaHouse by Yaman Şener ")
    constant_url_main="https://www.markastok.com"
    whole_list=ReadingExcel(constant_url_main)
    product_names=IdentifyingProductName(whole_list,constant_url_main) #Function call for gathering productname
    product_offer_price=IdentifyingProductOfferPrice(whole_list,constant_url_main) #Function call for gathering productofferprice
    product_price=IdentifyingProductPrice(whole_list,constant_url_main) #Function call for gathering productprice
    product_sale_price=IdentifyingProductSalePrice(whole_list, constant_url_main) #Function call for gathering productsaleprice
    product_stocks=IdentifyingProductStocks(whole_list,constant_url_main) #Function call for gathering productstocks
    product_sku=IdentifyingProductSKU(whole_list,constant_url_main)
    ExcelDone(product_names,product_offer_price,product_price,product_sale_price,product_stocks,product_sku,whole_list,constant_url_main) #Function to write list items to Excel

MainFunction()