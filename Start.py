from Player import Player

class Events:
  def __init__(self):
    pass

  def start(self):
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
    name = input("What's your name, kind sir?\n")
    role = input("And be you fighter, mage, or rogue?\n")
    player1 = Player(name, role)
    def exercise(self):  
      exercise = input("Which exercise would you like to complete? You can choose between 'Binary Search' and 'Write a list'\n")
      if exercise == 'Binary Search':
        print("Binary? Wut?")
      elif exercise == 'Write a list':
        print("A list you say?")
      else:
        print("I'm sorry, that's not an option here. Press Ctrl+C to quit, or answer the damn question.")
        exercise()
    exercise()
