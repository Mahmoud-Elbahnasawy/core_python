import operator

def is_comment(item):
    return isinstance(item , str) and item.startswith("#")

program = list(reversed(("#this is comment 1",2 , 5 , operator.add , 3 , operator.mul )))

def execute(program):
    # any calculation envolves two numbers, old is used to either hold the value of the very first operand, or the accumulative results of 
    # the program
    old = None
    # new hold either the second item, or second operand
    new = None
    while program :
        # remove the an item and check if it was a comment to delete it.
        item = program.pop()
        # commnet are supposed to be at the first of the program only
        # if this item was not a comment the add it again to the program
        if not is_comment(item):
            program.append(item)
            break
    else : # nobreak happend
        print("We checke for each item in program, but found either comment or the program is empty")
        # get out of this empty program
        return
    while program :
        item = program.pop()
        if isinstance(item , int):
            # if you old was None, then this means that no items were added to it then assing the value of this item to it.
            if not old :
                old = item
            # if the old variable was not None then add the value of the second operand to the new variable
            else:
                new = item
        else :
            # if enterd here , then the item is either a function (intended) , or not a function (not intended neither handled)
            print("We made a calculation") 
            old = item(old , new)
            print(f"result of calculation is {old}")
    else :
        print("Finished Program!")


#if you notice that here we used the else clause to handle the failure of search (found no items in program) and this is the most
# widespread case of the while-else clause.

if __name__ == "__main__":
    execute(program)