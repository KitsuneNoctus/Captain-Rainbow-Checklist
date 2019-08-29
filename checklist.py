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
        print(index + list_item)
        index += 1

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
