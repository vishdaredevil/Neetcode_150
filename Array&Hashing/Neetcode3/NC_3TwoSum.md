[https://neetcode.io/problems/two-integer-sum?list=neetcode150](https://neetcode.io/problems/two-integer-sum?list=neetcode150)  
[https://leetcode.com/problems/two-sum/submissions/1379093318/](https://leetcode.com/problems/two-sum/submissions/1379093318/)  
In this question we used to find the index of number whose sum is equal to the given number ,  
So 1st approach  
Ek loop chlega i to n tk then usme hum complement nikl lenge jse i \- target jo number ayega then usko phir se ek loop lgakr i+1 to n us number ko dundnge or jis index pr aya usko return krva lenge.   
  	   n \= len(nums)  
         for i in range(n):  
             x \= target \- nums\[i\]  
             for j in range(i \+ 1, n):  
                 if nums\[j\] \==x:  
                     return \[i, j\]  
But its time complexity is much higher means its complexity is 0(n) which is higher and consider as non optimal approach.

2nd approach 👍  
Using hashmap in this ek dictionary bna lo then hum ek loop i to n lagenge then har num ki  i value pr ek complement niklange x target me se num\[i\] substrat krkr then  usko hum dictiony me check krnge ki vo complement x ki value h ya ni usme agr h to diction ki us value pr uska index or jo index chl ra h vo return kr denge list ki form me aur ni h toh Agar **nahi**, toh **current number (num)** aur uska index i dictionary mein daal denge   
 	  d \= {}  
        for i in range(len(nums)):    
            n \= nums\[i\]    
            x \= target \- n  
            if x in d:  
                return \[d\[x\], i\]  
            d\[n\] \= i  
Its time complexity is of o(n) which is very optimal approach.