import sys,bs4,requests,webbrowser,re
url='https://www.google.co.in/search?q='+' '.join(sys.argv[1:])
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
webbrowser.open(url) 
resp=requests.get(url,headers=headers)
soup_obj=bs4.BeautifulSoup(resp.text)
#print('RESP',resp.text)
#type(soup_obj)
links=soup_obj.select('.r a')
for link in links:
    webbrowser.open(link.get('href'))
    #print(res.group())
