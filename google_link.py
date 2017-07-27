import sys,bs4,requests,webbrowser
url='https://www.google.co.in/search?q='+' '.join(sys.argv[1:])
webbrowser.open(url) 
resp=requests.get(url)
soup_obj=bs4.BeautifulSoup(resp.text)
type(soup_obj)
