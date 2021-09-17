import eyed3
from tkinter import Tk 
from tkinter.filedialog import askopenfilename
from appJar import gui
from shutil import copyfile

selected_filename = 'No file has been selected!'

def select_file():
    global selected_filename
    Tk().withdraw()
    selected_filename = askopenfilename()
    audiofile = eyed3.load(selected_filename)

    app.setLabel('file', 'selected file: ' + selected_filename[::-1].split('/', 1)[0][::-1])
    
    try:
        app.setLabel('song', 'Song Name: ' + audiofile.tag.title)
    except TypeError:
        app.setLabel('song', 'Song Name: ????')

    try:
        app.setLabel('artist', 'Artist(s) Name: ' + audiofile.tag.artist)
    except TypeError:
        app.setLabel('artist', 'Artist(s) Name: ????')

    app.enableButton('Submit')



def generate_new_name(name):
    return name[::-1].split('.', 1)[1][::-1] + '(modified).' + name[::-1].split('.', 1)[0][::-1]

def change_metadata(filename):
    audiofile = eyed3.load(filename)
    audiofile.tag.title = app.getEntry("New Song Name:")
    audiofile.tag.artist = app.getEntry("New Artist(s) Name:")
    audiofile.tag.save()

def press(button):
    global selected_filename
    print('s')
    if button == 'Submit':
        if not app.check("Create a new file"):
            change_metadata(selected_filename)
        else:
            new_file_name = generate_new_name(selected_filename)
            copyfile(selected_filename, new_file_name)
            change_metadata(new_file_name)
        

app = gui("Login Window", "400x200")

app.addButton("select", select_file)

app.addLabel("file", selected_filename)

app.addLabel("song", 'Song Name: -')
app.addLabel("artist", 'Artist(s) Name: -')


app.addLabelEntry("New Song Name:")
app.addLabelEntry("New Artist(s) Name:")

app.addCheckBox("Create a new file")

app.addButton("Submit", press)
app.disableButton('Submit')

app.go()
