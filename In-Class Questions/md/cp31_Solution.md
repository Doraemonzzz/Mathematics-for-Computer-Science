#### Problem 1

选择相邻的两个数$a,a+1$，此时第二组赢的概率为
$$
p=\frac 1 7+\frac 6 7 \times \frac 1 2 =\frac 4 7
$$
所以第一组赢的概率为
$$
1-p=\frac 3 7
$$



#### Problem 2

$$
\begin{aligned}
\mathbb P[I_A =1, I_B=1]
&= \mathbb P[I_A =1]\mathbb P[I_B =1]\Leftrightarrow \\
\mathbb P[AB]&= \mathbb P[A]\mathbb P[B]
\end{aligned}
$$



#### Problem 3

(a)
$$
\text{PDF}_M(1) =\frac 1 {n^m}
$$
(b)
$$
\begin{aligned}
\mathbb P[M\le k]
&=\left(\frac {k} n \right)^m
\end{aligned}
$$
(c)
$$
\begin{aligned}
\text{PDF}_M(k)
&= \mathbb P[M\le k] -\mathbb P[M\le k-1]\\
&= \left(\frac {k} n \right)^m -\left(\frac {k-1} n \right)^m
\end{aligned}
$$



#### Problem 4

(a)
$$
\begin{aligned}
\frac{\text{PDF}_J(k)}{\text{PDF}_J(k-1)}
&=\frac{ \binom n k   p^{k} q^{n-k}}{ \binom n {k-1}   p^{k-1} q^{n-k+1}}\\
&=\frac{(n-k+1) p}{k(1-p)}
\end{aligned}
$$
令上式大于$1$得到
$$
\begin{aligned}
\frac{(n-k+1) p}{k(1-p)}& > 1 \\
(n-k+1) p& > k-kp \\
np+p& > k
\end{aligned}
$$
令上式小于$1​$得到
$$
np+p< k
$$
所以结论成立。

(b)代入$k=np$得到
$$
\begin{aligned}
\binom n {np}   p^{np} q^{n-np}
&= \frac{n!}{(np)! (nq)!}  p^{np} q^{nq}\\
&\approx\frac{\sqrt{2\pi n} \left(\frac{n}{e}\right)^n }
{\sqrt{2\pi np} \left(\frac{np}{e}\right)^{np}\sqrt{2\pi nq} \left(\frac{nq}{e}\right)^{nq} }
 p^{np} q^{nq}\\
&=\frac{1}{\sqrt{2 \pi n p q}}
\end{aligned}
$$



#### Problem 5

(a)
$$
\text{PDF}_B(i)=\frac 1 {2^{i+1}}
$$
(b)
$$
\begin{aligned}
\text{CDF}_B(i)
&=\sum_{j=0}^i \text{PDF}_B(i)\\
&=\sum_{j=0}^i \frac 1 {2^{i+1}} \\
&= 1-\frac 1 {2^{i+1}}
\end{aligned}
$$

