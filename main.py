import os
import subprocess
import sys
import json
from Player import Player

def open_text_editor(exercise):
    editor = os.environ.get('EDITOR', 'vim')
    filename = exercise
    try:
        subprocess.run([editor, filename])
    except FileNotFoundError:
        print("The specified editor could not be found.")
        sys.exit(1)

def main():
    print(r"""\               
            ,:  ..;
             . ,;;%
            +;;%%%%%
             /- %,%%
             *   \ %%
              =  / \
              *-/ / \
                /\/.-.\
               |  |    |
               |  |   ||
               |  |   ||
           _.-----|   ||
          / \________,||
         |||/  |       |
         //    |       |
        //     |\      |
       //      | \     |
      //       |  \    |
     //        |   \   |
    //         |    \  |
   //          |    |\ |
  //           |    | \|
 //            \    \
c              |\    \
               | \    \
               |  \    \
               |. \    \
              _\    \.- \ 
             |___.-|__.\/
             """)
    with open("./savedata", 'r') as file:
        content = file.read()
        if content:
            print("Your face...yes, I remember you.")
            data = json.loads(content)
            player1 = Player(name=data["Name"], role=data["Role"])
        else:
            name = input("What's your name, kind sir?\n")
            role = input("And be you fighter, mage, or rogue?\n")
            player1 = Player(name, role)

    print(f"Your name is {player1.name} and your role is {player1.role}.")
    def exercise():  
        exerciseChoice = input("Which exercise would you like to complete? You can choose between 'Binary Search' and 'Write a list'\n")
        if exerciseChoice == 'Binary Search':
            player1.exp += 10
            open_text_editor('binary_search')
        elif exerciseChoice == 'Write a list':
            open_text_editor('write_a_list')
            print("A list you say?")
        else:
            print("I'm sorry, that's not an option here. Press Ctrl+C to quit, or answer the question.")
            exercise()
    exercise()
    print(player1.exp)

main()
