def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    html=set(html.split())
    maxi=""
    with open("words","r") as myfile:
        dic =set(myfile.read().split())
        for i in html:
            if len(i)>len(maxi) and i in dic :
                maxi=i
    return maxi
