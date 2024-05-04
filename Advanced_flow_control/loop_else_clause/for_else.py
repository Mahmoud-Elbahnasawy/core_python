# problem 
# Ensure that a list of integers contains at least one integer divisible by a specific value
# if no item was found then add the divisble itself to the list of ints 

def ensure(list_ints :list  , divisble):
    for int in list_ints:
        if int % divisble == 0 and int != 0:
            print(f"Item {int} is divisble by {divisble}")
            return int
        
    else : # case of no_break or no return.
        list_ints.append(divisble)
        print(f"We found no item divisble by {divisble}, but we added the {divisble} to the list to become {list_ints}")
        return list_ints
    
def ensure_refactored(list_ints :list  , divisble):
    for int in list_ints:
        if int % divisble == 0 and int != 0:
            print(f"Item {int} is divisble by {divisble}")
            return int
        
    list_ints.append(divisble)
    print(f"We found no item divisble by {divisble}, but we added the {divisble} to the list to become {list_ints}")
    return list_ints

if __name__ == "__main__":
    list_ints=list(range(0,254,17))
    divisble_value = 15
    ensure(list_ints , divisble_value)