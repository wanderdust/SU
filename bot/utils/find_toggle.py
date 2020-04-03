# This function finds out if user wants something "on" or "off"

def find_toggle(utterance):
    toggle = "off" #default
    split_uttrerance = utterance.split(" ")

    if ("on" in split_uttrerance):
        toggle ="on"

    return toggle