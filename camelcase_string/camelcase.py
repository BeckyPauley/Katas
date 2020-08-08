def to_camel_case(text):
    capitalised = []
    for word in text.split(check_splitter(text)):
        capitalised.append(word.capitalize())
    if text[0].islower() == True:
        capitalised[0] = capitalised[0].lower()
    print(check_splitter(text).join(capitalised))

def check_splitter(text):
    if '-' in text:
        return '-'
    elif '_' in text:
        return '_'

#split string into words based on - or _ characters

#  if first letter capitalised, return that word with capital

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
