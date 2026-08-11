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
- **Signal I used to recognize it:** Comparing two indices and updating it parallely
- **Brute force approach:** Preprocess the strings. Take two strings, iterate the input string from the back and from the front. Compare both
- **Optimized approach:** Using two pointers simulateiously and returning false even if one of the does not comply
- **Time / Space:** O(n)
- **Where I got stuck:** Preprocessing the string to exclude the non alphanumeric elements
- **The "aha" / trick:** Basically just by reading the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### Two Integer Sum II — TP 2
- **Date:** 2026-07-23
- **Topic/Pattern:** Two pointers
- **Signal I used to recognize it:** Comparing two indices and updating it parallely
- **Brute force approach:** Take nested for loops and look for all possible pairs which give the target. Which is O(n2)
- **Optimized approach:** Using two pointers as it is already sorted we update the start and end based on their sum being greater or lesser than target and return 
- **Time / Space:** O(n)
- **Where I got stuck:** The 1-indexed solution return. Had to add 1
- **The "aha" / trick:**  
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### 3Sum — TP 3
- **Date:** 2026-07-24
- **Topic/Pattern:** Two pointers
- **Signal I used to recognize it:** Comparing two indices and updating it parallely
- **Brute force approach:** Take nested for loops and look for all possible pairs which give the target. Which is O(n3)
- **Optimized approach:** We fix one element and now the target is -(number we fixed) Then using two pointers as it is already sorted we update the start and end based on their sum being greater or lesser than target and return 
- **Time / Space:** O(n2)
- **Where I got stuck:** The duplicate solution must not be added. This was brutal
- **The "aha" / trick:** It was just a two sum after fixing one element
- **Confidence (1-5):** 2
- **Revisit by:** 2026-07-28

### Container With Most Water — TP 4
- **Date:** 2026-07-25
- **Topic/Pattern:** Two pointers
- **Signal I used to recognize it:** Comparing two indices and updating it parallely
- **Brute force approach:** Take nested for loops and look for all possible pairs which give the target. Which is O(n2)
- **Optimized approach:** We take two pointer approach and check which height is less and move that pointer accordingly
- **Time / Space:** O(n)
- **Where I got stuck:** Handling the case when both the heights are equal
- **The "aha" / trick:** It was just a two sum after knowing we need to move both the pointers with a condition
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### Trapping rain water — TP 5
- **Date:** 2026-07-26
- **Topic/Pattern:** Two pointers
- **Signal I used to recognize it:** Honestly i did not know how to do it two pointers. So i could not recognixe it
- **Brute force approach:** We take prefix and suffix sum for that position calculate it and then use the minimum of prefix[i] and suffix[i] to get the trapped water
- **Optimized approach:** We take two pointers and maintain the leftmax and right max. We move the pointer which is minimum and proceed to add the trapped water to the variable
- **Time / Space:** O(n)
- **Where I got stuck:** Handling the two pointer approach. Could not even get the idea
- **The "aha" / trick:** When i got to know that we only need left max and right max of the current poisition not all.
- **Confidence (1-5):** 2
- **Revisit by:** 2026-07-28

### Valid Parentheses  — ST 1
- **Date:** 2026-07-27
- **Topic/Pattern:** Stack
- **Signal I used to recognize it:** Normally when anything want to be searched in the same order which they came in stack is the best DS for it
- **Brute force approach:** We insert the opening brackets, then pop each one out in the same order, if it doesnt comply then we return false
- **Optimized approach:** There is no optimized approach except we can use a hashmap also to get the mappings and use it instead of writing 3 if else statements
- **Time / Space:** O(n)
- **Where I got stuck:** Certain edge cases like ")" this returned nothing in my code
- **The "aha" / trick:** Basically just by reading the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### Min Stack  — ST 2
- **Date:** 2026-07-27
- **Topic/Pattern:** Stack
- **Signal I used to recognize it:** Normally when anything want to be searched in the same order which they came in stack is the best DS for it
- **Brute force approach:** We take currentmin variable and track the minimum while inserting into the stack.
- **Optimized approach:** We take a new array and push only when there is change in minimum, So when we pop we check whether minimum is popped or not, if yes we pop from the new stack too, if not it stays same
- **Time / Space:** O(1)
- **Where I got stuck:** No mistakes once got to know to use another stack track
- **The "aha" / trick:** Got to know when we have to maintain the minimum after every push and pop, we needed a stack 
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### Evaluate Reverse Polish Notation  — ST 3
- **Date:** 2026-07-27
- **Topic/Pattern:** Stack
- **Signal I used to recognize it:** Normally when anything want to be searched in the same order which they came in stack is the best DS for it
- **Brute force approach:** We insert the integers and when operand comes we pop the elements in tbe stack and perform the operation and push the result
- **Optimized approach:** There is no optimized approach 
- **Time / Space:** O(n)
- **Where I got stuck:** Wrong order for - and / because we have to do num2-num1 not num1-num2
- **The "aha" / trick:** Basically just by reading the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-07-28

### Daily Temperatures  — ST 4
- **Date:** 2026-07-28
- **Topic/Pattern:** Stack
- **Signal I used to recognize it:** We need decresing order which means monotonic stack
- **Brute force approach:** We check for the next large temperature and find the index of it and push it into the sol vector
- **Optimized approach:** We can use monotonic stack where we store indices and check whether the top of the stack is greater than the current element, If it is push it. If its not then we pop it find the index difference and store it in sol vector
- **Time / Space:** O(n)
- **Where I got stuck:** Got the basic logic but could not figure out we can store indices instead of temperatures
- **The "aha" / trick:** Basically just by reading the question
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-04

### Car Fleet  — ST 5
- **Date:** 2026-07-29
- **Topic/Pattern:** Stack
- **Signal I used to recognize it:** We need decresing order and one after the other, depends only on the car infront thats it
- **Brute force approach:** We sort and calculate the times and then iterate over all seeing which one is slower and faster for each pair.
- **Optimized approach:** We sort the elements and calculate the time. We push when only the current time is greater than the top of the stack. We return the stack size
- **Time / Space:** O(nlogn)
- **Where I got stuck:** The pair can be sorted or not. Basic implementation 
- **The "aha" / trick:** Because of previous problem of monotonic stack.
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-04

### Largest Rectangle In Histogram  — ST 6
- **Date:** 2026-08-04
- **Topic/Pattern:** Stack
- **Signal I used to recognize it:** We have to keep track of the left and right of the current index to get the maximum area. This is like trapping rain water
- **Brute force approach:** We calculate the left and right until we get smaller height and then stop to calculate the area
- **Optimized approach:** We use increasing stack where we push the indices until we get a smaller than the top and then pop until we get a bigger one and calculate the area simltaneously for every element popped and get the max area
- **Time / Space:** O(n)
- **Where I got stuck:** Had no idea about optimised approach. Need to practice more like this
- **The "aha" / trick:** Because of previous problem of monotonic stack.
- **Confidence (1-5):** 1
- **Revisit by:** 2026-08-11

### Binary Search  — BS 1
- **Date:** 2026-07-30
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** We use normal for loop and iterate over it to find the target element
- **Optimized approach:** We use binary search and reduce the search array by half every time we iterate which reduces the time by a factor of 2
- **Time / Space:** O(logn)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-04

### Search a 2D Matrix  — BS 2
- **Date:** 2026-07-30
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** We use nested for loops and iterate over it to find the target element but it is O(n2)
- **Optimized approach:** We can first find out which row the target is in by checking the first and last element of that row Then We use binary search and reduce the search array by half every time we iterate which reduces the time by a factor of 2
- **Time / Space:** O(nlogn)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-04

### Koko Eating Bananas  — BS 3
- **Date:** 2026-07-31
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** We can use to check everything from 1 to max(piles) in the piles array and calculate the total time and then proceed
- **Optimized approach:** We can use binary search and check whether mid is the rate which gives us less than the target time. If it does update the variable otherwise we change the start
- **Time / Space:** O(nlogm)
- **Where I got stuck:** Got stuck at calculating total time and got to the ceil function in CPP
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-04

### Find Minimum in Rotated Sorted Array  — BS 4
- **Date:** 2026-08-01
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** We can finf the pivot and check which side has the minimum element
- **Optimized approach:** We csn binary search as we know two of start, end or mid will always be on the same side
- **Time / Space:** O(logn)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 5
- **Revisit by:** 2026-08-04

### Search in Rotated Sorted Array  — BS 5
- **Date:** 2026-08-01
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** We can finf the pivot and check which side has the target and then do binary search on that half
- **Optimized approach:** We csn binary search as we know two of start, end or mid will always be on the same side
- **Time / Space:** O(logn)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 5
- **Revisit by:** 2026-08-04

### Time Based Key-Value Store  — BS 6
- **Date:** 2026-08-02
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** Everything is same but we use linear search instead of binary search
- **Optimized approach:** We use binary search and check anything <= given timestamp is the latest one and valid one
- **Time / Space:** O(logn)
- **Where I got stuck:** At getting the latest value if the timestamp is not equal to the one given
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-04

### Median of Two Sorted Arrays  — BS 7
- **Date:** 2026-08-03
- **Topic/Pattern:** Binary Search
- **Signal I used to recognize it:** Sorting in logn time is almost always binary search
- **Brute force approach:** Everything is same but we use linear search instead of binary search
- **Optimized approach:** We merge both the arrays and get the median with the help of nth_element.
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-04

### Best Time to Buy and Sell Stock  — SW 1
- **Date:** 2026-08-04
- **Topic/Pattern:** Sliding window
- **Signal I used to recognize it:** The most basic sliding window problem where we have to keep track of a window to buy and sell with a condition
- **Brute force approach:** Iterate through for loops and find the best time to buy and sell
- **Optimized approach:** Use sliding window to keep track of the max profit and the minimum to buy a stock
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Basically by looking at the question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Longest Substring Without Repeating Characters — SW 2
- **Date:** 2026-08-05
- **Topic/Pattern:** Sliding window
- **Signal I used to recognize it:** We have to calculate maximum continuous of something which generally means sliding window
- **Brute force approach:** We can iterate through the entire string until there is a duplicate, note the length and then incremenet to next charecter. Do it again and again
- **Optimized approach:** We can use sliding window where the invalid condition is if there is a repeating charecter, We can use a hash map to keep track and we move the left pointer until there is no duplicate in the substring and continue. We can take the maximum of all the values
- **Time / Space:** O(n)
- **Where I got stuck:** Looping through the left and right correctly and tracking the letters
- **The "aha" / trick:** moving the left pointer and updating the map simultaneously
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### Longest Repeating Character Replacement — SW 3
- **Date:** 2026-08-06
- **Topic/Pattern:** Sliding window
- **Signal I used to recognize it:** We have to calculate maximum continuous of something which generally means sliding window
- **Brute force approach:** We can check each substring and find out the maximum frequency in that substring and check whether the number of replacements will be less than or equal to k but that woulkd O(n2)
- **Optimized approach:** We can use sliding window approach where we keep track of max frequency of that window, we move right until the number of replacements we can to exceed k, then we shrink the window.
- **Time / Space:** O(n)
- **Where I got stuck:** Find max frequency without using a spearate function
- **The "aha" / trick:** moving the left pointer and updating the map simultaneously
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### Permutation in String  — SW 4
- **Date:** 2026-08-05
- **Topic/Pattern:** Sliding window
- **Signal I used to recognize it:** fixed size and check something inside the window is generally sliding window
- **Brute force approach:** We can iterate through the string and see if it is equal. That will O(n2) or even O(n3)
- **Optimized approach:** We can use a sliding wondow where the size is fixed to first string and we slide across the second string and check whether the maps are equal or not.
- **Time / Space:** O(n)
- **Where I got stuck:** Updating the maps simulataneously moving the pointer is somewhat tricky
- **The "aha" / trick:** Using hash maps to compare is perfect althogh they take space, maybe we can use vectors
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### Minimum Window Substring  — SW 5
- **Date:** 2026-08-06
- **Topic/Pattern:** Sliding window
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can iterate through each substring and check the condition but that would be O(n2)
- **Optimized approach:** We use sliding window and to keep track of the frequency we use hash map, We check whether our window hashmap contains the charecters which the tracking map has, We shrink when it until it doesnt and return the minimum
- **Time / Space:** O(n)
- **Where I got stuck:** Updating the maps simulataneously moving the pointer is somewhat tricky
- **The "aha" / trick:** Using hash maps to compare is perfect althogh they take space, maybe we can use vectors
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### Sliding Window Maximum — SW 6
- **Date:** 2026-08-06
- **Topic/Pattern:** Sliding window
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can iterate through each substring and check the condition but that would be O(n2)
- **Optimized approach:** We use sliding window with fixed window size and check max element for each window. It is O(n2) but the optimised approach is deque which i dont know yet
- **Time / Space:** O(n2)
- **Where I got stuck:** order of Pushing the elements and updating the variables 
- **The "aha" / trick:** Using hash maps to compare is perfect althogh they take space, maybe we can use vectors
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### Reverse Linked List — LL 1
- **Date:** 2026-08-07
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can take a new linked list and iterate backwards to create a reversed linked list but that takes up more space
- **Optimized approach:** We can keep track of the previous, current and the next pointers and traverse to change their direction
- **Time / Space:** O(n)
- **Where I got stuck:** Which pointer to return 
- **The "aha" / trick:** Basically the last pointer to leave is the pointer to return 
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Merge Two Sorted Linked Lists — LL 2
- **Date:** 2026-08-07
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can turn them into arrays and merge them and sort, then convert them to linked lists
- **Optimized approach:** We can initialise a dummy node and a tail to keep track and change the next pointers to the least element
- **Time / Space:** O(n)
- **Where I got stuck:** How to initialise a dummy vector in O(1) memory
- **The "aha" / trick:** Just initialise listnode instead of a ptr
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Linked List Cycle Detection — LL 3
- **Date:** 2026-08-08
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can use hash set to keep track of the addresses of the pointers, if it repeats we return true else false
- **Optimized approach:** We can use fast and slow pointers and iterate until one of the becomes null or they meet, If they meet we return true
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** With fast and slow pointers they will always meet when there is a loop.
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Reorder Linked List — LL 4
- **Date:** 2026-08-08
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can turn it into an array then use two pointers to create an new array. Then we turn it into a linked list
- **Optimized approach:** We use fast and slow pointers to get the middle element, then reverese the second part of the linked list. Then traverse it into a new linked list
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** Finding the middle element is an eye opening idea. Noticing the pattern is not easy
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Remove Nth Node From End of List — LL 5
- **Date:** 2026-08-08
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can turn it into an array then we remove the element at index i, then convert it into linked list
- **Optimized approach:** We calculate the length of the LL with iteration. Then we iterate until we get the nth element from the last and the delete it
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** There is no aha moment 
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Copy Linked List with Random Pointer — LL 6
- **Date:** 2026-08-09
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can use hashmap and keep track of all the pointers with old nodes. Then we create a new LL and attach the mapped random pointer to the new one
- **Optimized approach:** We can also attach the new pointers after the old node and we can find the random because the new nodes would be next to the old nodes then we split the new nodex separately
- **Time / Space:** O(n)
- **Where I got stuck:** How to create the new nodes syntax
- **The "aha" / trick:** Using hashmap to map it and then use it is a good idea
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### Add Two Numbers — LL 7
- **Date:** 2026-08-10
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can convert the LL into array of integers, add them and convert them to linked lists again
- **Optimized approach:** We can create new nodes and a new LL with the added values
- **Time / Space:** O(n)
- **Where I got stuck:** Did not get stuck
- **The "aha" / trick:** No particular aha moment. It was a straightforward question
- **Confidence (1-5):** 4
- **Revisit by:** 2026-08-11

### Find the Duplicate Number — LL 8
- **Date:** 2026-08-10
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can use hashset to check which element is coming more than once. Or else we can mark the index as negative when we visit as the elements are always between 1 and len(nums). if it is already negative, which means it is already visited then we return that index
- **Optimized approach:** We can treat it as LL, then we can use fast and slow pointers to find the element as it will form a loop if there is a duplicate
- **Time / Space:** O(n)
- **Where I got stuck:** How to point it to the next element without using pointers
- **The "aha" / trick:** Finding the element rather than if it is a loop or not.
- **Confidence (1-5):** 3
- **Revisit by:** 2026-08-11

### LRU Cache — LL 9
- **Date:** 2026-08-11
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can use arrayList and hashmap to keep track and change the LRU easily but it takes memory O(n)
- **Optimized approach:** We can use hashmap to keep track of the key and the pointer pointing to the key, value pair. Using a doubly linked list we can track LRU and MRU with two pointers always pointing to the LRU and the right to the MRU
- **Time / Space:** O(n)
- **Where I got stuck:** Initialising the variables is a nightmare
- **The "aha" / trick:** Using left and rights pointers to always track and slide for LRU is efficient
- **Confidence (1-5):** 2
- **Revisit by:** 2026-08-11

### Merge K Sorted Linked Lists — LL 10
- **Date:** 2026-08-11
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** We can use merge two lists function, and merge each list one by one by storing it and moving to next one.
- **Optimized approach:** We can use divide and conquer method where we recursively call the divide function to split the lists and then use ,merge two lists function to conquer it 
- **Time / Space:** O(n)
- **Where I got stuck:** Optimized approach idea
- **The "aha" / trick:** D & C is a game changer whenever we can think to split rather than sequentially solve it
- **Confidence (1-5):** 2
- **Revisit by:** 2026-08-11

### Reverse Nodes in K-Group — LL 11
- **Date:** 2026-08-11
- **Topic/Pattern:** Linked list
- **Signal I used to recognize it:** Just by looking at the question
- **Brute force approach:** Split all of them into size of k, reverse all of them and then koin them. This takes O(n2)
- **Optimized approach:** We can keep track of the currhead, currtail, previoustail and nexthead. This will help us in reversing and joining simulataneously.
- **Time / Space:** O(n)
- **Where I got stuck:** Optimized approach idea
- **The "aha" / trick:** I first though we have to divide the LL into two and solve but then I realised there can be multiple lists
- **Confidence (1-5):** 2
- **Revisit by:** 2026-08-11
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