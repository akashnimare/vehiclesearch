import mechanize
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import json
num = raw_input("Enter the registration number: ")
url = "http://mis.mptransport.org/MPLogin/eSewa/VehicleSearch.aspx"
br = mechanize.Browser()
br.set_handle_robots(False)
br.open(url)
br.select_form(name='aspnetForm')
br["ctl00$ContentPlaceHolder1$txtRegNo"] =(num)
res = br.submit()
content = res.read()
soup=BeautifulSoup(content)
table = soup.find("table", {"border":"1","id":"ctl00_ContentPlaceHolder1_grvSearchSummary"})
for row in table.findAll('tr',{'class':'GridItem'}):
	col = row.findAll('td')
	a=col[14].string
	b=col[5].string
	c=col[6].string
	d=col[8].string
	with open("result.json", "w") as outfile:
		json.dump({'Model':a, 
				   'Owner Name':b, 
				   'RTO NAME':c, 
				   'Regi. Date':d
				   }, outfile, indent=4)
	
    
