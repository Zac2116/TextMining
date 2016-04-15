def cleanTypo(word):
    if len(word) <= 2:
        return word
    else:
        isTypo = False
        index = 0
        char_list = list(word)
        three_chars = ngrams(char_list,3)
        for i in range(len(three_chars)):
            c1 = 'a' <= three_chars[i][0] <= 'z'
            c2 = 'A' <= three_chars[i][1] <= 'Z'
            c3 = 'a' <= three_chars[i][2] <= 'z'
            isTypo = isTypo or c1&c2&c3
            if isTypo:
                index = i+1
                cor_word = word[:index] + " " + word[index:]
                break

            else:
                cor_word = word


        return cor_word.split(" ")
