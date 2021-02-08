from time import sleep

from selenium import webdriver

import xlrd

class Read_Ex():
    def read_excel(self,filepath):
        #打开excel表，填写路径
        book = xlrd.open_workbook(filepath)
        # book = xlrd.open_workbook(r"E:\hugewarts\web_auto\comment\sheel.xls")
        #找到sheet页
        table = book.sheet_by_name("Sheet1")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        s =[]
        key =table.row_values(0)# 这是第一行数据，作为字典的key值

        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d ={}
                values = table.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                s.append(d)
            return s





if __name__ == '__main__':

    r = Read_Ex()
    filepath = r"E:\pythonstudy\qiang_gou\grade_one.xls"
    s=r.read_excel(filepath)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://245314.yichafen.com/public/queryscore/sqcode/MsTcIn4mOTQxOHw0NjIxNDMzYWYwMWNiMWEzZmU2YWQ5ODRhMzAwZDFjMXwyNDUzMTQO0O0O.html')
    subject=[]
    for i in s:
        print(i)
        driver.find_element_by_name('s_kaohao').send_keys(i["准考证号"])
        driver.find_element_by_name('s_xingming').send_keys(i["姓名"])
        driver.find_element_by_css_selector('[type="button"]').click()
        eles = driver.find_elements_by_css_selector('.case tr:nth-child(1) th')
        for ele in eles:
            subject.append(ele.text)
        eles =driver.find_elements_by_css_selector('.case tr:nth-child(2) td')
        for i,ele in enumerate(eles):
            print(f"{subject[i]}:{ele.text}")
        driver.find_element_by_link_text('返回').click()
        sleep(1)