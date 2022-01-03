from anagram import is_anagram1, is_anagram2,normalize

def test_is_anagram1():
    assert is_anagram1("listen","silent") == True
    assert is_anagram1("A gentleman","Elegant man") == True
    assert is_anagram1("Clint Eastwood","Old west action") == True
    assert is_anagram1("dormitory","dirty room") == True


def test_is_anagram2():
    assert is_anagram2("listen","silent") == True
    assert is_anagram2("A gentleman","Elegant man") == True
    assert is_anagram2("Clint Eastwood","Old west action") == True
    assert is_anagram2("dormitory","dirty room") == True


def test_normalize():
    word1 = "silent"
    word2 = ""
    for word in word1.split():
        word2 += word
    assert normalize(word1) == word2.lower()
    word1 = "A gentleman"
    word2 = ""
    for word in word1.split():
        word2 += word
    assert normalize(word1) == word2.lower()
    word1 = "Clint Eastwood"
    word2 = ""
    for word in word1.split():
        word2 += word
    assert normalize(word1) == word2.lower()