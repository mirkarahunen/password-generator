import random
import string

small_letter = list(string.ascii_lowercase)
big_letter = list(string.ascii_uppercase)
number = list(str(range(1,10)))
special_character = [".", ",", "#", "+", "!", "?", "%", "&", "=", "$", "/"]

all_characters = small_letter + big_letter + number + special_character
temp_password = random.sample(all_characters, 10)

password = "".join(temp_password)
print(password)



