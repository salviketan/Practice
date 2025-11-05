import re


string = input()
sub_string = input()
# string = 'aaabaabbbaaaaaaabaaeddedsdaa'
# sub_string = 'aa'

for i in range((len(string)-1)):
    end = 2 + i
    found = re.search(rf'{sub_string}',string[i:end])
    if found:
        print('('+str(found.start()+i)+',',str(found.end() - 1 + i)+')')