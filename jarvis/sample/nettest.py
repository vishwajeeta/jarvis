from urllib import request

def checkInternet():
    try:
        request.urlopen("https://www.google.com",timeout=1)
        return True
    except:
        return False
print(checkInternet())