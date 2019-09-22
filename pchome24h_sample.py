import requests #先引用requests
import time

#目標網址為：https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=關鍵字
#請求範例：https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E8%97%8D%E8%8A%BD%E9%9F%B3%E9%9F%BF&page=1&sort=sale/dc

#建構網址
keyword = "藍芽音響"
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q="+keyword+"&page=1&sort=sale/dc"

#嘗試請求
rs = requests.get(url=url)

#輸出結果
data = rs.text
print(data)

import json #引用json函式

json_data = json.loads(data)
page_max = json_data['totalPage'] #取得所有頁數

all_items = [] #先宣告一個 所有商品的保存陣列




for n in range(page_max): #針對頁數做一個迴圈
    page_num = n + 1 #因為 頁碼會從0開始計算
    if page_num > 20: #只爬到第20頁就停止，本次教學 不含換ip教學 所以先這樣
        break

    # 建構網址
    #將頁碼與字串合併，因為 頁數為 整數int型別，所以要括一個format來進行轉換
    url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + keyword + "&page="+format(page_num)+"&sort=sale/dc"
    # 嘗試請求
    rs = requests.get(url=url)
    # 輸出結果
    data = rs.text
    try:#做一個例外處理，如果出現錯誤可以避免卡住
        page_data = json.loads(data)#轉換json格式
        products = page_data['prods']#取得商品列表
        for pro in products:
            all_items.append(pro)#將商品保存進商品陣列
        # print(data)
        print("目前進度頁數 {}/{} 已保存：{}個商品".format(page_num,page_max,len(all_items)))#字串整合的應用
    except Exception as e: #輸出的錯誤名稱叫e
        print(e) #印出錯誤內容
        print(data) #印出這一頁所抓取的值

    time.sleep(1)#記得要休息一秒再抓取，不然會被封ip

#保存結果
all_items_json = json.dumps(all_items) #將資料轉為json格式字串
fp = open("result.txt",'w',encoding="utf-8")#建立檔案
fp.write(all_items_json)#寫入
fp.close()#關閉檔案
