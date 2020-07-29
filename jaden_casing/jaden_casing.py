def jaden_casing(tweet):
    capitalised = []
    for word in tweet.split(' '):
        capitalised.append(word.capitalize())
    return(' '.join(capitalised))


