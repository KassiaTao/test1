import requests
from bs4 import BeautifulSoup
import xlwings as xw
from requests.exceptions import RequestException

def getHTML(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.get(url,timeout=30, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def getBank(soup):
    # 查找数据所在表格
    table = soup.find_all('table')[1]
    # print(table)
    dataAll = []
    for all_tr in table.find_all('tr'):  # 找到所有tr,返回一个列表
        all_th = all_tr.find_all('th')
        # print(all_th)
        all_td = all_tr.find_all('td')
        # print(all_td)
        if len(all_th) > 0:
            dataRow = []
            for item in all_th:
                dataRow.append(item.text)
            dataAll.extend([dataRow])
        if len(all_td) > 0:
            dataRow = []
            for item in all_td:
                dataRow.append(item.text)
            dataAll.extend([dataRow])
    return dataAll

def main():
    url = "https://www.bankofchina.com/sourcedb/whpj/"

    html = getHTML(url)
    # BeautifulSoup将字节流转换为utf-8编码
    soup = BeautifulSoup(html, 'lxml')
    Bankinfo = getBank(soup)
    wb = xw.Book()
    sht = wb.sheets('Sheet1')
    sht.range('a1').value = Bankinfo  # 将数据添加到表格中

    chart = sht.charts.add(500, 50, 700, 400)
    chart.set_source_data(sht.range('A1:A28,C1:C28,E1:E28'))  # 设置数据画图
    chart.chart_type = 'line_markers'

    chart.name = 'line_markersd'
    # chart.api[1].ChartTitle.Text='中国银行外汇牌价'
    #wb.close()

if __name__ == '__main__':
    main()
