### Chapter 1 What is a Proof? 

#### Problem 1.1 

(a)按照下图组合即可：

![](https://github.com/Doraemonzzz/Mathematics-for-Computer-Science/blob/master/photo/Chapter%201/C1P1a.png?raw=true)

(b)按照下图组合即可：

![](https://github.com/Doraemonzzz/Mathematics-for-Computer-Science/blob/master/photo/Chapter%201/C1P1b.png?raw=true)

(c)如果$a=b$，那么上图就变成一个变成为边长为$a$和$2a$的矩形，面积为$2a^2$，此时的等式为$2a^2 = a^2 + b^2 =c^2$，依旧符合勾股定理。

(d)(a)，(b)两问中计算面积都利用到直角以及直线的条件。



#### Problem 1.2

(a)下面这一步出错，不能直接拆开
$$
\sqrt{(-1)(-1)} = \sqrt{(-1)}\sqrt{(-1)}
$$
(b)两边同除$2 $可得
$$
\frac 1  2 = - \frac 1 2 
$$
两边加上$\frac 3 2 $可得
$$
2=  1
$$
(c)利用平方根的定义验证即可
$$
rs=\sqrt{rs} \times \sqrt{rs} = r\times s = \sqrt r \times\sqrt r  \times \sqrt s  \times \sqrt s
= (\sqrt r \sqrt s )\times (\sqrt r \sqrt s )
$$
从而
$$
\sqrt{rs} = \sqrt r \sqrt s 
$$



#### Problem 1.3

(a)第二步错误，因为$\log_{10} {\frac 1 2 } < 0$

(b)第二步错误，美元是带单位的，平方后单位都不同，显然不相等

(c)倒数第三步到倒数第二步有问题，要讨论消去的项是否为$0$



#### Problem 1.4

第二步到第三步不等价，因为满足第三步等价于
$$
(2\sqrt{ab} - a-b)(2\sqrt{ab} +a+b) \le  0\\
-a-b\le 2\sqrt{ab} \le a+b
$$
要在这一步利用$a>0,b>0$，将上式化为
$$
2\sqrt{ab} \le a+b
$$
最简单的推导方法是利用$(\sqrt{a}- \sqrt{b})^2 \ge 0$



#### Problem 1.5

我的理解是第一步假设就有问题，因为如果学生默认在周五不会有测验，那么在周五有测验本身就是个惊喜。



#### Problem 1.6

如果$n= 7^s,s\in \mathbb N$，那么$\log_7 n = s \in \mathbb N$；否则可以假设$n= 7^s t, s,t\in \mathbb N, 7\nmid t$，那么$\log_7 n = s+ \log_7 t$，接下来证明$\log_7 t$为无理数，利用反证法，假设$\log_7 t = \frac pq $，$p,q$为整数且互质，那么
$$
q\log_7 t = p\\
\log_7 t^q = p \\
t^q = 7^p
$$
这说明$7 \mid t^q$，因为$7$为质数，这说明$7\mid t$，这就与$7\nmid t$矛盾，从而$\log_7 t$为无理数，因此当$n= 7^s t$时，$\log_7 n$为无理数



#### Problem 1.7

结论如下：
$$
无理数的无理次方可能为有理数
$$
考虑$\sqrt{2}^{\sqrt 2}$，如果$\sqrt{2}^{\sqrt 2}$为有理数，那么结论成立，否则$\sqrt{2}^{\sqrt 2}$为无理数，此时考虑$(\sqrt{2}^{\sqrt 2})^\sqrt 2  = \sqrt 2 ^{\sqrt 2 \sqrt 2 }=\sqrt 2 ^2 = 2$，那么结论依旧成立，这就说明了无理数的无理次方可能为有理数。

关于此有一个更强的结论：
$$
几乎所有 (1, ∞) 里的有理数都是某个无理数 a 的 a 次方
$$
参考链接：http://www.matrix67.com/blog/archives/4984



#### Problem 1.8

反证法，如果$a$是奇数，那么$a= 2k+1 ,k\in \mathbb N$，那么$a^n = ( 2k+1)^n$，所以$2\nmid a^n$，这就产生了矛盾



#### Problem 1.9

反证法，如果结论不成立，那么$a> \sqrt n$且$b > \sqrt n$，因此$ab > n$，这就产生了矛盾



#### Problem 1.10

这里证明一个更强的结论：
$$
任取质数p，如果p\mid n^2，那么p\mid n
$$
利用反证法，如果$p\nmid n$，那么$n=kp + r ,0< r \le p-1$，从而$n^2 = (kp+r)^2= k^2p^2 + 2kpr + r^2$，因为$p\mid n^2$，所以$p\mid r^2$，而$p$是质数，这说明$p\mid r$，这就与$0< r \le p-1$矛盾



#### Problem 1.11

取$m=4,n=2$，那么$m \mid n^2$，但是$m\nmid n$

如果$m<n$，取$m=4, n =6$，那么$m \mid n^2$，但是$m\nmid n$



#### Problem 1.12

这里证明更强的结论：
$$
对于任意素数p,\sqrt p 都是无理数
$$
利用反证法证明，如果$\sqrt p$是有理数，那么$\sqrt p  =\frac m n ,m,n\in \mathbb N且m,n互质$，平方可得
$$
p =\frac{m^2}{n^2} \\ 
p n^2 = m^2
$$
所以$p\mid m^2$，由Problem 1.10可得$p\mid m$，从而$m=pm_1$，带入上式可得
$$
pn^2= p^2 m_1 ^2 \\
n^2 = pm_1^2
$$
这说明$p\mid n^2$，$p\mid n$，这就与$m,n$互质矛盾



#### Problem 1.13

利用反证法，假设$\log_4 6  =\frac m n ,m,n\in \mathbb N且m,n互质$，那么
$$
n\log_4 6  =m\\
\log_4 6^n = m\\
6^n = 4^m\\
3^n = 2^{2m-n}
$$
最后一步显然不可能，所以$\log_4 6 $是无理数



#### Problem 1.14

(a)假设$\sqrt 2$是有理数，选择最小的正整数$q$，使得$(\sqrt 2 -1)q$是非负整数，令$q' =(\sqrt 2- 1)q$，显然有$q' <q$，此外，我们我们还有

$$
(\sqrt 2 - 1) q' = (\sqrt 2 - 1)^2 q= (3-2\sqrt 2 ) q = q +2(1-\sqrt 2 )q
$$
因为$(\sqrt 2 -1)q$是整数，所以$q +2(1-\sqrt 2 )q$也是整数，从而$(\sqrt 2 - 1) q'$是整数，非负性是显然的，所以$(\sqrt 2 - 1) q'$是非负整数，这就与$q$是使得$(\sqrt 2 -1)q$是非负整数的最小正整数矛盾，因此$\sqrt 2$是无理数

(b)这种证明技巧性比较强，不如课本上的方法直接



#### Problem 1.15

(a)取$a_0 =-k,a_i=0(i=1,...,m-1)$，那么该方程的解为
$$
x = k^{\frac 1 m }
$$
如果$k\neq k_0 ^{m}$，那么$x$不是整数，从而由引理可知$x = k^{\frac 1 m }$为无理数

(b)只要证明该方程没有形如$x=\frac p q,q\neq 1,p,q$互质的解即可，利用反证法，假设有这样的解，带入上式可得
$$
\sum_{i=0}^m a_i (\frac p q)^i = 0
$$
两边同乘$q^m$可得
$$
\sum_{i=0}^m a_i p^i q^{m-i} = 0 \\
a_0 q^m+a_1 pq^{m-1}+...+ a_{m-1}p^{m-1}q + p^m=0
$$
因为$0$被$q$整除，所以左边也被$q$整除，除去最后一项都是$q$的倍数，所以
$$
q \mid p^m
$$
由于$p,q$互质，这说明$q=1$，与假设矛盾，所以原结论成立



#### Problem 1.16

反证法，假设$2\log_2 3$为有理数，那么$2\log_2 3=\frac p q,p,q$互质，因此
$$
q \log_2 9 = p\\
 \log_2 9^q = p\\
 9^q = 2^p
$$
左右两边奇偶性不同，显然不可能相等，所以$2\log_2 3$为无理数



#### Problem 1.17

(a)将多项式写出来，假设次数为$k$，那么
$$
q(n)= \sum_{i=0}^k c_i n^i，c_0=q(0)=c
$$
从而
$$
q(cm)=\sum_{i=0}^k c_i (cm)^i= \sum_{i=1}^k c_i (cm)^i + c
$$
因此
$$
c\mid q(cm)
$$
(b)利用(a)即可，因为$c\mid q(cm)$且$c>1$，所以$q(cm)$不是质数，因为$m\in \mathbb Z$，注意$q(n)$不是常数，所以有无穷多个$n$，使得$q(n)$不是质数

(c)只要考虑$c=1$或$c=0$即可，如果$c=0$，那么多项式的形式如下
$$
q(n) =n(\sum_{i=0}^k a_i x^k)
$$
结论显然成立。

如果$c=1$，那么$q(0)=c = 1$不是质数，此时结论也成立。

综上，对于任意整系数多项式$q(n)$，存在$n\in \mathbb N$，使得$q(n)$不是质数。



#### Problem 1.18

反证法，假设$\log_9 12$为有理数，那么$\log_9 12=\frac p q,p,q$互质，因此
$$
q\log_9 12=p\\
\log_9 12^q=p \\
12^q= 9^p \\
2^{2q}\times 3^q = 3^{2p}\\
2^{2q} = 3^{2p-q}
$$
左右两边奇偶性不同，显然不可能相等，这就产生了矛盾



#### Problem 1.19

反证法，假设$\log_{12} 18$为有理数，那么$\log_{12} 18=\frac p q,p,q$互质，因此
$$
q\log_{12} 18=p\\
\log_{12} 18^q = p\\
12^p = 18^q\\
2^{2p}\times 3^p = 3^{2q} \times 2^q \\
3^{p-2q} = 2^{q-2p}
$$
左右两边奇偶性不同，显然不可能相等，这就产生了矛盾