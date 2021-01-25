import requests, re
from bs4 import BeautifulSoup #用于解析网页的库

def get_city():
    url='https://www.cnblogs.com/daly2008/archive/2013/05/25/3099467.html'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
    res1 = requests.get(url, headers=header)
    soup = BeautifulSoup(res1.text, 'html.parser')
    bf = soup.find('div', class_='blogpost-body')
    city1 = bf.get_text() #get_text()方法可以清空所有html标签元素之后，返回干净的文字
    city2 = city1.replace(' ','')
    city2_name = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", city2) #保留字符串的中文部分
    city2_name = city2_name.replace(':', ':\n') #将冒号替换成冒号加换行，实现遇到冒号后就换行的效果
    city2_name = city2_name.replace(':','')
    city2_name = city2_name.split('\n')
    city2_code1 = ''.join(filter(lambda c:ord(c)<256,city2)) #删除字符串的中文部分
    city2_code = city2_code1.replace(':', '')
    city2_code = re.sub(r"(.{9})","\\1\n",city2_code) #每隔9个字符插入一个换行符
    city2_code = city2_code.split('\n')
    for i in range(3):
        city2_name.remove('')
        city2_code.remove('')
        pass
    # print(city2_name)
    # print(city2_code)
    city = {}
    for j in range(0,446):
        city[city2_name[j]] = city2_code[j]
        pass
    return city