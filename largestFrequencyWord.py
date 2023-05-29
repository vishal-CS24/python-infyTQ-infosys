# Write a python program that accepts a text and displays
# a string which contains the word with the largest frequency in the te
# xt and the frequency itself separated by a space.
# lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    print(data)
    word = ""
    frequency = 0
    data = data.split(' ')
    kv = {}
    for i in data:
        kv[i] = data.count(i)
    maxi = -1
    x = []
    for key, value in kv.items():
        if value == max(kv.values()):
            x.append(key)
            frequency = value
    for i in x:
        if len(i) > maxi:
            maxi = len(i)
            word = ''
            word += i
    print(word, frequency)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #
# data = "Work like you do not need money, love like you you you have never been hurt, and dance like no one is watching"
data = 'Listen to the big clock Tick tock tick'
max_frequency_word_counter(data)
