def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    with open("words") as f:
        content = f.readlines()
        content = [s.strip() for s in content]
        words_url = set(html.split())
        words_dict = set(content)
        words = words_url.intersection(words_dict)
        max_len = len(max(words, key=len))
        word = [w for w in words if len(w) == max_len]
        return sorted(word)[0]
