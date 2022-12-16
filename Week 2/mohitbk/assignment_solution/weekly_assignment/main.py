# Feel free to add as much lines as you want between ## START CODE HERE and ## END CODE HERE.
# Please donot write code outside this boundry or you may fail the test.

# start by importing the necessary documents

import random
import string 

def rank(pwd: str) -> str:
    '''
    Ranker function that ranks the password based on the assigned criteria

    Input: pwd -> character or string

    The following are the requirements for POOR / MODERATE / STRONG password.

    Passwords can contain (not required) any of the following requirements:  
    i. Lower case letters (a – z).       iii) Numbers ( 0 – 9 ).  
    ii. Upper case letters (A – Z).      iv) Symbols ( ! + - = ? # % * @ & ^ $ _ )

    1. A POOR Password is defined as: 
    a. Contains less than 3 from the above 4 items ( i – iv ).  
    b. Less than 8 characters in length.

    2. A MODERATE Password is defined as:  
    a. Contains 3 from the above 4 items ( i – iv )  
    b. Between 8 to 10 characters in length.

    3. A STRONG Password is defined as:  
    a. Meets all 4 of the above items ( i – iv )  
    b. Greater than 10 characters in length.

    Returns: rank -> rank of password; POOR / MODERATE / STRONG
    '''
    ## Start code here
    # POOR
    lower_check = 0
    upper_check = 0
    number_check = 0
    special_char = 0
    checks = [lower_check,upper_check,number_check,special_char]
    c=0
    r = ""
    for i in pwd:
        if i in string.ascii_uppercase:
            upper_check = 1
        elif i in string.ascii_lowercase:
            lower_check = 1
        elif i in string.digits:
            number_check = 1
        elif i in string.punctuation:
            special_char = 1
    
    for i in checks:
        if i == 1:
            c += 1

    if len(pwd) < 8 or c < 3:
        r = "POOR"
    elif len(pwd) >= 8 and len(pwd) <= 10 or c == 3:
        r = "MODERATE"
    elif len(pwd) > 10 or c == 4:
        r = "STRONG"
    ## End code here
    return r

def option1():
    '''
    Helper function that will be executed when user selects option 1 in the initial case.
    '''
    # Steps to follow:
    # 1. Ask user to rank password from either Users-Pwds.txt or a custom file (second part for bonus only you can skip this)
    # 2. Open the file containing username and password in each line and a file to store the ranked password information(Users-Pwds-Chked.txt).
    # 2.1 ## !IMPORTANT ## Store the list of username,passwords in a variable called usrpwds. 
    # 3. Use the rank() function to rank the password
    # 4. Write to the Users-Pwds-Chked.txt file (username,password,rank) in each line as string. Omit the brackets and only fill up the actual values. 
    # 5. Close necessary files and print to terminal.
    
    ## START CODE HERE
    print("Select one of them.")
    print("1. Default file    2. Custom File")
    
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Conversion error. Please enter valid option.")
    
    # if option is 1

    with open('Users-Pwds.txt', 'r') as input_file:
        usrpwds = []
        usrpwds = input_file.read().split('\n')[:-1]
        usrpwds = [i.split(',') for i in usrpwds]
        # print(usrpwds)
        usrpwds_chked = usrpwds
        for i,c in enumerate(usrpwds):
            pw_rank = rank(c[1])
            usrpwds_chked[i].append(pw_rank)
    
        with open('Users-Pwds-Chked.txt', 'w') as output_file:
            output = [','.join(i) for i in usrpwds_chked]
            output_file.writelines('\n'.join(output))
            output_file.write('\n')
    ## END CODE HERE

    print('#'*80)
    # [INFO] Be sure to change userpwds with the name of variable that you give to the list of passwords
    print('[INFO] '+'Number of passwords checked:',str(len(usrpwds))) 
    print('[INFO] '+'The given rankings can be found in Users-Pwds-Chked.txt')
    print('#'*80)

def option2():
    '''
    Function to be executed when the user selects option 2 (generate password) in the main loop.
    
    Steps to follow:
        Prompt the user for a username (No more the 20 characters in length).
        Create a Function that will have no (zero) arguments. (generate)
        The Function will randomly generate a STRONG password (Meeting the STRONG Requirments).
        Ask the user if they would like this saved (Y or N).
        If Y: Open the Input file (Users-Pwds.txt) and append the username,password to the EOF.
        If N: Ask if they would like to generate a different password for this user (Y or N).
        Then the program loops back to the menu again offering displaying and offering to select 1, 2 or 3.
    '''

    def generate() -> str:
        '''
        Helper function to generate password.
        Returns: A string pwd with strong ranking in our ranking system.
        '''
        # Starter code, Ualphabets contains all upper case alphabets
        # Lalphabets condains all lowercase alphabets
        # chars contains all special characters and digits contains all numeric digits
        Ualphabets = string.ascii_uppercase
        Lalphabets = string.ascii_lowercase
        chars = string.punctuation
        digits = string.digits
        pwd = ''
        # Hint: user random.choice to select a random Upperalphabet(Ualphabet), Lalphabet, chars, and digits. Join then all together in pwd and check ranking
        # While the required ranking is not met continue joining new Ualphabet, Lalphabet, chars and digits.
        lst = [Ualphabets,Lalphabets,chars,digits]
        ## START CODE HERE
        for i in range(12):
            c_i = random.randint(0,3)
            pwd += lst[c_i][random.randint(0,len(lst[c_i])-1)]

        ## END CODE HERE
        return pwd
    
    # Ask for username and check 20 character limits

    ## START CODE HERE
    while True:
        username = input("Enter your name: ")
        if len(username) > 20:
            print("Please enter username of less than 20 chars.")
            continue
        break

    
    ## END CODE HERE

    # Generate the password using generate() and follow the steps as guided in the function header. 

    ## START CODE HERE
    p = generate()
    while True:
        r = rank(p)
        if r != "STRONG":
            p = generate()
        else:
            print(f"You password is {p}")
            print("Would you like to save this password,Y/N? ", end=" ")
            choice = input()

            if choice == "Y":
                with open('Users-Pwds.txt', 'a') as file:
                    file.write(f"{username,p}")
            else:
                print("Would you like to generate new password Y/N?", end=' ')
                y_n = input()
                
                if y_n == "Y":
                    p= generate()
                    continue
                else:
                    break
        
        


    ## END CODE HERE

def main():

    print('Welcome to my password ranking program')
    while True:
        print('-'*40)
        print('Please select one of 3 options')
        print('option1. Rank password from an existing file \t option2. Generate a strong password \noption3. exit the program')
        inp = input("Enter your option here:")
        
        # try converting the inp to integer form and then check condition if input was either option1, 2, 3 or something else. 
        # exit the loop by using the break command if the user selects 3 other wise use option1() and option 2() function 

        ## START CODE HERE

        # type conversion
        try:
            inp = int(inp)
        except ValueError:
            print("Conversion error, Please enter valid option")

        # task handling
        if inp == 3:
            break
        elif inp == 1:
            option1()
        elif inp == 2:
            option2()
        ## END CODE HERE


# DONOT TOUCH THESE LINES
if __name__=='__main__':
    main()