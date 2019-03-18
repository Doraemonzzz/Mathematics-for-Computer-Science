#### Problem 1

| $R$ is       | iff $R^{-1}$ is |
| ------------ | --------------- |
| total        | a surjection    |
| a function   | an injection    |
| a surjection | total           |
| an injection | a function      |
| a bijection  | a bijection     |



#### Problem 2

$\forall (a_i, b_j) \in |A\times B|$，构造映射$f$，其中$f$将$(a_i, b_j)$映射为$(i+1)(j+1)-1=i+j+ij$，所以
$$
f(|A\times B|) = \{0,1,...,mn-1\}
$$



#### Problem 3

(a)
$$
|f(A)| \le |B|
$$
(b)
$$
|A|\ge |B|
$$
(c)
$$
|f(A)| =|B|
$$
(d)
$$
|f(A)| \le |A|
$$
(e)
$$
|A| =|B|
$$



#### Problem 4

因为函数有$\le 1$的out，所以
$$
|X|\ge |R(X)|
$$



#### Problem 5

(a)
$$
|A|\ge |B|\ge C \Rightarrow A\text{ surj }C
$$
(b)因为
$$
|A|\ge |B| \Leftrightarrow |B|\le |A|
$$
(c)由(a)，(b)可得
$$
A\text{ inj }B \Leftrightarrow B\text{ surf }A  \Leftrightarrow  |B| \ge |A| \\
B\text{ inj }C \Leftrightarrow C\text{ surf }B  \Leftrightarrow  |C| \ge |B|
$$
所以
$$
|C | \ge |A|
$$
因此
$$
A\text{ inj }C 
$$
(d)因为
$$
A\text{ inj } B
$$
等价于
$$
B\text{ surf }A
$$
等价于存在从$B$到$A$的surjective function $R$，由第一题可知$R^{-1}$为injective total relation，所以等价于存在从$A$到$B​$的injective total relation。