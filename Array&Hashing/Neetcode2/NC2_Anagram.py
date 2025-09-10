class Solution:
    def areAnagrams(self, s1, s2):
# code here
        d1={}
        d2={}
        for i in s1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in s2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        if d1==d2:
            return True
        else:
            return False

