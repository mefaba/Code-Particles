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
