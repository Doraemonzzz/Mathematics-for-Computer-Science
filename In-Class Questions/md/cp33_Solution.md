#### Problem 1

(a)反证法，如果有超过$\frac 3 4$的牛存活，那么平均体温大于
$$
\frac 3 4\times 90 + \frac 1 4 \times 70=85
$$
(b)$300$头牛是的体温为$90$；其余$100$头牛的体温是$70$即可。

(c)记牛的体温为$T$，那么
$$
\begin{aligned}
T& \ge 70\\
\mathbb E[T] & =85
\end{aligned}
$$
所以
$$
\begin{aligned}
\mathbb P[T \ge 90]
&= \mathbb P[T-70 \ge 20]\\
&\le  \frac{\mathbb E[T-70]}{ 20}\\
& = \frac{15}{20}\\
& =\frac 3 4
\end{aligned}
$$



#### Problem 2

(a)记draw poker每天赢的胜场为$X_1$，black jack每天赢的胜场为$X_2$，stud poker每天赢的胜场为$X_3$。那么每天赢的胜场为
$$
X=X_1+X_2+X_3
$$
因此
$$
\begin{aligned}
\mathbb E[X]
&=\sum_{i=1}^3 \mathbb E[X_i]\\
&= 20+30 + 4\\
&=54
\end{aligned}
$$
(b)
$$
\begin{aligned}
\mathbb E[X \ge 108] 
&\le \frac{\mathbb E[X]}{108}\\
&= \frac 1 2
\end{aligned}
$$
(c)由两两独立可得
$$
\begin{aligned}
\text{Var}(X)
&= \sum_{i=1}^3 \text{Var}(X_i)\\

&\approx 34.87
\end{aligned}
$$
(d)
$$
\begin{aligned}
\mathbb E[X \ge 108] 
&= \mathbb E[X-54\ge 54]\\
&\le \frac{\text{Var}(X)}{54^2}\\
&\approx 0.0119570
\end{aligned}
$$



#### Problem 3

(a)
$$
\begin{aligned}
\mathbb E[S_n]
& =\sum_{i=1}^n \mathbb E[X_i] \\
&=\sum_{i=1}^n\frac 1n \\
&=1
\end{aligned}
$$
(b)
$$
\begin{aligned}
\mathbb E[X_i X_j]
&= \mathbb P[X_i =1]\mathbb P[X_j=1 |X_i=1]\\
&=\frac 1 n\times \frac 1 {n-1}\\
&=\frac 1{n(n-1)}
\end{aligned}
$$
(c)因为
$$
\mathbb P[X_i=1, X_j=1]
=\frac 1 {n(n-1)}\ne \frac 1 n \times \frac 1 n
$$
(d)
$$
\begin{aligned}
\mathbb E[S_n^2]
& = \mathbb E 
\left[\left(\sum_{i=1}^n X_i\right)^2\right]\\
&=\sum_{i=1}^n \mathbb E[X_i^2]+\sum_{i\neq j}\mathbb E[X_i X_j]\\
&=\sum_{i=1}^n \mathbb E[X_i]+\sum_{i\neq j}\mathbb E[X_i X_j]\\
&=1 + {n(n-1)} \times  \frac 1{n(n-1)}\\
&=2
\end{aligned}
$$
(e)
$$
\begin{aligned}
\text{Var}(S_n)
& =\mathbb E[S_n^2] - \mathbb E[S_n]^2\\
&=2-1\\
&=1
\end{aligned}
$$
(f)
$$
\begin{aligned}
\mathbb P[S_n \ge 11]
&= \mathbb P[S_n -1\ge 10]\\
&\le \frac{\text{Var}(S_n)}{10^2}\\
&=\frac 1 {100}
\end{aligned}
$$





#### Problem 4

(a)由独立性可得
$$
m =6rbg
$$
(b)
$$
\begin{aligned}
\mathbb E[I_T]& =m\\
&=6rgb\\
\text{Var}(I_t) & =6m(1-6m)\\
&=6rgb(1-6rgb)
\end{aligned}
$$
(c)如果不共享边，那么该概率为
$$
p_1 = m^2 =36r^2b^2g^2
$$
如果共享边，那么该概率为
$$
p_2= r\times(2bg)^2 +g\times(2br)^2 +b\times(2rg)^2
$$
(d)如果
$$
r=b=g=\frac{1}{3}
$$
那么
$$
\begin{aligned}
\mathbb E[I_T]&=m \\
&= \frac{2}{9}\\

\text{Var}(I_t) 
&=m(1-m)\\
&=\frac {14}{81} \\

p_1 &= \frac{4}{81} \\
&=p^2\\

p_2 & = 12\times \frac{1}{3^5}\\
&=\frac{4}{81}\\
&=p_1\\
&=p^2
\end{aligned}
$$
所以独立。

(e)显然有
$$
M=\sum_{T} I_T
$$
而三角形的数量为
$$
\binom n3 =\frac{n(n-1)(n-2)}{6}
$$
所以
$$
\begin{aligned}
\mathbb E[M]
& = \sum_{T}\mathbb E[I_T]  \\
& =\frac{mn(n-1)(n-2)}{6}  \\
&=\frac{n(n-1)(n-2)}{6}\times \frac 2 9 \\
&=\frac{n(n-1)(n-2)}{27}\\

\text{Var}(M) & = \sum_{T}\text{Var}(I_T)\\
&=\frac{m(1-m)n(n-1)(n-2)}{6} \\
&=\frac{n(n-1)(n-2)}{6} \times \frac {14}{81}\\
&=\frac{7n(n-1)(n-2)}{243}
\end{aligned}
$$
(f)注意我们有
$$
\begin{aligned}
\text{Var}(M)
&= \frac{m(1-m)n(n-1)(n-2)}{6}\\
&<\frac{mn(n-1)(n-2)}{6}  \\
&= \mathbb E[M]
\end{aligned}
$$
所以
$$
\begin{aligned}
\mathbb P[|M-\mu|>\sqrt{\mu \log \mu}]
&\le \frac{\text{Var}(M)}{\mu \log \mu}\\
&<\frac{\mathbb E[M]}{\mu \log \mu}\\
&=\frac{\mu}{\mu \log \mu}\\
&=\frac 1 {\log \mu}
\end{aligned}
$$
(g)当$n\to\infty​$时，我们有
$$
\mu =\mathbb E[M]= \frac{n(n-1)(n-2)}{27}\to \infty
$$
所以
$$
\frac 1 {\log \mu} \to 0
$$
因此
$$
\lim_{n\to\infty}\mathbb P[|M-\mu|>\sqrt{\mu \log \mu}]  =0
$$



#### Problem 5

(a)答案是可以趋于无穷，构造如下：
$$
\begin{aligned}
\mathbb P[R=i] &=\frac 4 {i(i+1)(i+2)} ,i \in \mathbb N
\end{aligned}
$$
下面分别验证条件：
$$
\begin{aligned}
\sum_{i=1}^\infty \mathbb P[R=i] &=\sum_{i=1}^\infty \frac 4 {i(i+1)(i+2)}\\
&= 2\sum_{i=1}^\infty \left(\frac{1}{i(i+1)} - \frac {1}{(i+1)(i+2)}\right) \\
&=2 \sum_{i=1}^\infty \left(\frac{1}{i(i+1)} - \frac {1}{(i+1)(i+2)}\right) \\
&= 2\times \frac 1 2 \\
&=1\\

\mathbb E[R]
&=\sum_{i=1}^\infty \mathbb P[R=i]\times  i\\
&=\sum_{i=1}^\infty \frac 4 {(i+1)(i+2)}\\
&= 4\sum_{i=1}^\infty \left(\frac{1}{i+1} - \frac {1}{i+2}\right) \\

&= 4\times \frac 1 2 \\
&=2\\

\mathbb E[R^2]
&=\sum_{i=1}^\infty \mathbb P[R=i]\times  i^2\\
&=\sum_{i=1}^\infty \frac {4i} {(i+1)(i+2)}\\
&\to \infty
\end{aligned}
$$
(b)
$$
\mathbb E\left[\frac 1 R\right]
\le \mathbb E\left[1\right]=1
$$
(c)设
$$
\begin{aligned}
\mathbb P[R=1]&=p \\
\mathbb P[R=2]&=q\\
p+q&=1
\end{aligned}
$$
那么
$$
\begin{aligned}
\text{Var}(R)
& =\mathbb E[R^2] - \mathbb E[R]^2\\
&= p+4q -(p+2q)^2\\
&=1+3q-(1+q)^2 \\
&=1+3q -1-2q-q^2\\
&=-q^2 +q \\
&\le \frac1 4
\end{aligned}
$$
当且仅当$q=\frac 12$时取等号。

