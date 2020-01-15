'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''
from urllib.parse import urlparse


def domain_name(url):
    print(url)
    res = urlparse(url).netloc
    if res == '':
        res = url.split('.')
        if res[0] == 'www':
            return res[1]
        else:
            return res[0]
    if res.split('.')[0] == 'www':
        return res.split('.')[1]
    return res.split('.')[0]



# other's solution 1
def domain_name_1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

# other's solution 2
import re
def domain_name_2(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')



domain_name("http://google.com")
domain_name("http://google.co.jp")
domain_name("www.xakep.ru")
domain_name("https://youtube.com")