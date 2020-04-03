# This function finds out if the user said "music", "heating", etc.

def find_item(utterance, rasa_output):
    item = "" # This is the variable that will hold the item
    split_uttrerance = utterance.split(" ") # Split the user's input
    split_rasa_output = " ".join(rasa_output.split("?")).split(" ") # Split Rasa's output

    items = [item for item in split_rasa_output if item == "music" 
            or item == "heating" or item == "tv" or item == "light"] # Identify the relevant items from Rasa's output

    # Identifies the item to be chosen from the user input
    if ("music" in split_uttrerance):
        item = "music"
    elif ("tv" in split_uttrerance or "television" in split_uttrerance or "telly" in split_uttrerance):
        item = "tv"
    elif ("heating" in split_uttrerance):
        item = "heating"
        print(item)
    elif ("lights" in split_uttrerance or "light" in split_uttrerance):
        item = "lights"
    elif ("first" in split_uttrerance): 
        item = items[0]
    elif ("second" in split_uttrerance): 
        item = items[1]
    elif ("third" in split_uttrerance): 
        item = items[2]
    else:
        return None

    return item