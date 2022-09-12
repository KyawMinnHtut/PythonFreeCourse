#Regular Expression
#[0-9],  [a-z],   [A-Z]
import re
#[]
my_str = "fool123bar"
print("Search ", re.search('[0-9][0-9][0-9]', my_str))
print("Search ", re.search('[0-9][0-9][0-9]', "kyawminhtut456"))
print("Search ", re.search('[0-9][0-9][0-9]', "123hello456"))

print("Search ", re.search('[abc]', my_str))

print("Search ", re.search('[1357][1357][1357]', "hello553"))
print("Search ", re.search('[1357][1357][1357]', "hello5253"))
print("Search ", re.search('[a-z][1357][1357]', "hello553asd135"))
# .
print("Search ", re.search('1.3', "1a3"))
print("Search ", re.search('1.3', "13a"))
# ^-
print("Search ", re.search('^Java', "Javascript"))
print("Search ", re.search('^Java', "Java"))
print("Search ", re.search('^Java', " Javascript"))
# -$
print("Search ", re.search('Java$', "Programming in Java"))
print("Search ", re.search('Java$', "Programming in JavaScript"))
# *
print("Search ", re.search('[a-z]*[1-5]*', "Program123ee"))
print("Search ", re.search('[a-z]*[1-5]*', "123ee"))
print("Search ", re.search('[a-z]*[1-5]*', ""))
# +
print("Search ", re.search('[a-z]+[1-5]+', "Program123ee"))
print("Search ", re.search('[a-z]+[1-5]+', "Program"))
# ? 
print("Search ", re.search('[a-z]+[1-5]?', "program123ee"))
print("Search ", re.search('[a-z]+[1-5]?', "program"))
# {}
print("Search ", re.search('[0-9]{5}', "0123456789"))
print("Search ", re.search('[0-9]{2,7}', "0123456789"))
# \
print("Search ", re.search('[a-z]*\.py', "hello.py"))
print("Search ", re.search('[a-z]*\.py', "hello"))
# | and ()
print("Search ", re.search('[a-z]{3,}\.(com|org|gov)', "hello.com"))
print("Search ", re.search('[a-z]{3,}\.(com|org|gov)', "hello"))
# \w and \W
print("Search ", re.search('\w+', "hello_123!@#$%"))
print("Search ", re.search('\W+', "hello_123!@#$%"))
# \d and \D
print("Search ", re.search('\d{9,11}', "09999888777"))
print("Search ", re.search('\D+', "12345asdcg@#$$"))
# \s and \S
print("Search ", re.search('\s*hello', "Hi  hello"))
print("Search ", re.search('\S*hello', "Hi  hello"))
# \b
print("Search ", re.search(r'\bHello', "Hello World"))

# grouping
m = re.search('([a-z]*)\.py', 'hello.py')
print(m.groups())

m = re.search('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com")
print(m.groups()[1])

m = re.match('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com")
print("Match start ", m.start(), " end ", m.end())

m = re.fullmatch('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com")
print("Full match " , m)

lst = re.findall('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com")
for item in lst:
    print("Match ", item)

lst = re.finditer('(http|https)://(www\.\w+\.(com|org|gov))', "http://www.google.com")
for item in lst:
    print("Match ", item)

replaced = re.sub('(http|https)://(www\.\w+\.(com|org|gov))',"domain", "http://www.google.com")
print(replaced)
replaced = re.subn('(http|https)://(www\.\w+\.(com|org|gov))',"domain", "http://www.google.com")
print(replaced)

#Web Scraping
# import urllib
# import urllib.request
# import urllib.request
# web_url = "http://www.google.com"
# u = urllib.request.urlopen(web_url)
# text = str(u.read())
# # print("Text ", text)
# title = re.findall("<title>.*</title>", text)
# print("Title ==> ", title)

# #BeautifulSoup
# import requests
# from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)