---
title: 02 Add Two Numbers
summary: Algorithm

date: "2022-1-2T00:00:00Z"
lastmod: "2022-1-2T00:00:00Z"

categories: Algorithm
---

### Description

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

[Add Two Numbers - LeetCode](https://leetcode.com/problems/add-two-numbers/)

### Simple Solution

This problem is actually relatively simple as long as I am pretty familiar with linked list (not with c++ grammar however, which is necessary for me to catch up). Just set up one carrier bit, and then add up digits one by one. Sort like merging two sorted arrays.

### Code

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carrier = 0;
        ListNode* answer = new ListNode;
        ListNode* ans = answer;
        
        while (l1 != NULL && l2 != NULL) {
            ans->val = (l1->val + l2->val + carrier) % 10;
            carrier = (l1->val + l2->val + carrier) / 10;
            
            if (l1->next != NULL || l2->next != NULL) {
                ListNode* newNode = new ListNode;
                 ans = ans->next = newNode;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        
        while (l1 != NULL) {
            ans->val = (l1->val + carrier) % 10;
            carrier = (l1->val + carrier) / 10;
            
            if (l1->next != NULL) {
                ListNode* newNode = new ListNode;
                ans = ans->next = newNode;
            }
            l1 = l1->next;
        }
        
        while (l2 != NULL) {
            ans->val = (l2->val + carrier) % 10;
            carrier = (l2->val + carrier) / 10;
            
            if (l2->next != NULL) {
                ListNode* newNode = new ListNode;
                ans = ans->next = newNode;
            }
            l2 = l2->next;
        }
        
        if (carrier != 0) {
            ListNode* newNode = new ListNode;
            ans = ans->next = newNode;
            ans->val = carrier;
        }
        
        return answer;
    }
};
```



### Complexity Analysis

Time complexity

This code need and only need one way look up. As a result, the time complexity is $O(n)$.

Space complexity

Only one linked list is need and one carrier int. So space complexity is also $O(n)$.
