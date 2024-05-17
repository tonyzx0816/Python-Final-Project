user_letter = input()
vowel = ['a','e','i','o','u']
if user_letter in vowel:
    print(f'{user_letter} is a vowel.')
elif user_letter == 'y':
    print('sometimes y is a vowel, and sometimes y is a consonant.')
else:
    print(f'{user_letter} is a consonant.')