# Greedy Algorithms – Problem Mapping to LeetCode

This document lists classic greedy problems along with their closest LeetCode counterparts. Each problem is stated as given, followed by a brief clarification of what is being asked.

---

## 1. Car Fueling Problem (Minimum Refills)

### Original Problem

You are going to travel to another city that is located d miles away from your home city. Your car can travel at most m miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1 , stop2 , . . . , stop n from your home city. What is the minimum number of refills needed?

### What it asks

Determine the minimum number of times you must refill fuel so that you can reach the destination.

### Closest LeetCode Problem

* LeetCode 871 – Minimum Number of Refueling Stops

---

## 2. Maximum Advertisement Revenue

### Original Problem

You have n ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up n slots on your page and estimated the expected number of clicks per day for each slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

### What it asks

Assign ads to slots such that total revenue (pay per click × expected clicks) is maximized.

### Closest LeetCode Problem

* LeetCode 1710 – Maximum Units on a Truck

---

## 3. Collecting Signatures (Minimum Points to Cover Segments)

### Original Problem

You are responsible for collecting signatures from all tenants of a certain building. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as possible. The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each segment contains at least one marked point.

### What it asks

Choose the minimum number of points such that every segment contains at least one of the chosen points.

### Closest LeetCode Problem

* LeetCode 452 – Minimum Number of Arrows to Burst Balloons

---

## 4. Maximum Number of Prizes (Distinct Summands)

### Original Problem

You are organizing a funny competition for children. As a prize fund you have n candies. You would like to use these candies for top k places in a competition with a natural restriction that a higher place gets a larger number of candies. To make as many children happy as possible, you are going to find the largest value of k for which it is possible.

### What it asks

Find the maximum number of winners k such that candies can be distributed with strictly increasing amounts.

### Closest LeetCode Problem

* LeetCode 2358 – Maximum Number of Groups Entering a Competition

---

## 5. Largest Number from Integers

### Original Problem

As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number. How can you do this?

In the lectures, we considered the following algorithm for composing the largest number out of the given single-digit numbers.

LargestNumber(Digits):
answer ← empty string
while Digits is not empty:
maxDigit ← −∞
for digit in Digits:
if digit ≥ maxDigit:
maxDigit ← digit
append maxDigit to answer
remove maxDigit from Digits
return answer

Unfortunately, this algorithm works only in case the input consists of single-digit numbers. For example, for an input consisting of two integers 23 and 3 (23 is not a single-digit number!) it returns 233, while the largest number is in fact 323. In other words, using the largest number from the input as the first number is not a safe move.

Your goal in this problem is to tweak the above algorithm so that it works not only for single-digit numbers, but for arbitrary positive integers.

### What it asks

Rearrange the given numbers to form the largest possible concatenated number.

### Closest LeetCode Problem

* LeetCode 179 – Largest Number

---

## 6. Fractional Knapsack

### Original Problem

A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.

### What it asks

Select items (possibly taking fractions) to maximize total value within a limited capacity.

### Closest LeetCode Problem

* LeetCode 1710 – Maximum Units on a Truck

---

## Summary Table

| # | Original Problem      | LeetCode Mapping |
| - | --------------------- | ---------------- |
| 1 | Car Fueling           | 871              |
| 2 | Ad Revenue            | 1710             |
| 3 | Collecting Signatures | 452              |
| 4 | Maximum Prizes        | 2358             |
| 5 | Largest Number        | 179              |
| 6 | Fractional Knapsack   | 1710             |
