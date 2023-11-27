from itertools import combinations
def generate_word_combinations(m,r):
    # Generate all combinations of words of length r
    word_combinations = list(combinations(m,r))
    return word_combinations
with open('uncombined.txt','r') as o:
    m=o.readlines()
    m=[line.strip() for line in m]
    print('your selected words are:\n\n'+str(m)+'\n\n')
t=int(input('Enter minimum length of word(in +ve integers) :'))
l=int(input('Enter maximum length of words(in +ve integers) :'))
for i in range(t,l+1,1):
    print(str(i)+'\n')
    combinatio=generate_word_combinations(m,t)
    for combination in combinatio:
        com=list(combination)
        k="".join(com)
        with open('combined.txt','a') as p:
            p.writelines(k+'\n')
print('\n\nplease restart your code editor if my code bugs :) \n and reopen combined.txt file again\n\n')