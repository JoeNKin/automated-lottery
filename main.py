import tkinter as tk
from tkinter import font
import re
import threading
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import time
import random
import os
import schedule
import requests
from  bs4 import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''

'''



# 创建 ChromeOptions 对象，并设置无头模式
# options = Options()
# options.add_argument('--headless')
# 创建一个webdriver实例
driver = webdriver.Chrome()
with open('cookie_b.nk', 'r', encoding='utf-8') as f:
    reader = f.read()
    cookies = list(eval(reader))

driver.get("https://space.bilibili.com/")
for cookie in cookies:
    driver.add_cookie(cookie)

send_list1=["|--(消息)----------------开始"]

def zuanfa(url, com):
    # 打开网页
    driver.get(url)

    try:
        # 等待span[data-type='lottery']元素加载出来
        lottery_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-type='lottery']"))
        )

        # 点击div[class='bili-dyn-title']
        dyn_title_element = driver.find_element(By.CSS_SELECTOR, "div.bili-dyn-title")
        dyn_title_element.click()

        # 等待新标签页打开
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))

        # 切换到新标签页
        driver.switch_to.window(driver.window_handles[1])
        random_number = random.randint(2, 4)
        time.sleep(random_number)

        try:
            # 检查是否存在span[class='h-f-btn h-follow']元素
            follow_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.h-f-btn.h-follow"))
            )

            # 点击span[class='h-f-btn h-follow']
            follow_element.click()
            random_number = random.randint(1, 6)
            time.sleep(random_number)

        except:
            send_list1.append("|--(消息)-------操作:"+"已关注")
        # 关闭第二个标签页
        driver.close()
        # 切换回原始标签页
        driver.switch_to.window(driver.window_handles[0])
        random_number = random.randint(3, 5)
        time.sleep(random_number)

        # 等待目标元素可见
        wait = WebDriverWait(driver, 10)
        target_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-module="action"][data-type="forward"]')))

        # 点击目标元素
        target_element.click()
        # 等待按钮可见
        button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.bili-dyn-forward-publishing__action__btn')))

        # 点击按钮
        button.click()



    except TimeoutException:
        send_list1.append("|--(消息)-------操作:"+"不是转发评论")
        # 设置等待时间上限
        wait = WebDriverWait(driver, 5)
        try:
            # 等待div[class='bili-dyn-card-reserve']元素加载出来
            reserve_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.bili-dyn-card-reserve"))
            )

            # 判断是否有button[class='uncheck']
            try:
                uncheck_button = reserve_element.find_element(By.CSS_SELECTOR, "button.uncheck")

                # 点击button[class='uncheck']
                uncheck_button.click()

            except:
                send_list1.append("|--(消息)-------操作:"+"已经预约完成")

        except TimeoutException:
            send_list1.append("|--(消息)-------操作:"+"不是官方抽奖")
    send_list1.append("|--(消息)-------操作:" + "完成操作")

def main_b():
    try:
        if os.path.exists("log.nk"):
            with open('log.nk', 'r', encoding='utf-8') as log:
                reader = log.read()
                url_de = list(eval(reader))
                log.close()
                # log =open('log.nk', 'w', encoding='utf-8')
        else:
            url_de = []

        urls = []

        url_ok = []
        url = 'https://api.bilibili.com/x/space/wbi/article'
        params = {
            'mid': '3493086911007529',
            'pn': '1',
            'ps': '12',
            'sort': 'publish_time',
            'web_location': '1550101',
            'platform': 'web',
            'w_rid': 'a256a607f1fa7d023803743ac106d29e',
            'wts': '1690605435'
        }

        headers = {
            'authority': 'api.bilibili.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'origin': 'https://space.bilibili.com',
            'referer': 'https://space.bilibili.com/3493086911007529/article',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        articles = data['data']['articles']
        for article in articles:
            id = article['id']
            url_id = "https://www.bilibili.com/read/cv" + str(id)
            urls.append(url_id)
        send_list1.append(url_de)
        send_list1.append("|--(消息)-------------------成功加载----------------------------")
        for url in urls:
            headers = {
                'authority': 'www.bilibili.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': 'buvid3=D7700999-F1EF-6EEF-4253-470D0A5188C523119infoc; b_nut=1690606023; b_lsid=ABB8B9FB_1899FF8B3EF; _uuid=7BE41948-8FDA-61E8-B10DE-12AE2C6842A423674infoc; buvid_fp=83b53b9c92d45bd84155dfd329d9f5f9; buvid4=E63F85EA-E0C0-E34A-A542-3744C41BDDF525765-023072912-kji2bknSwKf3tqZzMqSpLRdzIgFni0vPwxWs8AWDuKoh4uj9kE90Iw%3D%3D',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
            comoms = []
            response = requests.get(url, headers=headers)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            # 使用选择器方法提取符合条件的内容
            results = soup.select('p a.article-link')
            for result in results:
                comom = result.parent.text.strip()
                comoms.append(comom)

            data = "\n".join(comoms)

            # 正则表达式提取时间和URL
            pattern = r'(\d{2}月\d{2}日 \d{2}:\d{2}).*?(https?://\S+)'
            matches = re.findall(pattern, data)

            # 当前时间（不比较年份）
            current_time = datetime.now().replace(year=2023)

            # 提取结果
            for match in matches:
                time_str, url = match
                if url not in url_de:
                    url_de.append(url)
                    # 转换时间字符串为datetime对象（不包含年份）
                    time1 = datetime.strptime(time_str, '%m月%d日 %H:%M').replace(year=2023)
                    if time1 > current_time:
                        com = str(time1) + "中！！！！"
                        send_list1.append("|--(消息)-------网址:"+url)
                        zuanfa(url, com)
                        send_list1.append('''---------------------------------------------------------------------
                                                ''')
                        # Thread(target=zuanfa, args=(url,com)).start()
                        log = open('log.nk', 'w', encoding='utf-8')
                        log.write(str(url_de))
                        log.close()
                        random_number = random.randint(15, 40)
                        time.sleep(random_number)
    except Exception as e:
        send_list1.append(e)


# ------------------------------------------------------------------------

send_list2=["|--(消息)----------------开始"]




if os.path.exists("log_wb.nk"):
    with open('log_wb.nk', 'r', encoding='utf-8') as log:
        reader = log.read()
        url_de2 = list(eval(reader))
        log.close()
        # log =open('log.nk', 'w', encoding='utf-8')
else:
    url_de2=[]
send_list2.append(url_de2)
# 配置 ChromeOptions
chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1')  # 设置 iPhone 12 的 user agent
# chrome_options.add_argument('--headless')
# 启动带有特定配置的浏览器
driver_b = webdriver.Chrome(options=chrome_options)

with open('cookie_wb.nk', 'r', encoding='utf-8') as f:
    reader = f.read()
    cookies = list(eval(reader))
# 打开网页
driver_b.get("https://m.weibo.cn/")
time.sleep(4)
for cookie in cookies:
    driver_b.add_cookie(cookie)
driver_b.refresh()
answerend_lists=["(",'!',"[送花花]","呀","","()","[流浪者]","~","[可莉]"]
def pinglu(url,com):
    com=com+str(random.choice(answerend_lists))
    try:
        driver_b.get(str(url))
        time.sleep(3)
        # 点击第一个被 flex 的 <div>
        first_div = driver_b.find_element(By.XPATH, '//div[@data-v-69b4128e]')
        first_div.click()

        # 等待第二个被 flex 的 <div> 加载完成
        second_div = WebDriverWait(driver_b, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'm-wz-def')))
        second_div = driver_b.find_element(By.CLASS_NAME, 'm-wz-def')
        text_input = second_div.find_element(By.TAG_NAME, 'textarea')

        # 在第二个 <div> 中发送文本
        text_input.send_keys(str(com))
        # 使用 JavaScript 设置样式属性为 display: flex
        driver_b.execute_script("arguments[0].style.display = 'flex';", second_div)
        # 等待目标元素出现（<a class="m-send-btn">）
        target_btn = WebDriverWait(driver_b, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.m-send-btn:not(.disabled)')))

        # 点击目标元素
        target_btn.click()

        # 等待3秒，等待评论提交完成
        time.sleep(3)
        # 获取页面文本内容
        page_text = driver_b.page_source
        if "发微博太多啦，休息一会儿吧!" in page_text:
            random_number = random.randint(260, 320)
            send_list2.append("|--(警告)-------发微博太多啦，休息"+str(random_number)+"s")
            time.sleep(random_number)
            send_list2.append("|--(重新)-------开始重试")
            pinglu(url, com)

    except:
        send_list2.append("|--(报错)-------异常,60秒后重新尝试")

        time.sleep(60)
        # send_list2.append("|--(重新)-------开始重试")
        # pinglu(url, com)









answer_lists=["来了来了","开心呀[送花花]","蹲蹲","[赢牛奶]开心就好了","顿"]
def answermain(response):
    date=(response.json())
    cards=date['data']['cards']
    for card in cards:
        mid=card['mblog']['mid']
        mid_url = "https://m.weibo.cn/detail/" + str(mid)
        if mid_url not  in  url_de2:
            mid_text=card['mblog']['text']
            mid_text = BeautifulSoup(mid_text, 'html.parser')
            mid_text = mid_text.text
            if "//@" not in mid_text:
                mid_own = card['mblog']['user']["id"]

                pinglu_1_url="https://m.weibo.cn/comments/hotflow?id="+str(mid)+"&mid="+str(mid)+"&max_id_type=0"

                headers = {
                    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                    'X-XSRF-TOKEN': 'e25623',
                    'sec-ch-ua-mobile': '?0',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                    'Accept': 'application/json, text/plain, */*',
                    'MWeibo-Pwa': '1',
                    'Referer': mid_url,
                    'X-Requested-With': 'XMLHttpRequest',
                    'sec-ch-ua-platform': '"Windows"'
                }

                response = requests.get(pinglu_1_url, headers=headers)

                date=(response.json())

                try:
                    common_lists=date['data']['data']
                    a=0
                    com_tf=False
                    while a <=len(common_lists):
                        common_owner=common_lists[a]['user']["id"]
                        if common_owner==mid_own:
                            a=a+1
                            continue
                        else:
                            common=date['data']['data'][a]['text']
                            soup = BeautifulSoup(common, 'html.parser')
                            common=soup.text
                            com_tf= True
                            break
                    if com_tf == False:
                        common=str(random.choice(answer_lists))

                except:
                    # print(e)
                    common=str(random.choice(answer_lists))

                send_list2.append("|--(消息)-------网址:"+mid_url)
                send_list2.append("|--(消息)-------原文:"+mid_text)
                send_list2.append("|--(消息)-------回答:"+common)
                pinglu(mid_url,common)
                url_de2.append(mid_url)
                log = open('log_wb.nk', 'w', encoding='utf-8')
                log.write(str(url_de2))
                log.close()
                send_list2.append('''---------------------------------------------------------------------
                        ''')
                random_number = random.randint(8, 25)
                time.sleep(random_number)




def main():
    # 抽氵
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%8A%BD%E6%B0%B5%26t%3D&page_type=searchall'

    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': '094b96',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%8A%BD%E6%B0%B5',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.get(url, headers=headers)
    answermain(response)

    # 抽个氵
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%8A%BD%E4%B8%AA%E6%B0%B5%26t%3D&page_type=searchall'

    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': 'a1ccc7',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%8A%BD%E4%B8%AA%E6%B0%B5',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.get(url, headers=headers)
    answermain(response)


    # 抽个🍬
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': '656231',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%8A%BD%E4%B8%AA%F0%9F%8D%AC',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%8A%BD%E4%B8%AA%F0%9F%8D%AC%26t%3D&page_type=searchall'

    response = requests.get(url, headers=headers)
    answermain(response)

    # 抽个糖
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': '656231',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%8A%BD%E4%B8%AA%E7%B3%96',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%8A%BD%E4%B8%AA%E7%B3%96%26t%3D&page_type=searchall'

    response = requests.get(url, headers=headers)
    answermain(response)

    # 抽糖
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': '656231',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%8A%BD%E7%B3%96',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%8A%BD%E7%B3%96%26t%3D&page_type=searchall'

    response = requests.get(url, headers=headers)
    answermain(response)

    # kls
    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': 'c9d0de',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3Dkls',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3Dkls%26t%3D&page_type=searchall'

    response = requests.get(url, headers=headers)
    answermain(response)

    # 抽个水
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%8A%BD%E4%B8%AA%E6%B0%B4%26t%3D&page_type=searchall'

    headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'X-XSRF-TOKEN': 'c9d0de',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%8A%BD%E4%B8%AA%E6%B0%B4',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.get(url, headers=headers)
    answermain(response)

def startone():
    try:
        main()
        # 每3小时运行一次 main 函数
        schedule.every(3).hours.do(main)

        while True:
            schedule.run_pending()
            time.sleep(100)
    except Exception as e:
        send_list2.append(e)


class LogViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动化抽奖  -by甯衎")

        # 设置字体为微软雅黑
        font_style = font.Font(family="微软雅黑")

        self.log_text1 = tk.Text(self.root, wrap=tk.WORD, font=font_style)
        self.log_text1.grid(row=0, column=0, sticky=tk.NSEW)

        self.log_text2 = tk.Text(self.root, wrap=tk.WORD, font=font_style)
        self.log_text2.grid(row=0, column=1, sticky=tk.NSEW)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=2)

        self.start_button = tk.Button(button_frame, text="开始b站运行", command=self.start_logging)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(button_frame, text="开始wb运行", command=self.start_logging2)
        self.stop_button.pack(side=tk.RIGHT, padx=20)

        self.is_logging = False
        self.log_thread1 = None
        self.log_thread2 = None

        # 设置网格布局权重以适应页面缩放
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)




    def start_logging(self):
        self.is_logging = True

        self.log_thread1 = threading.Thread(target=self.update_log, args=(self.log_text1, self.get_log_line_project1))
        # self.log_thread2 = threading.Thread(target=self.update_log, args=(self.log_text2, self.get_log_line_project2))
        threading.Thread(target=main_b).start()

        self.log_thread1.start()
        # self.log_thread2.start()
    def start_logging2(self):
        self.is_logging = True

        # self.log_thread1 = threading.Thread(target=self.update_log, args=(self.log_text1, self.get_log_line_project1))
        self.log_thread2 = threading.Thread(target=self.update_log, args=(self.log_text2, self.get_log_line_project2))
        threading.Thread(target=startone).start()

        # self.log_thread1.start()
        self.log_thread2.start()






    def update_log(self, log_text, get_log_line_func):
        while self.is_logging:
            log_line = get_log_line_func()  # 替换成获取日志的函数
            log_text.insert(tk.END, log_line + '\n')
            log_text.see(tk.END)
            time.sleep(1)  # 每秒刷新一次日志

    def get_log_line_project1(self):
        while True:
            try:

                item = send_list1.pop(0)  # 从列表中获取第一个元素并删除
                item=str(item)
                return (item)
            except:
                continue
        # 替换成你获取项目1日志的实际逻辑

    def get_log_line_project2(self):
        while True:
            try:

                item = send_list2.pop(0)  # 从列表中获取第一个元素并删除
                item = str(item)
                return (item)
            except:
                continue
        # 替换成你获取项目2日志的实际逻辑


if __name__ == "__main__":
    root = tk.Tk()
    app = LogViewerApp(root)
    root.mainloop()
