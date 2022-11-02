# a notes app made by arihtich
# how to use:
#   run .py file

class note:
    def __init__(self):
        #staring message for new users
        print('''
NOTETAKER!
type the letter 'n' to make a new note
type the letter 'w' to write to a file
type the letter 'q' to quit
''')
        filename = input("name of file: ")
        f = open(filename + ".txt", 'w')
        while True:
            prompt = input(": ")
            

            if (prompt == 'n'):
                note = input("take note: ")
                f.write(note + '\n')

            if (prompt == 'w'):
                print("saving...")
                f.close()
                print("closing notetaker")
                break

            if (prompt == 'q'):
                print("quitting...")
                break

run = note()

