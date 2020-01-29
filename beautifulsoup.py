from bs4 import BeautifulSoup



#soup = BeautifulSoup(HTML)
#soup2 = soup.find_all("table")[0]
#tableDataText(soup2)
def tableDataText(table):       
    rows = []
    trs = table.find_all('tr')
    trs = trs[:11]
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')] # header row
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return rows

#creating empty dataframe with columns
list_df = pd.DataFrame(columns=('Store Name', 'Address','Info1'))
def beautifulscrape(html,list_df): 
    soup = BeautifulSoup(html)   
    store_name = soup.
    store_adress = soup.
    info1= soup.     
    #This is HOW TO APPEND LİST as ROW into Pandas Dataframe
    list_df.loc[len(list_df)] = [store_name, store_adress, info1]
    return list_df

#Selenium
for city in LISTNAME:  #change according to your listname
    browser.get("WEBSİTE LINK") 
    time.sleep(3) #wait for website to open
    #Get element to you will enter City and click
    searcher =browser.find_element_by_xpath("XPATH").click()   
    searcher.send_keys(city)
    #how to press enter ====> searcher.send_keys(Keys.ENTER) #enter
    xpath = "XPATH".format(city)  #bonus
    element= browser.find_element_by_xpath(xpath).click()  
    storelist_html = browser.find_element_by_xpath("XPATH").get_attribute('outerHTML')#getouterhtml of element that involves storeinformation.
    beautifulscrape(storelist_html,list_df)     ####.....SCRAPE-BeautifulSoup4.....#####
    print("LETS GOOO")
