def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    html=html.split()
    max1=""
    with open("words.txt","r") as my_document:

        my_document=my_document.read()
        for i in html:
            if len(i)>len(max1) and i in my_document :
                max1=i
        return max1
            
print( longest_word("https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet"))     
    
    
        