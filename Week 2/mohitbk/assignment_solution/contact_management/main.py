from typing import Any

def add_contact(name: str, email: str, phone: int) -> bool:
    with open('contact.txt','a') as file:
        file.write(','.join((name,email,str(phone))))
        file.write('\n')
        return True
    return False

def find_contact(username: str) -> list:
    with open('contact.txt','r') as file:
        contents = file.read().split('\n')
        contents = [i.split(',') for i in contents][:-1]

        res =[]
        for name,email,phone in contents:
            if name.lower() == username.lower():
                res.append((name,email,phone))
        return res

def update_contact(old_details: tuple, new_details: tuple):
    '''
    This functions updates the given contact:
    Args:
        old_details: tuple containing name, email, phone of the existing data
        new_details: tuple containing name, email, phone of the new data that should replace the existing data
    Returns:
        do anything you want but make it functional.
    '''

    with open('contact.txt','r') as file:
        content = file.read().split('\n')[:-1]
        content = [i.split(',') for i in content]
        to_update_contact_index = [i for i,c in enumerate(content) if content[i][1]==old_details[1]][0]
        content[to_update_contact_index][0] = new_details[0]
        content[to_update_contact_index][1] = new_details[1]
        content[to_update_contact_index][2] = str(new_details[2])
        with open('contact.txt','w') as f:
            output = [','.join(i) for i in content]
            f.writelines('\n'.join(output))
            f.write('\n')
            return True

def delete_contact(email: str):
    # same as update contact but instead of editing the list in the particular index you just delete the given index.
    with open('contact.txt','r') as file:
        content = file.read().split('\n')[:-1]
        content = [i.split(',') for i in content]
        to_delete_contact_index = [i for i,c in enumerate(content) if content[i][1]==email][0]
        content.pop(to_delete_contact_index)
        with open('contact.txt','w') as f:
            output = [','.join(i) for i in content]
            f.writelines('\n'.join(output))
            f.write('\n')
            return True
        

def import_contacts(filename) -> bool:
    try:
        file = open(filename,'r').readlines()
        with open('contact.txt','a') as contacts:
            for items in file:
                contact_details = items.split(',')
                contacts.write(','.join(contact_details))
            contacts.write('\n')
            return True
    except Exception as e:
        print('CANNOT OPEN GIVEN FILE')
        return False

def print_all():
    print('PRINTING ALL CONTACTS')
    try:
        contacts = open('contact.txt','r').readlines()
        for i, contact in enumerate(contacts):
            contact = contact.split(',')
            print(f'Contact No. {i}')
            print(f'Name: {contact[0]}')
            print(f'Email: {contact[1]}')
            print(f'Phone: {contact[2]} \n')
    except Exception as e:
        print('No Contacts found.. INVALID FILE PATH. Please change the Relative path of the file in code to run it in windows properly')

def check_int_type(inp: Any) -> int:
    '''
    Helper function:
    Converts the given input to integer if possible if, else returns exception.
    Parameter: inp -> input
    Returns inp as int or exception
    '''

    try:
        inp = int(inp)
        return inp
    except Exception as exception:
        print('\n'+'#'*100)
        print('Conversion Error. The following exception was thrown: ' + str(exception))
        print("Invalid option, please only enter integers and kindly omit other details. Restarting the program....")
        print('#'*100+'\n')
        return 0

def main():
    '''
    This function is executed when the file is run.
    '''
    print('#'*60)
    print('Welcome to My Contact Management System')
    print('#'*60)

    while True:
        print('*'*80)
        print('Please choose one of the following options!')
        print('*'*100)

        print('''Option 1. Add a Contact \t Option 2. Search for a contact by name\t Option 3 Update a contact
        \nOption 4. Delete a Contact \t Option 5. Import contacts from a file\t option 6. Print all contacts 
        \nOption 7. Exit the program
        ''')
        print('-'*100)
        task  = input("Enter Your Choice here: ")
        task  = check_int_type(task)

        if task == 0:
            pass
        elif task == 1:
            name = input('Enter Contact Name: ')
            email = input('Enter Contact Email: ')
            phone = input('Enter Contact Phone Number (Do not enter 0): ')
            phone = check_int_type(phone)

            if phone and len(str(phone)) == 10:
                res = add_contact(name, email, phone)
                print('-'*100)
                print("Addition success" if res else "Addition failed")
                print('-'*100)

            else:
                print('Please enter a valid phone number with 10 digits and omit country codes')\

        elif task == 2:
            name = input("Enter Name to Search: ")
            contacts = find_contact(name)
            if len(contacts):
                print('#'*100)
                print('The following contacts were found in the contacts book with the provided name')
                print('#'*100)
                for i, contact in enumerate(contacts):
                    print(f'Contact No. {i}')
                    print(f'Name: {contact[0]}')
                    print(f'Email: {contact[1]}')
                    print(f'Phone: {contact[2]} \n')

            else:
                print('#'*60)
                print("NO CONTACTS FOUND")
                print('#'*60)

        elif task == 3:
            # complete this as homework
            email = input("Enter the contact email to update contact: ")
            with open('contact.txt','r') as file:
                contacts = file.read().split('\n')[:-1]
                contacts = [i.split(',') for i in contacts]
                try:
                    old_value = tuple([cont for cont in contacts if cont[1]==email][0])
                except IndexError:
                    print(f"{email} does not exist.")
                    continue
                print(old_value)

            new_name = input("Enter new contact name: ")
            new_email = input("Enter new contact email: ")
            new_phone_num = input("Enter new contact phone number: ")
            new_phone_num = check_int_type(new_phone_num)
            new_values = (new_name,new_email, new_phone_num)

            if new_phone_num and len(str(new_phone_num))==10:
                if update_contact(old_value, new_values):
                    print("updated succesfully.")
                else:
                    print("error while updating.")
            else:
                print('Please enter a valid phone number with 10 digits and omit country codes')

        elif task == 4:
            # complete his as homework
            email = input("Enter the contact email to delete contact: ")
            with open('contact.txt','r') as file:
                contacts = file.read().split('\n')[:-1]
                contacts = [i.split(',') for i in contacts]
                try:
                    to_delete = tuple([cont for cont in contacts if cont[1]==email][0])
                except IndexError:
                    print(f"{email} does not exist.")
                    continue

            if delete_contact(email):
                print("contact deleted.")
            else:
                print("error while deleting.")

        elif task == 5:
            file_path = input("Enter File Path Here (Hint: paste precontact.txt file path): ")
            if import_contacts(file_path):
                print('CONTACTS IMPORTED SUCCESSFULLY')
            else:
                print("RESTARTING THE PROGRAM")
                print('*SAD*'*10)
        elif task == 6:
            print_all()
        elif task == 7:
            print('Thanks for using my contact management system. I hope you liked it...')
            exit()
        else:
            print("Please enter a valid number between 0 and 6")
        
if __name__ == '__main__':
    main()