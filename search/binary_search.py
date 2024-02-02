def binary_search(elements,key):
    if not elements:
        return -1
    low = 0
    high = len(elements) 
    while low <= high:
        mid = int(low + (high - low) / 2)
        if elements[mid] == key:
            return mid
        elif key > elements[mid] :
            low = mid + 1
        else:
            high = mid - 1
    return -1

def test_bsearch():
    assert binary_search([1,2,3,4,5,6],1) == 0, "Should be 0"
    assert binary_search([1,2,3,4,5,6],6) == 5, "Should be 5"
    assert binary_search([],1) == -1, "Should be -1"

if __name__==  "__main__":
    test_bsearch()
    print("Binary search passed")