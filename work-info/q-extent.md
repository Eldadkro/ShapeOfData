---
tags: 
	- invariant
	- 
---
is the maximum [[distance]] of the q-tuple 
$$ xt_qX = \frac{1}{C(n,2)} max_{(x_1,...,x_q)\in X^q} \sum d(x_i,x_j)$$
where q=2 : is the [[diameter of a graph]]

and the following inequality holds

$$ xt_2X \ge xt_3X \ge ... \ge xtX$$
where $xtX = lim_q xt_qX$


## Calculation

1) for a given $q$ calculate the sum of the weights of all the paths
2) use itertools to to quary all the tuples of length q