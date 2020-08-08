def to_camel_case(text):
    capitalised = []
    [capitalised.append(word.capitalize()) for word in text.split(check_splitter(text))]
    if text[0].islower() == True:
        capitalised[0] = capitalised[0].lower()
    return check_splitter(text).join(capitalised)

def check_splitter(text):
    if '-' in text:
        return '-'
    elif '_' in text:
        return '_'
