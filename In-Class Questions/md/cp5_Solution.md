#### Problem 1

上述命题分别编号为$1\sim 5$，结果如下表所示

|      | $\mathbb N$ | $\mathbb Z$ | $\mathbb Q$ | $\mathbb R$      | $\mathbb C$ |
| ---- | ----------- | ----------- | ----------- | ---------------- | ----------- |
| 1    | F           | F           | F           | T($\pm \sqrt 2$) | T           |
| 2    | T(显然)     | T           | T           | T                | T           |
| 3    | F           | F           | F           | F                | T(显然)     |
| 4    | F           | F           | T(显然)     | T                | T           |
| 5    | F           | F           | F           | F                | F           |



#### Problem 2

(a)
$$
\exists y\ (yyy=x)
$$
(b)
$$
\exists y, \text{NO-1 S}(y), yy=x
$$
(c)
$$
\text{NO-1 S}(x) \text { OR }(\text{NOT}(\text{SUBSTRING}(0, x))
$$
(d)
$$
x= 1 或\exists y,\text{NO-1 S}(y)，1y1= x
$$
(e)如果$x$只含有$0$或空字符串，则显然正确；否则至少含有一个$1$，假设第$k$位是$1$，那么$x$的前$k$位为
$$
\underbrace {0...0}_{k-1个0} 1
$$
$0x$的前$k$位为
$$
\underbrace {0...0}_{k个0}
$$
所以$x$不是$0x$的前缀，因此
$$
\text{PREFIX}(x, 0x)
$$
等价于$x$只含有$0$或空字符串，从而命题成立。



#### Problem 3

第一种情形是没人给自己发邮件
$$
\not \exists  x ,E(x,x)
$$
第二种情形为只给自己发邮件，前一部分表示存在某人给自己发邮件，第二部分表示唯一性
$$
(\exists x , E(x,x)) \land  (E(x,s)\to s=x)
$$
第三种情形为给除自己以外一个人发邮件
$$
(\exists x,y , E(x,y)) \land(E(x,s)\to (s=x) \or (s= y))
$$
第四种情形为给除自己以外两个人发邮件，注意此时要表示这两个人不同
$$
(\exists x,y,z , E(x,y)\land E(x, z)) \land \\
((x\neq y) \land (y\neq z)\land (x\neq z))\land \\
(E(x,s)\to ((s=x) \or( s= y)\lor (s= z))
$$



#### Problem 4

1错误，2正确。

1的反例：

取
$$
P(x,y) 为x>y
$$
此时
$$
\forall x. \exists y .P(x,y)恒成立
$$
但是不存在$y$，使得$\forall x$，满足
$$
x>y
$$
2的证明：

因为
$$
\exists y .\forall x.P(x,y)成立
$$
所以存在$y_0$，使得$P(x, y_0)$对任意$x$成立，也就是说，对任意$x$，$P(x, y_0)$成立，即
$$
\forall x.\exists y .P(x,y)成立
$$



#### Problem 5

(a)阴谋集团至少存在$3$个人

(b)Siggi和Annie至少有一个不在阴谋集团中

(c)如果Elizabeth在阴谋集团中，那么每个人都在阴谋集团中

(d)如果Annie在阴谋集团中，那么Siggi在阴谋集团中

(e)如果Ben和Albert至少有一个在阴谋集团中，那么Tom不在阴谋集团中

(f)如果Ben和Siggi至少有一个在阴谋集团中，那么Adam不在阴谋集团中

(g)根据上述结论推断谁在阴谋集团中

由c，e可知Elizabeth不在阴谋集团中；由b,d可知，Annie不在阴谋集团中。

如果Siggi在阴谋集团中，那么由f可知Adam不在阴谋集团中，如果Ben在阴谋集团中，那么由e可知，Tom不在阴谋集团中，由a可知，此时Albert在阴谋集团中；如果Ben不在阴谋集团中，此时已有$4$人不在阴谋集团中，结合a可知，Albert和Tom都在阴谋集团中，这就与e矛盾。

如果Siggi不在阴谋集团中；由e,f，如果Ben在阴谋集团中，那么Adam不在阴谋集团中，Tom不在阴谋集团中，此时有5人不在阴谋集团中，与a矛盾，所以Ben不在阴谋集团中，此时已有$4$人不在阴谋集团中，结合a可知，剩余$3$人都在阴谋集团中，这就与e矛盾，所以这种情形不会发生。

综上，阴谋集团的$3$人为Siggi，Ben，Albert。

