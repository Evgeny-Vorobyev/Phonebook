main_menu = '''Head menu
    1. Open file
    2. Save file
    3. Show all contacts
    4. Create new contact
    5. Find contact
    6. Edit contact
    7. Delete contact
    8. Exit
    '''

menu_choice = 'Select menu item: '
input_error = 'Incorrect input. Enter from 1 to 8'
book_error = 'Phonebook is clear or file do not open'

open_successful = 'Phonebook is successfully opened'


input_new_contact = 'Enter new contact'
new_contact = ['Enter name contact: ', 'Enter phone: ', 'Enter comment: ']
search_word = 'Enter search: '
input_index = 'Enter index changeable contact: '
input_change_contact = 'Enter data changeable contact or Enter? To leave unchangeable: '

def contact_saved(name: str):
    return f'Contact {name} successfully saved'

def contact_changed(name: str):
    return f'Contact {name} successfully changed'