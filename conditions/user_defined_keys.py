operation = input("enter e for encoding or d for decoding: ")
if operation != 'e' and operation != 'd':
    print("sorry we did not understand that")
    exit(0)

key = input("enter the key value: ")
message = input("Enter a message to encode or decode: ") # Get a message
message = message.upper()           # Make it all UPPERCASE :)
output = ""                         # Create an empty string to hold output
for letter in message:              # Loop through each letter of the message
    if letter.isupper():            # If the letter is in the alphabet (A-Z),
        if operation == "e":
            value = ord(letter) + int(key)    # shift the letter value up by 13,
        elif operation == "d":
            value = ord(letter) + (26 - int(key))
        else:
            print("sorry we did not understand that")
            exit(0)

        letter = chr(value)

        # turn the value back into a letter,
        if not letter.isupper():    # and check to see if we shifted too far
            value -= 26             # If we did, wrap it back around Z->A
            letter = chr(value)     # by subtracting 26 from the letter value
    output += letter                # Add the letter to our output string
print("Output message: ", output.lower())   # Output our coded/decoded message
