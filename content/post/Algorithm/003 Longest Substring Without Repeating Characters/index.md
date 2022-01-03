---
title: 03 Longest Substring Without Repeating Characters
summary: Algorithm

date: "2022-1-3T00:00:00Z"
lastmod: "2022-1-3T00:00:00Z"

categories: Algorithm
---

## Descreption

Given a string `s`, find the length of the **longest substring** without repeating characters.

[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## First Thought

I suppose the first thought that popped up was just do what human would do: Read one by one, save what you have encountered and update when the repeated character is showing up.

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int longest = 0, current = 0;
        int head = 0;
        int pot[256] = {0};

        for (char c : s) {
            if (!pot[c]) {
                pot[c] = 1;
                current += 1;
            }
            else {
                // update
                if (longest < current) longest = current;

                // trace back
                for (int f = head; ; ++f) { // search from header
                    if (s[f] == c) {        // and break when find the one
                        head = f+1;
                        break;
                    }
                    current -= 1;  // update minus length
                    pot[s[f]] = 0; // and clear the pot
                }
            }
        }

        if (longest < current) longest = current;
        return longest;
    }
};
```

## Complexity Analysis

Time complexity: $O(n)$

The string can only be traversed twice: the first time is searching and the second time is tracing back, which will not have any overlap. So, the best is $O(n)$ and the worst might be $O(2n)$.

Space complexity: $O(1)$

Just 256+4 integers.

(I have checked out the solutions and only to find my solution not bad XD)