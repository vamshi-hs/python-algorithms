def linear_search(elements,key):
    index = 0
    for element in elements:
        if key == element:
            return index 
        index += 1
    return -1

def test_lsearch():
    assert linear_search([1,2,3,4,5,6],1) == 0, "Should be 0"
    assert linear_search([1,2,3,4,5,6],6) == 5, "Should be 5"
    assert linear_search([],1) == -1, "Should be -1"

if __name__==  "__main__":
    test_lsearch()
    print("Linear search passed")