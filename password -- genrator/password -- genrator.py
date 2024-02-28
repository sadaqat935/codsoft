import string
import random

def get_valid_length():
    while True:
        length = input("Enter the length of the password: ")
        if length.isdigit(): 
            return int(length)
        else:
            print("Please enter a valid number.")

a0 = string.ascii_letters
a1 = string.ascii_lowercase
a2 = string.ascii_uppercase
a3 = string.digits
a4 = string.punctuation
a5 = string.hexdigits

length = get_valid_length()

complexity = input("Enter the complexity of password (low/medium/high): ")

if complexity == "low" and "LOW":
   
    a=[]
    a.extend(list(a0))
    a.extend(list(a1))
    random.shuffle(a)
    print("".join(a[0:length]))
  
elif complexity == "medium" and "MEDIUM":
   
    b=[]
    b.extend(list(a0))
    b.extend(list(a2))
    b.extend(list(a1))
    b.extend(list(a3))
    random.shuffle(b)
    print("".join(b[0:length]))

elif complexity == "high" and "HIGH":
 
  s=[]
  s.extend(list(a0))
  s.extend(list(a1))
  s.extend(list(a2))
  s.extend(list(a3))
  s.extend(list(a4))
  s.extend(list(a5))

  random.shuffle(s)
  show="".join([random.choice(s) for x in 
  range(length)])
  print("Generated password: ",show)
else:
    print("Invalid choice.")
    password = None

