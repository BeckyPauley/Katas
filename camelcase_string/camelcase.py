def to_camel_case(text):
    capitalised = []
    if len(text) >= 1:
        [capitalised.append(word.capitalize()) for word in text.split(check_splitter(text))]
        if text[0].islower():
            capitalised[0] = capitalised[0].lower()
        return ''.join(capitalised)
    else:
        return text

def check_splitter(text):
    if '-' in text:
        return '-'
    elif '_' in text:
        return '_'

to_camel_case('')
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C")