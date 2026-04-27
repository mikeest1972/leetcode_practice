# Valid palindrome

link =  https://leetcode.com/problems/valid-palindrome/?envType=problem-list-v2&envId=oizxjoit

must only take into account alphanumeric char

A palindrome is a word that reads the same backwards and forward
for example :

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Plan 1:
- remove all non-alphanumeric char and change it to lowercase
- two pointers l and r l = 0 r = len(s)
- move the pointers to the middle and compare them as you move them

edge cases:
- empty string = true

Time complexity: O(n) 
Space complexity: O(1)