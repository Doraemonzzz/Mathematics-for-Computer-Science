#### Problem 1

如果结论不成立，假设$M,N$为两颗最小生成树，令$e$集合$(M-N)\cup (N-M)$中最短的边，不失一般性，假设$e\in M-N$，由定义可得$N\cup e$包含循环，不妨设该环为$R$，如果存在$r\in R$，并且$r>e$，那么$N\cup e -r$依然为生成树，但是长度更小，这就与$N$为最小生成树矛盾；如果$\forall r\in R,r< e$，那么因为$e$为属于$M$但不属于$N$的最短边，我们必然有$r\in N$，即$R\subseteq N$，所以$N$中包含一个环，这就与$N$为最小生成树矛盾。



#### Problem 2

(a)(b)画图即可验证这点。



#### Problem 3

(a)直接验证即可。

(b)因为
$$
(B_1, G_2),(B_2,G_1)
$$
也是stable matching，所以不是boy-pessimal。

因为
$$
(B_3, G_4),(B_4,G_3)
$$
也是stable matching，所以不是boy-optimal。

(c)只要按照提示分组即可，每组男生和对应的女生可以构成两种stable assignment，因为一共有$\frac n 2​$组，所以stable assignment的数量大于等于
$$
2^{\frac n 2}
$$
