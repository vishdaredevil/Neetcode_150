This is valid anagram problem from NEETCODE sheet question 2nd and LEETCODE 242 question   
[https://leetcode.com/problems/valid-anagram/description/](https://leetcode.com/problems/valid-anagram/description/)  
[https://neetcode.io/problems/is-anagram?list=neetcode150](https://neetcode.io/problems/is-anagram?list=neetcode150)

1st approach:  
After seeing this question 1st approach came in my mind is to sort the both the str and then after sorting it we can compare both the string to find they are anagram or not.But wait what is anagram it is type of string in which aal the element are are exact same but the order of element doesnt matter   
After using this approach i able to get the correct answer and also my code run successfully, hurrayyyyy\!\!\!\! But when i analyse the complexity it is of   
O(NlogN) , is it is optimal approach so answer is a big nooooo.

2nd approach:  
We can use dictionary approch in this we use to make two separate diction for string s and t and count the frequency of each element and then compare the both dictionary if all is matched then return true else return false , its time complexity if of O(n)  which is a much optimal approach then other .

 **NOTE 👍: DICTIONARY APPROACH IS ALSO CALLED HASHING MAP METHOD OR HASHMAP**