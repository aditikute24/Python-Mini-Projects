import pyshorteners
url=input("Enter the url:")
shortner=pyshorteners.Shortener()
a=shortner.tinyurl.short(url)
print(a)











#pip install pyshorteners