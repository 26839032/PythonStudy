def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        else:
            print("found the key")


