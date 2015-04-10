import urllib.request
import os
url_page = input('Select your web page: ')
domain_name = url_page.partition('.')[0]
if 'https://' not in url_page : url_page = 'https://%s' % url_page
req = urllib.request.Request(url_page)
response = urllib.request.urlopen(req)
the_page = response.read()
if not os.path.exists(domain_name):
	os.makedirs(domain_name)
output = open(domain_name + '\\' + domain_name + '.html','wb')
output.write(the_page)
output.close()