def to_camel_case(text):
    capitalised = []
    if len(text) >= 1:
        replaced_string = text.replace('_', ' ').replace('-', ' ')
        [capitalised.append(word.capitalize()) for word in replaced_string.split(' ')]
        if text[0].islower():
            capitalised[0] = capitalised[0].lower()
        return ''.join(capitalised)
    else:
        return text


to_camel_case('')
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C")