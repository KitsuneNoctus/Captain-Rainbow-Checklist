"""hi."""
checklist = list()


# CREATE
def create(item):
    """Adding items to the list created."""
    checklist.append(item)


# Read
def read(index):
    """Gets element from the list."""
    return checklist[index]


# UPDATE
def update(index, item):
    """Updates items in list."""
    checklist[index] = item


# Destroy
def destroy(index):
    """Remove elements from list"""
    checklist.pop(index)


def list_all_items():
    """Lists all items."""
    index = 0
    for list_item in checklist:
        #print(str(index) + list_item)
        #below is the proper way to format the line
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    #add code
    #https://www.geeksforgeeks.org/print-colors-python-terminal/
    #Checkout later for the stretch goal

    checklist[index] = "%s %s"%("√",checklist[index])



def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

# Test
def test():
    """Testing code above"""
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

# def test2():
#     create("purple sox")
#     create("red cloak")
#
#     mark_completed(0)
#     print(checklist)

test()

# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)
#
# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)
#
# checklist = ['Blue', 'Cats']
# checklist.pop(1)
# print(checklist)
