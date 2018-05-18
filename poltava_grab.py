from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
s="http://vpoltave.info/tag/%D1%81%D0%B2%D1%96%D1%82%D0%BB%D0%BE/page"
xs="/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/a["
i=2
j=1

f = open('poltava2.csv', 'w')
f.write("\"date\";\"time\";\"adress\"\n")

while i<6:
    s1=s+str(i)
    driver.get(s1)
    while j<11:

        xs1=xs+str(j)+"]"
        driver.find_element_by_xpath(xs1).click()
        try:
            
            darkDate = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[1]").text
            darkTime = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[2]").text
            
            darkAdress = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[3]").text
            path = "//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr["
            darkAdress1 = driver.find_element_by_xpath("//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr[1]/td[4]").text
            if (darkAdress1.find(','))!=-1:
                if (darkAdress1.find(';'))!=-1:
                    addr=list(darkAdress1.split(";"))
                else:
                    addr=list(darkAdress1.split(","))
            else:
                addr=['']
                addr[0]=darkAdress1
            for a in addr:
                if (a.find(".")!=-1):
                    f.write(darkDate+"; "+darkTime+ "; " +darkAdress+", "+a+"\n")
                else:
                    f.write (darkDate+"; "+darkTime+ "; " +darkAdress+", вул."+a+"\n")
        except NoSuchElementException:
                continue
        
        k=2
        while 1:
            try:
                path = "//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr["
                path += str(k)
                path += "]/td[2]"
                darkAdress = driver.find_element_by_xpath(path).text
                path = "//div[@class='content_wrapper ng-scope']//div[4]/table[1]/tbody[1]/tr["
                path += str(k)
                path += "]/td[3]"
                darkAdress1 = driver.find_element_by_xpath(path).text
                if (darkAdress1.find(','))!=-1:
                    if (darkAdress1.find(';'))!=-1:
                        addr=list(darkAdress1.split(";"))
                    else:
                        addr=list(darkAdress1.split(","))
                else:
                    addr=['']
                    addr[0]=darkAdress1
                for a in addr:
                    if (a.find(".")!=-1):
                        f.write(darkDate+"; "+darkTime+ "; " +darkAdress+", "+a+"\n")
                    else:
                        f.write (darkDate+"; "+darkTime+ "; " +darkAdress+", вул."+a+"\n")
                k+=1
            except NoSuchElementException:
                break
        j+=1
        driver.back()
    j=1
    i+=1

driver.close()
f.close()
