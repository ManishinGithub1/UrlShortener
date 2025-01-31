import pyshorteners #importing the module pyshorteners

url=input("Enter the URL: \n")  #taking the URL as input


print("The URL after shortening:\n",pyshorteners.Shortener().tinyurl.short(url)) #shortening the URL using tinyurl