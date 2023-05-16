# lex_auth_01269444890062848087

def find_correct(word_dict):
    ans = [0, 0, 0]
    for key, value in word_dict.items():
        if key == value:
            ans[0] += 1
        else:
            if len(key) != len(value):
                ans[2] += 1
            else:
                c = 0
                for i in range(len(key)):
                    if key[i] != value[i]:
                        c += 1
                if c <= 2:
                    ans[1] += 1
                else:
                    ans[2] += 1
    return ans


word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS",
             "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
