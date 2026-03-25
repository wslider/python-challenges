str = "heffalump" 

def reverse_string(str):
    reversed_string = str[::-1]
    print(reversed_string)

def reverse_string_loop(str):
    reversed_string = ""
    for char in str: 
        reversed_string = char + reversed_string
    print(reversed_string)
        
        

reverse_string(str)
reverse_string_loop(str)