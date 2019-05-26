#!/usr/bin/env python
# encoding=utf-8
import requests
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
wb = Workbook()
dest_filename = '电影.xlsx'
ws1 = wb.active
ws1.title = "电影top250"

# 豆瓣Api地址
DOWNLOAD_URL = 'http://movie.douban.com/top250/'


def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    print('DouBan apiUrl:%s , RespData: %s ... ' % (url, data))
    return data


def get_li(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('ol', class_='grid_view')
    # 名字
    name = []
    # 评价人数
    star_con = []
    # 评分
    score = []
    # 短评
    info_list = []
    for i in ol.find_all('li'):
        detail = i.find('div', attrs={'class': 'hd'})
        movie_name = detail.find(
            # 电影名字
            'span', attrs={'class': 'title'}).get_text()
        level_star = i.find(
            # 评分
            'span', attrs={'class': 'rating_num'}).get_text()
        star = i.find('div', attrs={'class': 'star'})
        # 评价
        star_num = star.find(text=re.compile('评价'))
        # 短评
        info = i.find('span', attrs={'class': 'inq'})
        # 判断是否有短评
        if info:
            info_list.append(info.get_text())
        else:
            info_list.append('暂无评分')
        score.append(level_star)
        name.append(movie_name)
        star_con.append(star_num)
    # 获取下一页
    page = soup.find('span', attrs={'class': 'next'}).find('a')
    if page:
        return name, star_con, score, info_list, DOWNLOAD_URL + page['href']
    return name, star_con, score, info_list, None


def main():
    url = DOWNLOAD_URL
    name = []
    star_con = []
    score = []
    info = []
    while url:
        doc = download_page(url)
        movie, star, level_num, info_list, url = get_li(doc)
        name = name + movie
        star_con = star_con + star
        score = score + level_num
        info = info + info_list
    for (i, m, o, p) in zip(name, star_con, score, info):
        col_a = 'A%s' % (name.index(i) + 1)
        col_b = 'B%s' % (name.index(i) + 1)
        col_c = 'C%s' % (name.index(i) + 1)
        col_d = 'D%s' % (name.index(i) + 1)
        ws1[col_a] = i
        ws1[col_b] = m
        ws1[col_c] = o
        ws1[col_d] = p
    wb.save(filename=dest_filename)


if __name__ == '__main__':
    main()

