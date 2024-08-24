from urllib.request import urlopen

page=urlopen("https://aditikute24.github.io")

sourcecode=page.read()
print(sourcecode)