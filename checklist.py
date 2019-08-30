"""hi."""
checklist = list()


# CREATE
def create(item):
    """Adding items to the list created."""
    checklist.append(item)


# Read
def read(index):
    """Gets element from the list."""
    try:
        return checklist[index]
    except IndexError:
        print("Index not within current list.")


# UPDATE
def update(index, item):
    """Updates items in list."""
    try:
        checklist[index] = item
    except IndexError:
        print("Outside the inedx range of the list. Try again.")


# Destroy
def destroy(index):
    """Remove elements from list"""
    try:
        checklist.pop(index)
    except IndexError:
        print("That Index does not exist.")


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

    #recieved help from tutor
    checklist[index] = "%s %s"%("√",checklist[index])


#Select Function ---------------
def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number?: ")
        item_index = int(item_index)
        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    elif function_code == "U" or function_code == "u":
        try:
            item_index = user_input("Index Number?: ")
            item_index = int(item_index)
            print(read(item_index))
            item_update = user_input("Update to Item?: ")
            
            # Remember that item_index must actually exist or our program will crash.
            update(item_index, item_update)
        except ValueError:
            print("Enter What is Asked.")
        except IndexError:
            print("Not an Index in current list")

    elif function_code == "D" or function_code == "d":
        try:
            item_index = int(user_input("Index Number to Delete item?: "))
            destroy(item_index)
        except ValueError:
            print("Inccorect Input. Use Number.")

    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "Q" or function_code == "q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
#--------------------------------------------------------------------
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

    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    user_value = user_input("Please Enter a value:")
    print(user_value)

# test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, U to update item in list, D to delete item in list, P to display list, and Q to quit: ")
    running = select(selection)
# def test2():
#     create("purple sox")
#     create("red cloak")
#
#     mark_completed(0)
#     print(checklist)

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
