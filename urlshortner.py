import pyshorteners
long_url = input("Enter the URL to shorten: ")
 
#Bitly shortener service
type_bitly = pyshorteners.Shortener(api_key='1a4440740d005e4537380cdd50175a95f2248b50')
short_url = type_bitly.bitly.short(long_url)
 
print("The Shortened URL is: " + short_url)


# https://app.bitly.com/settings/api/  
# this link is used to generate API KEY