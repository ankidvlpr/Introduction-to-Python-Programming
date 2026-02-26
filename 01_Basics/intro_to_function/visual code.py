# Please write a program which asks the user which editor they are using. The program should keep on asking until the user types in Visual Studio Code.

# Have a look at the example of expected behaviour below:

# Sample output
# Editor: Emacs
# not good
# Editor: Vim
# not good
# Editor: Word
# awful
# Editor: Atom
# not good
# Editor: Visual Studio Code
# an excellent choice!

# If the user types in Word or Notepad, the program counters with awful. Other unacceptable editor choices receive the reply not good.

# The program should be case-insensitive in its reactions. That is, the same user input in lowercase, uppercase or mixed case should trigger the same reaction:

# Sample output
# Editor: NOTEPAD
# awful
# Editor: viSUal STudiO cODe
# an excellent choice!



while True:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")

