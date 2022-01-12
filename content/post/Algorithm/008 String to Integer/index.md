---
title: 08 String to Integer (atoi)
summary: Algorithm

date: "2022-1-12T00:00:00Z"
lastmod: "2022-1-12T00:00:00Z"

categories: Algorithm
---

## Description

[String to Integer (atoi) - LeetCode](https://leetcode.com/problems/string-to-integer-atoi/)

## First Thought

This problem is easy, just operate every digit.

Those detailed requirements are not interesting and pretty easy to cope with, so I will just skip them.

The only alert is about overflow. The way to cope with over flow is the same as the last question. [07 Integer Reverse](https://penway.cn/post/algorithm/007-reverse-integer/) `if (ans > max10 || (ans == max10 && c - 48 > 7))`

But the problem lies in the update process: `ans = ans * 10 + c - 48`, the head part `ans * 10 + c` might cause a overflow due to it is `ans * 10 + c - 48` that will not overflow, so just use `ans * 10 + (c - 48)` instead.

## Code

```cpp
class Solution {
public:
    int myAtoi(string s) {
        int ans = 0;
        int pos = 0;
        int max10 = INT_MAX / 10;
        int start = 0;
        for (char c : s) {

            if (c >= 48 && c <= 57)
            {
                start = 1;
                if (ans > max10 || (ans == max10 && c - 48 > 7))
                {
                    if (pos >= 0)
                        return INT_MAX;
                    return INT_MIN;
                }
                ans = ans * 10 + c - 48;
            }
            else if (start == 0) {
                if (c == ' ') continue;

                else if (c == '-') {
                    pos = -1;
                    start = 1;
                }
                else if (c == '+') {
                    pos = 1;
                    start = 1;
                }
                else break;
            }
            else {
                break;
            }
        }
        if (pos >= 0)
            return ans;
        else
            return ans * -1;
    }
};
```

## Complexity Analysis

**Time Complexity**

$O(log(x))$, There are about $log\_{10}(x)$ digits in number x

or $O(n)$, whatever.

**Space Complexity**

$O(1)$

