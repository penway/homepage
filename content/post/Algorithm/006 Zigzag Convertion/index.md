---

title: 06 Zigzag Conversion
summary: Algorithm

date: "2022-1-10T00:00:00Z"
lastmod: "2022-1-10T00:00:00Z"

categories: Algorithm

---

## Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this:

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

## First Thought

This zigzag form actually does not need to be written out. The string can be divided into groups by one zigzag, whose length is `rownum*2 - 2`. Then every line can be calculated out.

For the first line, they are the head of each zigzag.

For the rest but not last, there would be two characters: counted from the front and counted from the end.

For the last line, they are the middle one.

Which gives us the code

## Code

Several details were missed by me in the beginning:

1. The tail, which does not form a full zigzag should be calculated specially
2. When `numRow == 1`, `numRow * 2 - 2 == 0` and it should be treated specially

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        string ans, c;
        int setnum = numRows * 2 - 2;
        if (setnum == 0) {
            return s;
        }
        int sets = s.size() / setnum;


        for (int j = 0; j < s.length(); j += setnum) {
            ans.append(c = s[j]);
        }
        for (int i = 1; i < numRows-1; ++i) {
            int j;
            for (j = 0; j < sets; ++j) {
                ans.append(c = s[j * setnum + i]);
                ans.append(c = s[j * setnum + setnum - i]);
            }
            if (j * setnum + i < s.size())
                ans.append(c = s[j * setnum + i]);
            if (j * setnum + setnum - i < s.size())
                ans.append(c = s[j * setnum + setnum - i]);     
        }
        for (int j = setnum / 2; j < s.length(); j += setnum) {
            ans.append(c = s[j]);
        }
        return ans;
    }
};
```

## Complexity

**Time Complexity**

Each character are just visited randomly once, so it is always $O(n)$.

**Space Complexity**

A new string is needed to store the output, so it is always $O(n)$.