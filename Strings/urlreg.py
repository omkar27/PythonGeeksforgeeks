import re
url = 'https://google.com,https://abc.com,http://wxy.com'
regex = re.compile(r'https?://(www\.)?')
print list(regex.findall(url))
