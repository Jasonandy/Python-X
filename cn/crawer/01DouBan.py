"""
python 豆瓣爬虫词云
"""
import re
import jieba
import pandas as pd
from urllib import request
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud

import numpy as np

CommentList = []

for a in range(11):
    url = 'https://movie.douban.com/subject/11537954/comments?start={}&limit=20'.format(a*20)
    resp = request(url)
    html_data = resp.read().decode('utf-8')
    # 第二个参数是指定解析器
    soup = bs(html_data, 'html.parser')
    comment_eachpage = soup.find_all('div', class_='comment')
    for item in comment_eachpage: 
        if item.find_all('p')[0].find('span').string is not None:
            CommentList.append(item.find_all('p')[0].find('span').string)

allcomments = ''
for k in range(len(CommentList)):
    allcomments = allcomments + (CommentList[k]).strip()



pattern = re.compile('[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, allcomments)
comments_zh = ''.join(filterdata)            


segment = jieba.lcut(comments_zh)
words_detail=pd.DataFrame({'segment':segment})

stopwords=pd.read_csv(r"D:\myprograms\douban\moviecontent\chineseStopWords.txt", index_col=False,quoting=3,sep="\t",names=['stopword'], encoding=u'gbk')
words_detail=words_detail[~words_detail.segment.isin(stopwords.stopword)] 


words_result=words_detail.groupby(by=['segment'])['segment'].agg({"countnum":np.size})
words_result=words_result.reset_index().sort_values(by=["countnum"],ascending=False)


matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)


wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
word_frequence = {x[0]:x[1] for x in words_result.head(1000).values}


wordcloud=wordcloud.fit_words(word_frequence)
fig = plt.gcf()
plt.imshow(wordcloud)
fig.savefig('rick&morty.png', dpi=100)