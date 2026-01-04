import json

def ask4notes(name):
    with open('./keywords/notes/notes.json', 'r') as js:
        notes = json.load(js)

    if name in notes:
        print(f"your last note were: \"{notes[name]["note"]}\"")
    else:
        print('U hav no notes')



