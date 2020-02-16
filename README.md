Data Bruteforcer
================

bruteforcer is a module for calculating all possible combinations of a dataset, calculate the sum
of one of the fields for all combinations and then identify those that add up within a certain
threshold to a "target" number.

The module uses numpy arrays to allow for better performance in comparison with using ordinary
python lists.

Simple Example:
---------------
    
   We are looking for a combination that sums 7 within the following universe:
    
    universe = [('A', 2), ('B', 1), ('C', 5)]
    
   When the module is fed with this data, it would return this result:
    
    result = [(('A', 2), ('C', 5), 0)]
   
   The last element in the previous list is the 'difference' to the target.


Usage:
-----
bruteforce(data: list[Tuple(Any, Int)], target_number: float, max_elements_to_combine: int)
```python
from bruteforcer import bruteforce

universe = [('A', 2), ('B', 1), ('C', 5), ('D', 10), ('E', 20)]
results = bruteforce(universe, 7.0, 5)
``` 

Performance
----------
On a Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz with 4 cores, the module is able to calculate 
32,837,266 in 35.9s (914k op/s).



To Do
=====
For big datasets further optimization is required to allow for parallel processing.