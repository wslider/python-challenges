# Find out if a Number is Prime

number = 7

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return True
    else: 
        i = 2 
        while i * i <= number:
            if number % i == 0:
                return False
            i +=1
        return True       

if is_prime(number):
    print(f"True, {number} is prime!")
else:
    print(f"False, {number} is not prime.")