# Consume one item
with cv:
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()
