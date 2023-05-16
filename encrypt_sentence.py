# lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    # start writing your code here
    ans = []
    sentence = sentence.split(' ')
    for i in range(1, len(sentence)+1):
        if i % 2 == 0:
            c = ''
            v = ''
            for k in sentence[i-1]:

                if k != 'a' and k != 'e' and k != 'i' and k != 'o' and k != 'u':
                    c += k
                else:
                    v += k
            ans.append(c+v)

        else:
            ans.append(sentence[i-1][::-1])

    return ' '.join(ans)


sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
