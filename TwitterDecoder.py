#Challenge Code
# Add support for abbreviations you commonly use or search the internet for some.
#Allow the user to enter a complete tweet (160 characters or less) as a single line of text. 
# Search the resulting string for abbreviations and print a list of each abbreviation along with its decoded meaning.
tweet = str(input('Enter tweet:\n'))
tweet = tweet.upper()
tweet_length = len(tweet)
if (tweet_length < 161):
    if 'LOL' in tweet:
        print('LOL = laughing out loud')
    if 'BTW' in tweet:
        print('BTW = by the way')
    if 'BFN' in tweet:
        print('BFN = bye for now')
    if 'FTW' in tweet:
        print('FTW = for the win')
    if 'IRL' in tweet:
        print('IRL = in real life')
    if 'IDK' in tweet:
        print("IDK = I don't know")
    if 'TY' in tweet:
        print('TY = thank you')
    if 'YW' in tweet:
        print("YW = you're welcome")
    if 'RN' in tweet:
        print('RN = right now')
    if ('LOL' not in tweet) and ('BTW' not in tweet) and ('BFN' not in tweet) and ('FTW' not in tweet) and ('IRL' not in tweet) and ('IDK' not in tweet) and ('TY' not in tweet) and ('YW' not in tweet) and ('RN' not in tweet):
        print("Sorry, don't know that one")
else:
    print('Tweet cannot be longer than 160 characters')
