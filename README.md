# Practical 3 – Dictionaries & Tuples

**Student:** Kartik Dayal  
**University:** Shoolini University  
**Assignment:** Practical 3 - Dictionaries & Tuples

## Overview

This repository contains my college assignment **Practical 3 – Dictionaries & Tuples**.

The practical is divided into two parts:

- Part A – Dictionaries
- Part B – Tuples

## Part A – Dictionaries

The dictionary section demonstrates:

1. Creating an empty dictionary.
2. Storing first product details in variables.
3. Adding the first product to an inventory dictionary.
4. Storing second product details in variables.
5. Adding the second product to the inventory.
6. Displaying products in the inventory.
7. Checking whether product release years are present in the product values.
8. Deleting the release year from both products.

The products used are **Mobile Phone** and **Laptop**.

## Part B – Tuples

The tuple section demonstrates:

1. Creating a `prices` tuple.
2. Finding the highest price.
3. Finding the lowest price.
4. Calculating the total sum.
5. Converting the tuple into a sorted list.
6. Attempting to modify a tuple element.

The submitted practical shows that modifying a tuple produces a `TypeError` because a tuple is immutable.

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python practical_3.py
```

## Expected Important Results

```text
Highest price: 400
Lowest price: 100
Total sum: 1750
Sorted list: [100, 150, 200, 250, 300, 350, 400]
```

The final attempted modification:

```python
prices[0] = 500
```

produces:

```text
TypeError: 'tuple' object does not support item assignment
```

## Student Submission

This repository contains both the executable Python source code and the submitted PDF practical record.
