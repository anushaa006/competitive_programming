class Solution(object):
    def monotoneIncreasingDigits(self, n):
        listNum=list(str(n))
        flag=len(listNum)
        for i in range(len(listNum)-1,0,-1):
            if listNum[i-1]>listNum[i]:
                flag=i
                listNum[i-1]=str(int(listNum[i-1])-1)
        for i in range(flag,len(listNum)):
            listNum[i]='9'
        return int("".join(listNum))
        