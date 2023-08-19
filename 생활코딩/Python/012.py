#!/user/local/bin/python3
print("Content-Type:text/html")
print()
import cgi,os

files = os.listdir('data')
 listStr = listStr + '<li><a href="">{name}</a></li>'

form = cgi.FieldStorage()

if 'id' in form:
 pageId = form["id"].value
 description = open('data/'+pageId, 'r').read()
else:
 pageId = 'Welcome'
 description ='Hello, web'
 printprint('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))