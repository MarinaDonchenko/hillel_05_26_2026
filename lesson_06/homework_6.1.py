user_input = input("Enter your text: ")
if len(set(user_input)) > 10:
    print("Text have unique characters > 10?:", True)
else:
    print("Text have unique characters > 10?:", False)