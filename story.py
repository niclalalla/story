import urllib.request
from lxml import etree
import textwrap
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # 假设将语速设置为每分钟150个单词
engine.setProperty('voice', 'com.apple.voice.compact.zh - CN.Tingting')


def create_request(url):
    '''
        构造请求request
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    '''
        得到响应内容
    '''
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


width = 80

if __name__ == '__main__':
    # 获取所有章节
    # 史上最强练气期
    # base_url = 'http://www.yetianlian.cc/yt4017/'
    # 夜的命名术
    base_url = 'http://www.yetianlian.cc/yt20281/'
    # 道诡异仙
    # base_url = "http://www.yetianlian.cc/yt77879"
    request = create_request(base_url)
    content = get_content(request)
    base_tree = etree.HTML(content)
    # 章节名
    name_list = base_tree.xpath('//div[@class="listmain"]/dl/dd/a/text()')
    # 章节地址
    url_list = base_tree.xpath('//div[@class="listmain"]/dl/dd/a/@href')

    # 定位到从哪一章开始读
    key = input('请输入要阅读的章节：')
    begin = 0
    for i in range(0, len(name_list) - 1):
        if (key in name_list[i]):
            begin = i

    for i in range(begin, len(name_list) - 1):
        input('章节名---------------------->' + name_list[i])
        # 获取具体哪一章的内容
        url = 'http://www.yetianlian.cc' + url_list[i]
        request = create_request(url)
        content = get_content(request)
        tree = etree.HTML(content)
        # 获取小说的内容
        result = tree.xpath('//div[@id="content"]/text()')
        # 遍历内容
        for res in result:
            engine.say(res)
            engine.runAndWait()
            # res = textwrap.fill(res, width=width)
            # input(res)
    engine.stop()
    print('-------------->end')
