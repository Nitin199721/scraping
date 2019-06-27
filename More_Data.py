from lxml import html
import requests
import  csv
url = 'https://www.phonecurry.com/best-phones'
res = requests.get(url)
tree = html.fromstring(res.content)

txt = tree.xpath('//*[@class="btn btn-blue-filled btn-load-more"]/text()')
i = 1
urls = []
while txt!=[]:
    url = 'https://www.phonecurry.com/best-phones?page='+str(i)
    i += 1
    print(i)
    res = requests.get(url)
    tree = html.fromstring(res.content)
    txt = tree.xpath('//*[@class="btn btn-blue-filled btn-load-more"]/text()')
    urls.extend(tree.xpath('//*[@class="phone-name"]/@href'))
mobile_list = []

for i, url1 in enumerate(urls):
    mobile_row = []
    resp1 = requests.get(url1)
    tree1 = html.fromstring(resp1.content)
    mobile_row.append(tree1.xpath('//*[@id="page-content-wrapper"]/div[3]/div/div[2]/h1/span/text()')[0])
    p = tree1.xpath('//p[1][@class="phone-sub-details"]/span[2]/text()')
    mobile_row.extend(map(lambda x: x.split()[1].encode('ascii'), p))
    mobile_row.append(tree1.xpath('//*[@id="specs"]/section/div/table[1]/tbody/tr/td[2]/text()')[0])
    mobile_row.append(tree1.xpath('//*[@id="productImg"]/img[1]/@src')[0])

    screen_resolution = tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody/tr[3]/td[2]/text()')
    if len(screen_resolution) != 0:
        mobile_row.append(screen_resolution[0])
    else:
        mobile_row.append('NA')

    screen_size = tree1.xpath('//*[@id="specs"]/section/div/table[2]/tbody/tr[2]/td[2]/text()')
    if len(screen_size) != 0:
        mobile_row.append(screen_size[0])
    else:
        mobile_list.append('NA')

    processor = tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody/tr[1]/td[2]/text()')
    if len(processor) != 0:
        mobile_row.append(processor[0])
    else:
        mobile_list.append('NA')

    GPU = tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody/tr[2]/td[2]/text()')
    if len(GPU) != 0:
        mobile_row.append(GPU[0])
    else:
        mobile_list.append('NA')

    RAM = tree1.xpath('//*[@id="specs"]/section/div/table[3]/tbody/tr[3]/td[2]/text()')
    if len(RAM) != 0:
        mobile_row.append(RAM[0])
    else:
        mobile_list.append('NA')

    mobile_list.append(mobile_row)


with open('xyz_data.csv', mode='w') as phone_data:
    writer = csv.writer(phone_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Name', 'Price', 'Smartphone OS', 'IMG PATH', 'Screen Resolution', 'Screen size', 'Processor', 'GPU', 'RAM'])
    for each_mobile in mobile_list:
        writer.writerow(each_mobile)


print (mobile_list)
