def reverse(s):
    if len(s) <=1:
        return s
    else:
        first_char = s[0]
        rest = s[1:]
        return reverse(rest) + first_char
    
word = input("Enter a word: ")
print(reverse(word))