import requests
from lxml import etree
from loguru import logger

'''
    封面放封面、时长和名字
    内容放视频和名字
    先获取viewkeys：//*[@class="phimage"]/div/a/@href
    名字title：//*[@class="phimage"]/div/a/img/@alt
    时长duration：//*[@class="phimage"]/div/div/var
    小视频mediabook：//*[@class="phimage"]/div/a/img/@data-mediabook
    封面img：//*[@class="phimage"]/div/a/img/@src
'''
url = "https://www.pornhub.com/video/search?search=minami+aizawa"
jobs = []
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, ' \
             'like Gecko) Chrome/63.0.3239.84 Safari/537.36'
headers = {'User-Agent': user_agent}
logger.add()

def list_jobs(url):
    response = requests.get(url, headers=headers)
    html_str = response.text

    html = etree.HTML(html_str)
    vks = html.xpath('//*[@class="phimage"]/div/a/@href')
    viewkeys = []
    for i in vks:
        viewkeys.append(i.split('=')[-1])
    titles = html.xpath('//*[@class="phimage"]/div/a/img/@alt')
    durations = html.xpath('//*[@class="phimage"]/div/div/var')
    mediabooks = html.xpath('//*[@class="phimage"]/div/a/img/@data-mediabook')
    imgs = html.xpath('//*[@class="phimage"]/div/a/img/@src')

    for i in range(len(vks)):
        item = {}
        item['viewkey'] = vks[i].split('=')[-1]
        item['mediabook'] = mediabooks[i]
        item['duration'] = durations[i].xpath('string(.)')
        item['img'] = imgs[i]
        jobs.append(item)
    return jobs


def download(item):
    base_url = 'https://www.pornhub.com/view_video.php?viewkey='
    url = base_url + item['viewkey']
    s = requests.Session()
    response = s.get(url, headers=headers)
    html = etree.HTML(response.content)
    item['video_url'] = html.xpath('//*[@player]/script/text()')[0]
