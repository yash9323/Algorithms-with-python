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

# Linear Search Algorithm 
def linear_search(arr,srch):
    a = len(arr)
    for i in range(a):
        if arr[i] == srch :
            print(f"{srch} found in the array at index {i+1} ")
            break
    if i == a - 1 :
        print(f"{srch} is not in the array !")

# Binary Search Algorithm 
def binary_search(arr,srch):
    mid = None
    start = 0 
    end = len(arr) - 1
    while start <= end :
        mid = (start + end ) // 2 
        if arr[mid] == srch :
            print("Element Found at :",mid + 1)
            break
        if srch > arr[mid] :
            start = mid + 1 
        if srch < arr[mid] :
            end = mid - 1  
    else :
        print(f"Element {srch} Not in Array !")      