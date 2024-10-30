num = 64
string = ''

def dec_to_n(num, d):
    string = ''
    while num:
        string += str(num % d)
        num //= d
    string = string[::-1]
    return int(string)
print(string)