str = "A man a plan a canal Panama!"

def is_palindrome(str):
    chars_to_remove = [ "!", ".", ",", "?"]
    clean_str = str.lower().join("")
    for char in chars_to_remove:
        clean_str.replace(char, "")
    reverse_clean_str = clean_str[::-1]
    if clean_str == reverse_clean_str:
        print(f"Yes, {str} ... is a palindrome!")
        return True 
    else:
        print(f"False, {str} ... is NOT a palindrome!")
        return False

is_palindrome(str)