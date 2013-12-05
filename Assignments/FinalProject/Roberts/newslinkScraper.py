import mechanize
import cookielib
from bs4 import BeautifulSoup

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open("https://newsarchive.nebpress.com/full_page_list.html")
br.form = list(br.forms())[0]

control1 = br.form.find_control("search_text")
control2 = br.form.find_control("start_date")
control3 = br.form.find_control("end_date")
control4 = br.form.find_control("publication_filter")

control1.value = "ALLY PHILLIPS Nebraska News Service"
control2.value = "10/20/2013"
control3.value = "10/31/2013"
control4.value = ["163"]

response = br.submit()

soup = BeautifulSoup(response)
text = soup.find_all('p')

for t in text:
	for child in t.children:
		if control1.value in child:
			print t