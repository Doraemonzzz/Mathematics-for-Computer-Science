#### Problem 1

这里直接计算结果。

(a)
$$
C_7^2 \times 5!
$$
(b)
$$
6\times C_7^2 \times 5!
$$
(c)
$$
6\times 5\times 4 \times C_7^2 \times 
 C_5^2
$$



#### Problem 2

(a)一共$5$个元音字母，剩下有$21$个非元音字母，这部分先排列，总数为$21!$，元音字母从除了最后一个间隔以外$21$个间隔内进行排列，总数为$P_{21}^5$，所以总数为
$$
21!\times P_{21}^5
$$
(b)利用减法即可：
$$
26!-  21 ! \times P_{22}^5
$$
(c)
$$
(2n-1)!!
$$
(d)每种type可以唯一对应一个递增的序列：
$$
0\le y_1\le \ldots \le y_8 \le 9
$$
回顾in class question 25的第三题可得总数为
$$
C_{17}^8
$$



#### Problem 3

(a)只要证明当$k_i <p ,i=1,\ldots ,n​$时，我们有
$$
p\Big|\left( \begin{array}{c}{p} \\ {k_{1}, k_{2}, \ldots, k_{n}}\end{array}\right)
$$
即可。事实上，因为
$$
\left( \begin{array}{c}{p} \\ {k_{1}, k_{2}, \ldots, k_{n}}\end{array}\right)= 
\frac{p!}{\prod_{i=1}^n k_i !} =p\frac{(p-1)!}{\prod_{i=1}^n k_i !}
$$
因为$p$是质数，所以$k_i <p$时，我们有
$$
(k_i! , p)=1
$$
所以
$$
(\prod_{i=1}^n k_i ! ,p)=1
$$
由组合数的定义可知
$$
\prod_{i=1}^n k_i ! \big | p\times (p-1)!
$$
所以
$$
\prod_{i=1}^n k_i ! \big | (p-1)!
$$
因此
$$
\frac{(p-1)!}{\prod_{i=1}^n k_i !}
$$
是整数，由此
$$
p\Big|p\frac{(p-1)!}{\prod_{i=1}^n k_i !}=\left( \begin{array}{c}{p} \\ {k_{1}, k_{2}, \ldots, k_{n}}\end{array}\right)
$$
(b)取$x_i=1$可得
$$
n^p \equiv n \mod p
$$
所以
$$
p| (n^p-n)=n(n^{p-1}-1)
$$
因为$n$不是$p$的倍数，并且$p$是质数，所以
$$
(n,p)=1
$$
因此
$$
p| n^{p-1}-1
$$
即
$$
n^{p-1} \equiv 1 \mod p
$$
