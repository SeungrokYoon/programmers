import re
from collections import Counter as mset


def solution(str1, str2):
    s1_l = [str1[i:i + 2].upper() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]

    s2_l = [str2[i:i + 2].upper() for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    if len(s1_l) == 0 and len(s2_l) == 0:
        return 65536
    mset_s1 = mset(s1_l)
    mset_s2 = mset(s2_l)

    interSetLen = len(list((mset_s1 & mset_s2).elements()))
    unionSetLen = len(list((mset_s1 | mset_s2).elements()))

    return int(interSetLen / unionSetLen * 65536)

def solution2(str1,str2):
    str1= str1.lower()
    str2= str2.lower()
    s1=[]
    s2=[]
    for i in range(0, len(str1)-1):
        if re.findall('[a-z]]',str1[i:i+2]):
            s1.append(str1[i:i+2])
    print(s1)
    print(s2)

solution2('AA1aAAA','1234')