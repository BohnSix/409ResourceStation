import re
import time

import requests
from lxml import etree
from loguru import logger
import os
from urllib.request import urlretrieve
import json

'''
*****************************************
Usage：
    python PH_crawler.py  
*****************************************
'''



'''
    viewkeys：//*[@class="phimage"]/div/a/@href
    title：//*[@class="phimage"]/div/a/img/@alt
    duration：//*[@class="phimage"]/div/div/var
    mediabook：//*[@class="phimage"]/div/a/img/@data-mediabook
    img：//*[@class="phimage"]/div/a/img/@src
'''


# 在PH上搜索并返回搜索结果的网址
def search_on_ph(keyword):
    url = 'https://www.pornhub.com/video/search?search=%E5%BC%A0%E5%AE%87' + keyword
    response = s.get(url, headers=headers)
    html = etree.HTML(response.content)
    vks = html.xpath('//*[@class="phimage"]/div/a/@href')
    # 最后四个是直播的广告，删除
    for i in range(4):
        vks.pop()
    return vks


# 分析每个结果的网址，提取出标题，视频和图片的URL
def detail_page(vk):
    url = 'https://www.pornhub.com/%s' % vk.strip()
    response = s.get(url, headers=headers)
    html = etree.HTML(response.content)
    title = ''.join(html.xpath('//h1//text()')).strip()

    js = html.xpath('//*[@id="player"]/script/text()')[0]
    tem = re.findall('var\\s+\\w+\\s+=\\s+(.*);\\s+var player_mp4_seek', js)[-1]
    con = json.loads(tem)
    img_url = con['image_url']

    for dic in con['mediaDefinitions']:
        if 'quality' in dic.keys() and dic.get('videoUrl'):
            logger.info('%s %s' % (dic.get('quality'), dic.get('videoUrl')))
            try:
                download(dic.get('videoUrl'), title, dic.get('format'), "videos")
                download(img_url, title, img_url.split('.')[-1], "cover")
                break
            except Exception as err:
                logger.error(err)


# 根据提取到的网址下载
def download(url, title, filetype, where):
    start_time = time.time()

    urlretrieve(url, r'/{}/{}.{}'.format(where, title, filetype))
    end_time = time.time()
    logger.info("{}下载完成，用时{}秒".format(title, end_time - start_time))


if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, ' \
                 'like Gecko) Chrome/63.0.3239.84 Safari/537.36'
    headers = {'User-Agent': user_agent}

    s = requests.Session()

    logger.add("/logs/%s.log" % __file__.rstrip('.py'), format="{time:MM-DD HH:mm:ss}{level}{message}")

    choose = input("1——搜索   2——下载。请输入数字：")
    if int(choose) == 1:

        keyword = input("告诉我你想找谁：") or 'aizawa minami'
        vks = search_on_ph(keyword)
        for vk in vks:
            detail_page(vk)
    if int(choose) == 2:
        vk = input("相对URL是:")
        detail_page(vk)
