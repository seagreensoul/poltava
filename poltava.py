# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:47:19 2018

@author: admin
"""


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("http://vpoltave.info/tag/%D1%81%D0%B2%D1%96%D1%82%D0%BB%D0%BE")
driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/a[9]").click()

f = open('poltava.csv', 'w')
f.write("\"date\";\"time\";\"adress\"\n")

darkDate = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[1]").text
darkTime = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[2]").text

darkAdress = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[3]").text
path = "//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr["
darkAdress1 = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[4]").text
if (darkAdress1.find(','))!=-1:
    addr=list(darkAdress1.split(","))
else:
    addr=['']
    addr[0]=darkAdress1
for a in addr:
    if (a.find(".")!=-1):
        f.write(darkDate+"; "+darkTime+ "; " +darkAdress+", "+a+"\n")
    else:
        f.write (darkDate+"; "+darkTime+ "; " +darkAdress+", вул."+a+"\n")


i=2
while 1:
    try:
        path = "//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr["
        path += str(i)
        path += "]/td[2]"
        darkAdress = driver.find_element_by_xpath(path).text
        path = "//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr["
        path += str(i)
        path += "]/td[3]"
        darkAdress1 = driver.find_element_by_xpath(path).text
        if (darkAdress1.find(','))!=-1:
            addr=list(darkAdress1.split(","))
        else:
            addr=['']
            addr[0]=darkAdress1
        for a in addr:
            if (a.find(".")!=-1):
                f.write(darkDate+"; "+darkTime+ "; " +darkAdress+", "+a)
            else:
                f.write (darkDate+"; "+darkTime+ "; " +darkAdress+", вул."+a)
        i+=1
    except NoSuchElementException:
        break
    
f.close()
driver.back()
driver.close()