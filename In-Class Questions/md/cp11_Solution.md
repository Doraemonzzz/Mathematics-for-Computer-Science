#### Problem 1

(a)该证明没什么问题。

(b)同(a)，我们可以取出$a_0,a_1,...,a_n,...$，现在构造如下映射：
$$
f(a_n)= n ,n\in \mathbb N \\
f(a)=0,a\in A- \{a_0,a_1,...\}
$$



#### Problem 2

证明：因为$f:\mathbb N \to S$是满射，所以$\forall s \in S$，存在$n\in \mathbb N$，使得
$$
s=f(n)
$$
现在可以按如下方式列出$S​$中的元素：

- 初始化$A=\{\} ​$

- 对$n=0,1,...,...$

  - 如果$f(n)$有定义，且$f(n)\notin A$，那么列出$f(n)$，并且令

  $$
  A= A\cup f(n)
  $$



#### Problem 3

(a)将$(i,j)$映射到$\frac i j $，那么这是一个满射。

(b)按对角线方法列出$(i,j)$，即对$n=2,...$，列出
$$
(1,n-1),(2, n-2),...,(n-1, 1)
$$
这样就可以将所有的$(i,j)$列出，因此$\mathbb Z^+ \times \mathbb Z^+ $可列，由(a)和上一题可知，正有理数集可列。



#### Problem 4

(a)假设输入是字符串$a$，可以用如下递归算法处理：

- 如果$a$的长度为$1$，返回False。
- 如果$a$的长度为$2$：
  - 如果$a[0]=a[1]$，返回True。
  - 否则返回Fasle。
- 如果$a$的长度大于$2$：
  - 如果$a[0]=a[1]$，那么对$a[2:]$重复运行该算法。
  - 否则返回Fasle。

(b)$\forall s\in \text{range}(f)​$，必然存在$s_1​$，使得
$$
f(s_1)=\mathcal s
$$
所以$P_{s_1}$可以识别$s$中全体字符串，这就说明$ \text{range}(f)$是全体可识别的字符串集合全体。

(c)如果$\mathcal N​$是可识别的，那么存在$s_1​$，使得
$$
f(s_1)=\mathcal N
$$
那么由定义可知，$\forall s\in \text{string}​$
$$
s\in f(s_1)\mathcal \Leftrightarrow s \notin f(s)
$$
取$s=s_1​$，我们有
$$
s_1\in f(s_1)\mathcal \Leftrightarrow s_1 \notin f(s_1)
$$
这就产生了矛盾，这说明$\mathcal N$是不可识别的。

(d)因为对于每个“program analyzers”，我们都可以定义上述的$\mathcal N$，使得$\mathcal N​$不可识别，这说明无法设计出完美的“program analyzers”。