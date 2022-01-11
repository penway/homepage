---

title: 07 Integer Reverse
summary: Algorithm

date: "2022-1-11T00:00:00Z"
lastmod: "2022-1-11T00:00:00Z"

categories: Algorithm

---

## Description

Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

[Reverse Integer - LeetCode](https://leetcode.com/problems/reverse-integer/)

## First Thought

This problem is easy, just operate every digit - pop from bottom and then add from top.

```
loop
	y = y * 10 + x % 10
	x = x / 10
```

But I didn't figured out how to avoid the 32-bit overflow. The trick is this must be done before `y = y * 10 + x % 10`, just to compare `y` with `INT_MAX / 10`.

If `y > INT_MAX / 10`, overflow must happen.

Due to `INT_MAX = 2147483647`, so `y = 214748364` and `x%10 > 7` will also cause overflow.

## Code

```cpp
class Solution {
public:
    int reverse(int x) {
        int y = 0, pos, temp, yt, MI = INT_MAX / 10;
        x > 0 ? pos = 1 : pos = -1;
        x = abs(x);
        while (x > 0) {
            temp = x % 10;
            if (y > MI || (y == MI && temp > 7)) return 0;
            y = y * 10 + temp;
            x /= 10;
        }
        return y * pos;
    }
};
```

## Complexity Analysis

**Time Complexity**

$O(log(x))$, There are about $log\_{10}(x)$ digits in number x

**Space Complexity**

$O(1)$