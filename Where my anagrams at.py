def anagrams(word, words):
    result = []

    word_unique = list(set(word))
    word_count = []
    for i in range(len(word_unique)):
        word_count.append(list(word).count(word_unique[i]))

    dict = {}
    for i in range(len(word_unique)):
        dict[word_unique[i]] = word_count[i]

    for w in words:
        words_unique = list(set(w))
        words_count = []
        for i in range(len(words_unique)):
            words_count.append(list(w).count(words_unique[i]))

        dict_w = {}
        for i in range(len(words_unique)):
            dict_w[words_unique[i]] = words_count[i]

        if dict == dict_w:
            result.append(w)
        
    return result
