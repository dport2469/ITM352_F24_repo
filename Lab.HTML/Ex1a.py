import urllib.request
import ssl

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

ssl._create_default_https_context = ssl._create_unverified_context
web_page = urllib.request.urlopen(url)

for line in web_page:
    html_line = line.decode('utf-8')
    if '<title>' in html_line:
        print(html_line)