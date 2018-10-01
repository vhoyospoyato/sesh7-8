
s = input('Please enter a line of random letters from the alphabet: ')

s = s.lower().replace(" ","")

subs = ""
smax= ""

for i in range(0, len(s)-1):

    if s[i] <= s[i+1]:

        if subs == "":

            subs = s[i] + s[i+1]

        else:
            subs = subs + s[i+1]

    elif s[i] > s[i + 1]:

        subs = ""

    if len(subs) > len(smax):
        smax = subs

print("This are the letters that follow the longest alphabetical order from your input: ", smax)

