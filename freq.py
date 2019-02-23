from collections import Counter
print ('Please enter encrypted message\n')
eM= input()
res_count = Counter(eM)
print(res_count)
most_com = res_count.most_common(5)
least_com = res_count.most_common()[:-5-1:-1]
print('\n\ntop 5 frequency', most_com) 
print('\n\nleast common 5 in frequency', least_com)
