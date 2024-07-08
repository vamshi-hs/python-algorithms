def naive_search(haystack,needle):
    i = 0
    j = 0
    temp_i = None
    haystack_len = len(haystack)
    needle_len = len(needle)
    while i < haystack_len and j < needle_len:
        if haystack[i] == needle[j]:
            temp_i = i
            i += 1
            j += 1
            while(j < needle_len and i < haystack_len):
                if haystack[i] != needle[j]:
                    j = 0
                    break
                j += 1
                i += 1
            if j == needle_len:
                return temp_i
            i = temp_i + 1
            continue
        i += 1
    return -1
         
def test_search_naive():
    assert naive_search("abcab","bc") == 1, "Should be 1"
    assert naive_search("aaaaab","aab") == 3, "Should be 3"
    assert naive_search("aaaaab","bab") == -1, "Should be -1"
    assert naive_search("emacs","rgv") == -1, "Should be -1"
    assert naive_search("","rgv") == -1, "Should be -1"
    assert naive_search("rgv","rgv") == 0, "Should be 0"
    assert naive_search("rgv","") == -1, "Should be 0"
    assert naive_search("","") == -1, "Should be 0"
    
if __name__==  "__main__":
    test_search_naive()
    print("Naive search test passed")
