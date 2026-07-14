# DSA Practice Log

Log every problem here, right after solving (or after reviewing the solution).
Keep entries short — 1-2 lines per field max. The goal is fast capture, not essays.

---

## Template (copy this block for each new problem)

### [Problem Name] — [NeetCode/LeetCode #]
- **Date:**
- **Topic/Pattern:** (e.g. Sliding Window, Two Pointers, BFS, DP-1D)
- **Signal I used to recognize it:** (what in the problem statement pointed here?)
- **Brute force approach:** (one line)
- **Optimized approach:** (one line)
- **Time / Space:**
- **Where I got stuck:** (be honest — this is the highest-value field)
- **The "aha" / trick:** (the one insight that unlocked it)
- **Confidence (1-5):** (1 = total blank, 5 = solved cleanly under time)
- **Revisit by:** (date — 1 week out if confidence ≤3)

---

## Entries

### Example: Longest Substring Without Repeating Characters — NC 3
- **Date:** 2026-07-14
- **Topic/Pattern:** Sliding Window
- **Signal I used to recognize it:** "contiguous substring" + "no repeating" = shrink/grow window
- **Brute force approach:** check all substrings, O(n^3)
- **Optimized approach:** expand right pointer, use set/map to detect repeats, shrink left when repeat found
- **Time / Space:** O(n) / O(min(n, charset))
- **Where I got stuck:** forgot to move left pointer to (last_seen_index + 1) instead of incrementing by 1
- **The "aha" / trick:** store last seen index, jump left pointer directly instead of looping
- **Confidence (1-5):** 3
- **Revisit by:** 2026-07-21

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