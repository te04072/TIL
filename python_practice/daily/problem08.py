
def reverse_string(s):
    if len(s) == 0:
        return ''
    else: 
        return reverse_string(s[1::])+s[0]

print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string("python"))  # "nohtyp"

