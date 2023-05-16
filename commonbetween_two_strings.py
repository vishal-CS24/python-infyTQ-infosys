# lex_auth_012693825794351104168
# Problem Statement
# Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

# Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

# Sample Input

# Expected output

# "I like Python"
# "Java is a very popular language"

# lieyon


# lex_auth_012693825794351104168

# lex_auth_012693825794351104168

def find_common_characters(msg1, msg2):
    str = ''
    for i in msg1:
        if i != " " and i in msg2:
            str += i
    if len(str) == 0:
        return -1
    else:
        return str


    # Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
