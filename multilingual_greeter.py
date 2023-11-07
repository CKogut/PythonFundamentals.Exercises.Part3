"""Prints a greeting"""
def greet(name, lang):
    if lang == 1:
        print("Hello there, " + name)
    elif lang == 2:
        print("Hola, " + name)
    elif lang == 3:
        print("Guten tag, " + name)
    else:
        print("Not supported")

"""Prompts user for name"""
def name_input():
   return input("Enter name: ")
   
"""Prompts user to select a language"""
def language_input():
    print("Enter a number to select a language")
    print("1. English")
    print("2. Spanish")
    print("3. German")
    return int(input())


"""Pass name_input to greet"""
greet(name_input(),language_input())

