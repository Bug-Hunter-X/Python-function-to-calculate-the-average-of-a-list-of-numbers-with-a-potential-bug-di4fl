# Python Average Calculator with Bug Fix

This repository demonstrates a Python function designed to calculate the average of a list of numbers.  The initial version contains a bug related to handling non-numerical inputs. A corrected version is provided to illustrate a robust solution.

## Bug Description

The original `calculate_average` function does not explicitly check the data type of elements within the input list. This can lead to a `TypeError` exception if the list contains non-numerical values (e.g., strings).

## Solution

The bug is addressed by adding input validation to ensure that all elements in the list are numbers before performing the calculation. This is achieved using a `try-except` block and a type check within a loop.