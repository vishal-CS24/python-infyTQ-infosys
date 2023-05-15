# lex_auth_01269438070259712046

def count_names(name_list):
    count1 = 0
    count2 = 0

    # start writing your code here
    # Populate the variables: count1 and count2
    for i in name_list:
        if len(i) == 3:
            if i[1:] == "at":
                count1 += 1
                count2 += 1
        else:
            if "at" in i:
                count2 += 1
    print("_at -> ", count1)
    print("%at% -> ", count2)


# Provide different names in the list and test your program
name_list = ["Hat", "Cat", "rabbit", "matter"]
count_names(name_list)
