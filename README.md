# Automated lottery

#### 介绍
自动化扫描并参与微博和哔哩哔哩的抽奖
!!欢迎各位创作者对本项目进行再开发
!!如果您对计算机语言没有任何的学习,建议使用发行版本运行
#### 新版本更新说明
以下简介不能解释最新版，最新版对所以进行重新构造，无需您进行环境配置，但未了不必要的麻烦只更新核心代码
同时删除wb功能

#### ----------------------------------------------------------------
#### 软件架构
软件架构说明
本项目全部由python开发编写
requests + webdriver(chrome) +tkinter开发


#### 原身安装教程

1.  安装python和chrome(其他浏览器也可以但是你要会自己调代码)
2.  自行配置环境
    所需要的库:
    ```
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
    ```

3.  运行

#### 使用说明

1.  保证网络联通正常,导致封号等自我承担与本项目作者无关
2.  本项目开源许可证为gpl-3.0(https://www.gnu.org/licenses/gpl-3.0.en.html)
3.  本项目为免费项目,你被收费和项目作者没关系,请您自行解决:如果你想对项目的作者进行感谢可以看最后

#### 参与作者

1.  所以作者名字:甯衎
!欢迎各位创作者对本项目进行再开发
#### 帮助安装
如果您实在想以源码运行但自己不会,可以联系我caibbdd@163.com,请顺便留下您的联系方式方便交流(!!帮忙可能会收取一些小费大概0~20r 看问题)


#### 赞赏

1.  如果您对作者表示感谢,可以请问喝点水(doge
![输入图片说明](https://foruda.gitee.com/images/1691581348638834804/14b1cc01_7640852.jpeg "微信图片_20230809194219.jpg")
