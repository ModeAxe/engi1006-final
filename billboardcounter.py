def count(word):
    word = word.lower()
    allLyrics = open("words.txt", "r", encoding="utf-8").read().lower()
    num = allLyrics.count(word)
    return num