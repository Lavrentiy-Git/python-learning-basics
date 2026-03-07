def count_vowels(q): # количество гласных в слове
    S = 0
    q = q.lower()
    for i in range(0, len(q)):
        if q[i] in ["а", "е", "у", "ы", "о", "э", "я", "и"]:
            S += 1
    return S
def merge_lists(list1, list2): # отсортиролванное объединение двух списков
    list1 += list2
    list1.sort()
    return list1
if __name__ == "__main__":
    print(count_vowels("Азбука"))
    print(merge_lists([1, 4, 7], [2, 3, 5, 6]))

