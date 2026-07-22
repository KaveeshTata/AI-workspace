# DSA Practice Log

Log every problem here, right after solving (or after reviewing the solution).
Keep entries short — 1-2 lines per field max. The goal is fast capture, not essays.

---

## Entries

### Contains Duplicate — AH 1
- **Date:** 2026-07-14
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** Talking about arrays and time complexity O(n)
- **Brute force approach:** two for loops to check for each element and return true or false
- **Optimized approach:** Using Hashmap and check if key exists or not
- **Time / Space:** O(n)
- **Where I got stuck:** Implementation of hashmap. Begineer in cpp
- **The "aha" / trick:** Counting the frequency of a number means it must be a hashmap
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-21

### Valid Anagram — AH 2
- **Date:** 2026-07-14
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** Talking about frequency and count of a string
- **Brute force approach:** Using two hashmaps and inserting the frequencies and then checking whether they are equal or not
- **Optimized approach:** Using a single hashmap and incrementing from one string, decrementing in another and at last checking the values are 0 or not
- **Time / Space:** O(n)
- **Where I got stuck:** Implementation to check the values in hashmap
- **The "aha" / trick:** Mention of a count or frequency of the charecters in a string
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-21

### Two Sum — AH 3
- **Date:** 2026-07-14
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** We have to remember previous numbers to compare them 
- **Brute force approach:** Using two for loops and adding the numbers to find if it is equal to target or not
- **Optimized approach:** Using a hashmap where we store the number and its index as key value pair
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Since we have to compare the numbers which came before too. We use a hashmap
- **Confidence (1-5):** 5
- **Revisit by:** 2026-07-21

### Group Anagrams — AH 4
- **Date:** 2026-07-15
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** Talking about frequency and count of a string
- **Brute force approach:** Sort the strings and then using hashmap we keep track of all the anagrams
- **Optimized approach:** Use a vector of size 26, change the frequency of that index. Convert it to string and then add it as a key in a hashmap
- **Time / Space:** O(n*k)
- **Where I got stuck:** Getting an optimized solution from brute force
- **The "aha" / trick:** Mention of a count or frequency of the charecters in a string
- **Confidence (1-5):** 2
- **Revisit by:** 2026-07-21

### Top k Frequent elements — AH 5
- **Date:** 2026-07-16
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** Talking about frequency and sorting
- **Brute force approach:** Use a frequency hashmap and then sort the values in descending order and return the top k elements
- **Optimized approach:** Use a frequency map but instead of sorting use bucket sort algorithm and then iterate over it for top k elements
- **Time / Space:** O(n*k)
- **Where I got stuck:** Iterating to get the result for it
- **The "aha" / trick:** Frequncy map and sorting because we need only top elements
- **Confidence (1-5):** 2
- **Revisit by:** 2026-07-21

### Encode and decode — AH 6
- **Date:** 2026-07-16
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** Encoding and decoding means a delimeter
- **Brute force approach:** Add a delimiter after every string while encoding and decode based on the delimiter
- **Optimized approach:** Use a count feature of every element in the vector add it before the delimiter so that while decoding we can get exact number of elements to be in the string in the vector
- **Time / Space:** O(n*k)
- **Where I got stuck:** Iterating delimeter and the count at once and leveraging them both
- **The "aha" / trick:** Basically counting and delimiter means its easy just like Group anagrams
- **Confidence (1-5):** 2
- **Revisit by:** 2026-07-21

### Product except self — AH 7
- **Date:** 2026-07-17
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** Product normally means looping through the elements and maintaining a variable to iterate
- **Brute force approach:** Two nested for loops for getting the product
- **Optimized approach:** Use a prefix and suffix approach and get the products of left to the element and right to the element. Then we multiply both the prefix and suffix vectors to get the output vector
- **Time / Space:** O(n)
- **Where I got stuck:** Initialising the vectors at the right index and iterating variables
- **The "aha" / trick:** Actually got it from the hints section of the editor
- **Confidence (1-5):** 3
- **Revisit by:** 2026-07-21

### Valid sudoku — AH 8
- **Date:** 2026-07-21
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** no duplicates normally means a hash set
- **Brute force approach:** Two nested for loops for checking rows and cols and then a 4 nested for loop for the square checking
- **Optimized approach:** There is no specified optimized approach. The brute force is the best approach
- **Time / Space:** O(n)
- **Where I got stuck:** Square boxes indexing and loop variable initilisation
- **The "aha" / trick:** Checking duplicates in O(1) time is always a hash set. So just be reading the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### Longest Consecutive Subsequence — AH 9
- **Date:** 2026-07-22
- **Topic/Pattern:** Arrays and Hashing
- **Signal I used to recognize it:** no duplicates normally means a hash set
- **Brute force approach:** Sorting and then iterating using two nested loops to get the integer back
- **Optimized approach:** Using hash set and checking whether the number is a starting of a subsequence or not. 
- **Time / Space:** O(n)
- **Where I got stuck:** indexing logic for iterating the hash set to get the solution
- **The "aha" / trick:** Checking duplicates in O(1) time is always a hash set. So just be reading the question
- **Confidence (1-5):** 3
- **Revisit by:** 2026-07-28

### Valid palindrome — TP 1
- **Date:** 2026-07-22
- **Topic/Pattern:** Two pointers
- **Signal I used to recognize it:** Comparing two indices and updating it prallelly
- **Brute force approach:** Preprocess the strings. Take two strings, iterate the input string from the back and from the front. Compare both
- **Optimized approach:** Using two pointers simulateiously and returning false even if one of the does not comply
- **Time / Space:** O(n)
- **Where I got stuck:** Preprocessing the string to exclude the non alphanumeric elements
- **The "aha" / trick:** Basically just by reading the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

---

## Weekly Review Checklist
- [ ] Pull all entries with confidence ≤ 3 from last 7 days
- [ ] Re-solve without looking at notes
- [ ] If still stuck, re-read only the "aha" line — not the full solution
- [ ] Update confidence score

## Pattern Cheat Sheet (fill in as you notice signals yourself)
| Signal in problem | Pattern | My note |
|---|---|---|
| Sorted array + pair/triplet | Two Pointers | |
| Contiguous subarray/substring + optimize | Sliding Window | |
| All subsets/permutations/combinations | Backtracking | |
| Shortest path, unweighted graph/grid | BFS | |
| Kth largest/smallest, top-K | Heap | |
| Overlapping subproblems | DP | |
| Range sum queries | Prefix Sum | |
| Next greater/smaller element | Monotonic Stack | |
| Linked list cycle / middle | Fast-Slow Pointers | |