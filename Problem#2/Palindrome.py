#Kai Jameson
#Thursday @ 2pm

def check_palindrome(user_input):
 #type your code here
    string = ''
    for x in range(len(user_input)-1, -1, -1):
        if user_input[x] != ' ':
            string += user_input[x]
    inputNoSpaces = ''
    for x in range(0, len(user_input), 1):
        if user_input[x] != ' ':
            inputNoSpaces += user_input[x]
    if string == inputNoSpaces:
        print('palindrome: ' + user_input)
    else: print('not a palindrome: ' + user_input)
    
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
