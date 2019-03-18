#### Problem 1

利用数学归纳法，$k=0$时，
$$
F_k = 0 = \frac{p^0 -q^0}{\sqrt 5}
$$
假设$k\le n$时结论成立，那么当$k=n+1$时，
$$
\begin{aligned}
F_{n+1}
&= F_{n}+F_{n-1}\\
&=  \frac{p^n -q^n}{\sqrt 5} + \frac{p^{n+1} -q^{n+1}}{\sqrt 5} \\
&= \frac{p^n(1+p)- q^n (1+q)}{\sqrt 5} \\
&=\frac{p^n p^2- q^n q^2}{\sqrt 5} \\
&=\frac{p^{n+1}- q^{n+1} }{\sqrt 5}
\end{aligned}
$$
注意这里使用了如下结论：
$$
p^2 =p+1 ,q^2 =q+1
$$
所以$k=n+1$时结论也成立。



#### Problem 2

构造如下命题：
$$
R(n)::=假设A到B是由n步产生，那么P(A)\ge  P(B)\\
Q(n)::=假设A到B是由n步产生，那么产生的得分为P(A)- P(B)
$$
当$k=0$时结论显然，

当$k=1$时，因为是$1$步产生，假设将$a+b$拆分成$a$和$b$，那么得分为
$$
ab
$$
注意到
$$
\begin{aligned}
P(A)-P(B)
&= \frac{(a+b)(a+b-1)}{2}-\frac{a(a-1)}{2}-\frac{b(b-1)}{2}\\
&=\frac{a^2+2ab+b^2 -a-b -a^2+a -b^2 +b}{2}\\
&=ab\\
&\ge 0
\end{aligned}
$$
所以$k=1$时结论成立。

假设$k\le n$时结论成立，那么$k=n+1$时，假设$A$由$n$步产生$C$，再$C$由$1$步产生$B$，那么
$$
P(B)\ge P(C)\ge P(A)
$$
并且$A$到$C$产生的得分为$P(C)-P(A)$，$C$到$B$产生的得分为$P(B)-P(C)$，所以总得分为
$$
P(C)-P(A) + P(B)-P(C)=P(B)-P(A)
$$
所以$k=n+1$时结论也成立。



#### Problem 3

surjective表示满射，injective表示单射。

(a)成立，因为$h$是surjective，所以$\forall y \in C$，存在$x$，使得
$$
y= h(x)=f(g(x))
$$
这说明$f$是surjective。

(b)不一定。

(c)不一定。

(d)如果$g$不是injective（单映），不妨设$x_1\neq x_2$，但是$g(x_1)= g(x_2)$。注意$f$是total，结合$f$是函数，所以$f(g(x_1))$有意义，因此
$$
h(x_1)= f(g(x_1))= f(g(x_2)) =h(x_2)
$$
这就与$h​$是injective矛盾。