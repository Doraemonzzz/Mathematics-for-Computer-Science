#### Problem 1

(a)因为平均伴侣数量和男女人数有关，因此该命题错误。

(b)设伴侣的数量为$n$，那么
$$
\frac n m =1.1\times \frac n f \Rightarrow m 
=\frac {10}{11}  f
$$
(c)假设男性virgins的数量为$m_1$，女性virgins的数量为$f_1​$，那么
$$
m_1= \frac 1 {20} m,f_1 =\frac 1 5f
$$
nonvirgin male average number of partners为
$$
\frac{n}{m-m_1}=\frac n{\frac{19m}{20}}=\frac {20n}{19m}
$$
nonvirgin female average number of partners为
$$
\frac{n}{f-f_1}=\frac{n}{\frac{4f}{5}}
=\frac{5n}{4f}
$$
所以
$$
\frac{20n}{19m}/\frac {5n}{4f}  =\frac{16}{19}\frac f m
$$
因此
$$
x= \frac{16}{19}
$$
(d)因为可能是一对多关系。



#### Problem 2

(a)注意如下等式：
$$
2|E | = ∑_{v\in V} \text{deg}(v)
$$
如果度数为奇数的顶点有奇数个，那么违背上述等式。

(b)将人看成顶点，握过手的两人有边相连，那么握手的次数为顶点的度数，所以利用(a)即可。

(c)考虑所有从George开始的握手序列的节点构成的图，然后使用反证法：如果结论不成立，那么该图中只存在一个度数为奇数的节点，这就与(b)(c)矛盾。



#### Problem 3

$$
1\leftrightarrow a,
2\leftrightarrow b,
3\leftrightarrow c,
4\leftrightarrow d,
5\leftrightarrow e,
6\leftrightarrow f\\

1\leftrightarrow b,
2\leftrightarrow a,
3\leftrightarrow c,
4\leftrightarrow d,
5\leftrightarrow e,
6\leftrightarrow f\\

1\leftrightarrow a,
2\leftrightarrow b,
3\leftrightarrow d,
4\leftrightarrow c,
5\leftrightarrow f,
6\leftrightarrow e\\

1\leftrightarrow b,
2\leftrightarrow a,
3\leftrightarrow d,
4\leftrightarrow c,
5\leftrightarrow f,
6\leftrightarrow e\\
$$

考虑度数，所以$3,4$必然和$c,d$对应，因此其他点也可以随之确定。



#### Problem 4

(b)(c)(e)(f)(g)(i)(j)



#### Problem 5

(a)证明：

$\Rightarrow​$
$$
\forall h\in H(f(v))
$$
那么
$$
f(v)\to h
$$
由定义，可以假设
$$
h=f(h_1)
$$
所以
$$
f(v)\to f(h_1)\\
v\to h_1
$$
因此
$$
h_1\in G(v), h=f(h_1)\in f(G(v))
$$
$\Leftarrow​$
$$
\forall h\in f(G(v))
$$
假设
$$
h=f(h_1)
$$
那么
$$
h_1\in G(v)
$$
即
$$
v\to h_1\\
f(v)\to f(h_1)
$$
因此
$$
h=f(h_1)\in H(f(v))
$$
(b)因为$f$是双射，所以
$$
|G(v)| =|f(G(v))|=|H(f(v))|
$$

