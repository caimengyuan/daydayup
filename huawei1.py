import sys 

def stringToError(str1, str2, l):
    list_str1 = list(str1)
    s = list(str1)
    for i in range(1, l+1):
        list_str1.pop(i)
        str1 = "".join(list_str1)
        if str1 == str2:
            return True
        list_str1 = s
    return False
    
def main(preStr, shortStr):
    l = int(len(shortStr) * 0.8)
    for i in range(len(shortStr)):
        if preStr.find(shortStr[i]) != -1:
            str2 = shortStr[i:i+l]
            str1 = preStr[preStr.find(shortStr[i]):preStr.find(shortStr[i])+l+1]
            if stringToError(str1, str2, l):
                list_pre = list(preStr)
                list_pre[preStr.index(shortStr[i]):preStr.find(shortStr[i])+l+1] = ["*"]*(l+1)
                preStr = "".join(list_pre)
                return preStr
    print(preStr)
                
                
# for line in sys.stdin:
#     a = line.split()
# abcdefgBCDEFG()012345678987654 ACEF
pre = "abcdefgBCDEDFG()012345678987654"
short = "ADEF"
print(main(pre, short))