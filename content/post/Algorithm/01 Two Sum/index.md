---
title: 01 Two Sum
summary: Algorithm

date: "2022-1-1T00:00:00Z"
lastmod: "2022-1-1T00:00:00Z"

categories: Algorithm
---

### Description

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

### First Thought

The basic solution is pretty simple: traverse `nums` by i and j and check if their sum equals to the target.

Thar produce the following answer:

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        for (int i = 0; i < nums.size() - 1; ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) {
                    answer.emplace_back(i);
                    answer.emplace_back(j);
                    return answer;
                }
            }
        }
        return answer;
    }
};
```

### Complexity Analysis

Time complexity

The average time complexity for this $O(n^2)$. The best situation is $O(1)$ and the worst is $O(n^2)$.

Space complexity

$O(1)$, just for i, j and answer.

### Hashmap Solution

(It seems that using hash table to find element is a great way to reduce time complexity)

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        map<int, int>::iterator in;
        vector<int> answer;
        for (int i = 0; i < nums.size(); ++i) {
                  
            int hope = target - nums[i];
            in = m.find(hope);
            if (in != m.end()) {
                answer.emplace_back(i);
                answer.emplace_back(in->second);
                return answer;
            }
            
            m.insert(pair<int, int>(nums[i], i));
        }
        return answer;
    }
};
```

Here is the only problem I met: this insert line `m.insert(pair<int, int>(nums[i], i));` should be at the end of the loop instead of at the beginning. Or if the target is a even number, then the new number itself is searchable, which lead to a false answer.

### Complexity Analysis

Time complexity

The average time complexity for this $O(n)$. The best situation is $O(1)$ and the worst is $O(n)$. The hash map really speed up the searching process, the `map.find()` function has a time complexity close to $O(1)$.

Space complexity

$O(n)$, hash map has to store all the numbers.

The runtime on leetcode decrease from 590ms to 7ms, really impressive.

