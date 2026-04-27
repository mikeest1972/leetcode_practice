# 141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=oizxjoit

Linked list problem

given head det if LL has cycle in it

two points problem the hare and the something else I saw this algorthim in an instagram short.
The idea is you increment a slow pointer and a fast pointer. Like slow + 1 and fast +2 

if they are ever in the same node then there is a cycle.


edge cases to watch out for
if next is null then no cycle obvusly. 


Solutions 1

1. Create two poitns slow and fast
2. loop until slow or fast is null if that happens return flase
3. in the loop check if val and next are the same then return true
4. if not just increment the pointers acordingly and loop again

thing that got me in this problem was the increment of the fast one. It can be null when incrementing. Add a simple check