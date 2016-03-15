from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
#driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT)
driver.implicitly_wait(10)

def getBalances(user,password,userdefs):
    driver.get("https://customer.pagepluscellular.com/my-account/my-account-summary.aspx")
    #login
    elem = driver.find_element_by_name("username")
    elem.send_keys(user)
    elem2 = driver.find_element_by_name("password") #obscure passwords...
    elem2.send_keys(password)
    elem2.send_keys(Keys.RETURN)
    
    #for each user...
    i=1
    for u in userdefs:#range(1,usercount+1):
        print i," ",u,":"
        driver.find_element_by_xpath('//*[@id="ContentPlaceHolderDefault_mainContentArea_Item2_My Account Summary_4_Registred1_DrpAccounts"]/option['+str(i)+']').click()
        #time.sleep(15)   #wait for item.. extra long for selserver
    
        #get balance
        balance = driver.find_element_by_xpath('//*[@id="ContentPlaceHolderDefault_mainContentArea_Item2_My Account Summary_4_Registred1_lblBalance"]').text
        #get expiration date
        v = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolderDefault_mainContentArea_Item2_My Account Summary_4_Registred1_divBundleDetails"]')
        for j in v:
            print j.text
            
        print balance,
        if float(balance[1:]) < 30: 
            print "Underblanced",
            #fund account with ($50)
                #pageplusdirect driver...
                    #chase checking driver..
            #store balances in spreadsheet
        print
        i+=1

    #exit/logout
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolderDefault_TopNav_1_lnkLogout"]').click()
    
    time.sleep(2)

#todo:
    #send 2d list of names,balance thresholds, account refunding value, spreadsheet store cell,phone number
        # could parse many of these out if desired...
    
user = ["UserName"] #account user name
getBalances('account_login_id','password',user)

#user = ["UserName1","Username2"]
#getBalances('2nd account_id','password',user)

driver.quit()
#driver.close() #hangs for some reason...