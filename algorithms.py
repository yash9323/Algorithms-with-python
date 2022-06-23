# Returns a list of all the anagrams in the string ! 
def anagram(st):
    l = st.split(" ")
    d = {}
    for word in l:
        sorted_word = ""
        for yo in sorted(word):
            sorted_word+=yo
        if sorted_word in d:
            d[sorted_word].append(word)
        else:
            d[sorted_word] = [word]
    return list(d.values())
