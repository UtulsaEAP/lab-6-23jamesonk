#Kai Jameson
#Thursday @ 2pm

def process_and_print(input_string):
      # Split into separate strings
    numList = list(input_string.split())
    # Convert strings to integers and filter out negative values
    inputData = []
    for num in numList:
      if int(num) < 0:
        inputData.append(int(num))

    # Sort integers in reverse order
    inputData.sort(reverse=True)
    # Print sorted integers
    result = ''
    for number in inputData:
      result += str(number) + ' '
    print(result, end='')
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")
    # Call the function to process and print the result
    process_and_print(user_input)
