# This function finds out if the user said "music", "heating", etc.

from speech_handlers.tts import tts

def find_item(utterance):
    item = ""
    split_uttrerance = utterance.split(" ")
    print(split_uttrerance)
    if ("music" in split_uttrerance):
        item = "music"
    elif ("tv" in split_uttrerance):
        item = "tv"
    elif ("heating" in split_uttrerance):
        item = "heating"
        print(item)
    elif ("lights" in split_uttrerance or "light" in split_uttrerance):
        item = "lights"
    else:
        # Returns bot saying "Sorry I didnt get that"
        tts(None, empty=True) # Text to speech "Sorry I didn't get that"
        return

    return item