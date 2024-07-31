name, char = input('Please enter your name and char:- ').split(",")
print(f'Your name length is:- {len(name)}')
# Lower case use
name_low = name.lower()
char_low = char.lower()
# Character count
print(f'Your character count is:- {name_low.count(char_low)}')