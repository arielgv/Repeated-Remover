"""
    This code uses a function called repeat_remover, which takes an interable, and return a 'newlist' 
    which will remove the repeated items of the given list. 
    Actually it doesnt remove anything. It just creates a new list checking every item if it exists or not in it.
"""

def repeat_remover(randomlist):
    newlist = []
    for element in randomlist:
        if element not in newlist:
            newlist.append(element)
    return newlist


def run():
    old_list = [1,1,3,4,4,6,6]
    #here we create a list of numbers, and use the function to return a new one without repeated items.
    nueva = repeat_remover(old_list)
    print(nueva)
    #This prints the list 1, 3 ,4, 6 

if __name__ == "__main__":
    run()
