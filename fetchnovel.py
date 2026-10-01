from urllib.parse import urljoin

import requests
from lxml import etree
base_url = 'https://www.quanben.io'
url = 'https://www.quanben.io/n/guimizhizhu/1.html'

while True :
   headers= {
      'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36'
   }

   resp = requests.get(url, headers=headers)

   # print(resp.text)

   e = etree.HTML(resp.text)
   title = e.xpath('//html[1]/body[1]/div[3]/h1[1]/text()')[0]
   chapter = "诡秘之主" + "_" + title
   content = e.xpath('//*[@id="content"]//p/text()')
   url = e.xpath('//html[1]/body[1]/div[3]/div[2]/span[3]/a[1]/@href')[0]
   url = urljoin(base_url, url)
   print(e.xpath('//html[1]/body[1]/div[3]/div[2]/span[3]/a[1]/@href')[0])

   with open(chapter, 'w', encoding='utf-8') as f:
      f.write(title + "\n\n".join(content))

   if url == 'https://www.quanben.io/n/guimizhizhu/1440.html':
      break