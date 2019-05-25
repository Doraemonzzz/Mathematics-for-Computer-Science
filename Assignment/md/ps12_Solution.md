#### Problem 1

(a)
$$
\begin{aligned}
\mathbb P[R=S]
& =\bigcup_{b\in V} \mathbb P[R=b,S=b]\\
&=\bigcup_{b\in V} \mathbb P[R=b]\mathbb P[S=b] \\
&=\bigcup_{b\in V} \frac 1 {|V|^2}\\
&= \frac 1 {|V|}
\end{aligned}
$$
(b)显然$R$和$S$独立，所以
$$
\begin{aligned}
\mathbb P[R=S]
&= \frac 1 {|V|}
\end{aligned}
$$
因此
$$
\begin{aligned}
\mathbb P[R=S, S=T]
&= \mathbb P[R=S=T]\\
&=\sum_{b\in V}\mathbb P[T=S=b]\mathbb P[R=b]\\
&=\frac 1 {|V|}\sum_{b\in V}\mathbb P[T=S=b]\\
&=\mathbb P[R=S]\mathbb P[T=S]
\end{aligned}
$$
(c)

(1)
$$
\begin{aligned}
\mathbb P[R=i]&=\begin{cases}
\frac 12 & i=1\\
\frac 12& i=2
\end{cases}\\
\mathbb P[S=j,T=k]&=\begin{cases}
\frac 13 & j=1,k=1\\
\frac 13& j=2,k=3\\
\frac 13& j=3,k=2
\end{cases}

\end{aligned}
$$
显然
$$
\mathbb P[R=i,S=j,T=k]=\frac 1 6 = \mathbb P[R=i]
\times \mathbb P[S=j,T=k]
$$
(2)
$$
\begin{aligned}
\mathbb P[R=S]& =\frac {1}{3}\\
\mathbb P[S=T]& =\frac {1}{3}
\end{aligned}
$$
但是
$$
\begin{aligned}
\mathbb P[R=S=T]& =\frac {1}{6}
\end{aligned}
$$
(3)显然。



#### Problem 2

(a)设实验次数为$m​$，那么
$$
\begin{aligned}
\mathbb E[m]
&=g\times \left((1-p)^k +\left(1-(1-p)^k\right)\times (k+1)  \right) \\
&=\frac n k \times \left(k+1 -k (1-p)^k  \right)\\
&=\frac{n(k+1)}{k} -n(1-p)^k
\end{aligned}
$$
(b)
$$
\begin{aligned}
\frac{n(k+1)}{k} -n(1-p)^k
&\approx n +\frac n k  -n\\
&=\frac n k
\end{aligned}
$$
如果$k=\frac 1 {\sqrt p}$，那么
$$
\frac n k\approx  n\sqrt p
$$
(c)方法1的实验次数为$n$，所以减少的百分比为
$$
1-\sqrt p =1-0.1=0.9
$$
(d)假设$n=guv$，先分为$g$组，每组再分为$v$组，每组$u$个人，设实验次数为$m​$，记
$$
q= (1-p)^u
$$
那么
$$
\begin{aligned}
\mathbb E[m]
&=g\times \left(\sum_{i=0}^v C_v^iq^{v-i}(1-q)^{i} \left(v+iu\right)\right)\\
&=g\times \left(v+u v(1-q) \right)\\
&=\frac n {uv}\times v + n\left(1- (1-p)^u\right)\\
&=\frac n u + n\left(1- (1-p)^u\right)
\end{aligned}
$$
从这个公式看，期望值只和每组的人数有关。



#### Problem 3

(a)
$$
p= 1-\frac 1 {2^k}
$$
(b)设ture k-clauses的数量为$m$，那么
$$
\mathbb E[m] = n\times \left(1-\frac 1 {2^k}\right)=n  -\frac  n {2^k}
$$
(c)如果$n< 2^k$，那么
$$
\begin{aligned}
\mathbb E[m] &= n  -\frac  n {2^k} \\
& > n-1
\end{aligned}
$$
因为$m$是整数，所以必然存在使得$\mathcal S$中元素全真的分配，因为如果该结论不成立，那么必然有
$$
\begin{aligned}
m& \le n-1\\
\mathbb E[m]&\le n-1
\end{aligned}
$$
