def run_checker():
    input_text = input("Type a word to check if it is a palindrome: ").strip()

    if not input_text:
        print("Empty input detected. Please enter a valid string.")
        return
    
    filtered_text = ''.join(c.lower() for c in input_text if c.isalnum())

    if filtered_text == filtered_text[::-1]:
        print(f"'{input_text}' is a palindrome!")
    else:
        print(f"'{input_text}' is not a palindrome.")

if __name__ == "__main__":
    run_checker()
