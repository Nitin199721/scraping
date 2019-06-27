from lxml import  html
import requests
import csv
url = 'https://www.phonecurry.com/best-phones'
resp = requests.get(url)
tree = html.fromstring(resp.content)
Product_url = tree.xpath('//*[@id="page-content-wrapper"]/div[3]/div[3]/div[2]/div/div/ol/li/div[@class="row mobile-list-item"]/div[3]/a[@class="phone-name"]/@href')
Phone_name,price, And_ver, screen_size, screen_res, ram, processor, gpu,Phone_img = [], [], [], [], [], [], [], [], []

for i in Product_url:
    url1 = i
    resp1 = requests.get(url1)
    tree1 = html.fromstring(resp1.content)
    Phone_name.append(tree1.xpath('//*[@id="page-content-wrapper"]/div[3]/div/div[2]/h1/span/text()')[0])
    price.append(tree1.xpath('//*[@id="page-content-wrapper"]/div[3]/div/div[2]/div[3]/div[1]/div/div/div[2]/p[@class="price"]/text()'))
    And_ver.append(tree1.xpath('//*[@id="specs"]/section/div/table[1]/tbody/tr/td[2]/text()')[0])
    Phone_img.append(tree1.xpath('//*[@id="productImg"]/img[1]/@src')[0])
    screen_res.append(tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody/tr[3]/td[2]/text()')[0])
    screen_size.append(tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody/tr[2]/td[2]/text()')[0])
    processor.append(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody/tr[1]/td[2]/text()')[0])
    gpu.append(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody/tr[2]/td[2]/text()')[0])
    ram.append(tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody/tr[3]/td[2]/text()')[0])
print(Phone_name)
print(price)
print(And_ver)
print(Phone_img)
print(screen_size)
print(screen_res)
print(processor)
print(gpu)
print(ram)

with open('phone_data.csv', mode='w') as phone_data:
    writer = csv.writer(phone_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name', 'Product URL', 'IMG_PATH', 'Price', 'Screen Size', 'Screen Resolution', 'Processor', 'GPU', 'RAM'])
    for i in range(10):
        writer.writerow([Phone_name[i],Product_url[i],Phone_img[i],price[i],screen_size[i],screen_res[i],processor[i],gpu[i],ram[i]])