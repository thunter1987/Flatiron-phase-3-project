#!/usr/bin/env python3

from simple_term_menu import TerminalMenu

class Cli():
    
    def start():
      options = ["Create new Patient", "Schedule Patient Next Appointment", "Exit" ]
      terminal_menu = TerminalMenu(options)
      menu_entry_index = terminal_menu.show()
      print(f"{options[menu_entry_index]}")
      
      if options[menu_entry_index] == "Exit":
        print("Thank You for using this database, Goodbye!")
        exit()
        
app=Cli
app.start()
    
