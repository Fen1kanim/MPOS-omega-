import json

def takeANote(name):
    with open('./keywords/notes/notes.json', 'r') as js:
        notes = json.load(js)
    newNote = {"note" : input('take a note: ')}

    notes[name] = newNote

    with open('./keywords/notes/notes.json', 'w') as js:
        json.dump(notes, js, indent=4)
