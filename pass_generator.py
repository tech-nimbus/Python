

def generate_pass():
    import random

    upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numeric_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ':', ';', '?', '/',
                    '|', '{', '}', '[', ']', ',', '.', '<', '>', '"']

    var = [upper_chars, lower_chars, numeric_chars, special_chars]

    pas = ""

    while len(pas)< 8:
        ct = random.choice(var)
        ta = random.choice(ct)
        if ta in pas:
            continue
        else:
            pas = pas + ta
        
    return pas

passw = generate_pass()
print(passw)
