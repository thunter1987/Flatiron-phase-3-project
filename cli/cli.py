from simple_term_menu import TerminalMenu

def start():
    options = ["Create new Patient", "Schedule Patient Next Appointment", "Exit" ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"{options[menu_entry_index]}")
    
if __name__ == '__main__':
    start()