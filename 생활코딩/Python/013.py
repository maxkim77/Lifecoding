#!/user/local/bin/python3
print("Content-type: text/html")
print()
import cgi,os
files = os.listdir('data')
liststr =""
for item in files:
    liststr = liststr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    