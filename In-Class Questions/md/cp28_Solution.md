#### Problem 1

(a)
$$
p=\frac 1 4
$$
(b)
$$
p=\frac 3  4 \times \frac 1 2 =\frac 3 8
$$



#### Problem 2

(a)定义
$$
\mathbb P[\{1,\ldots, n\}] =p,\mathbb P[\varnothing] =1-p
$$
以及其余情形发生的概率为
$$
0
$$
(b)定义
$$
\mathbb P[\{i\}] =p,1\le i\le n\\
\mathbb P[\varnothing] =1-np
$$
以及其余情形发生的概率为
$$
0
$$

(c)显然
$$
F=\cup_{i=1}^n F_i
$$
所以
$$
\begin{aligned}
p& = \mathbb P[F_i]\\
&\le \mathbb P[F]\\
&\le \sum_{i=1}^n \mathbb P[F_i]\\
&=np
\end{aligned}
$$


#### Problem 3

投币$2$次赢的概率为
$$
p(1-p)
$$
投币$4$次赢的概率为
$$
\left(p^2+(1-p)^2\right) p(1-p)
$$
所以第一个人赢的概率为
$$
\sum_{i=0}^{\infty}
\left(p^2+(1-p)^2\right)^i p(1-p)
= p(1-p)\times  \frac 1 {1-\left(p^2+(1-p)^2\right)}=\frac 1 2
$$

同理可得第二个人赢的概率为
$$
\sum_{i=0}^{\infty}
\left(p^2+(1-p)^2\right)^i(1-p) p
= (1-p) p\times  \frac 1 {1-\left(p^2+(1-p)^2\right)}=\frac 1 2
$$
所以没人赢的概率为
$$
1-\frac 12 -\frac 12 =0
$$


#### Problem 4

记
$$
B_k =\bigcup_{n=1}^k A_n
$$
那么
$$
\begin{aligned}
\mathbb P\left[B_k\right]
\le \sum_{n=1}^k \mathbb P[A_n]
\end{aligned}
$$
因此
$$
\mathbb P\left[B_k\right] \le \sum_{n=1}^{\infty}  \mathbb P[A_n]
$$
因为$B_k \uparrow$，所以$\mathbb P[B_k]$单调递增，因此
$$
\mathbb P
\left[\bigcup_{n=1}^\infty A_n\right]
=\lim_{k\to\infty} \mathbb P\left[B_k\right]\le
\sum_{n=1}^{\infty}  \mathbb P[A_n]
$$



#### Problem 5

因为
$$
(A\cap B ) \cap (A-B) =\varnothing ,(A\cap B ) \cup (A-B) =A
$$
所以
$$
\begin{aligned}
\mathbb P[A\cap B] + \mathbb P[A-B] &=\mathbb P[A]\\
 \mathbb P[A-B] & = \mathbb P[A]-\mathbb P[A\cap B]
\end{aligned}
$$
对第一个结论取$A=\Omega ,B=A$即可。
$$
\begin{aligned}
\mathbb P[A\cup B]
&=\mathbb P[A] + \mathbb P[(A\cup B)-A]\\
&=\mathbb P[A] +\mathbb P[B-A]\\
&=\mathbb P[A] + \mathbb P[B]- \mathbb P[A\cap B]
\end{aligned}
$$
利用上一个结论可得
$$
\mathbb P[A\cup B] \le \mathbb P[A]+\mathbb P[B]
$$
对第一个等式取$A=B,B=A$可得
$$
\mathbb P[B] =\mathbb P[A] + \mathbb P[B-A]\ge \mathbb P[A]
$$



#### Problem 6

(a)
$$
p= 1- \left(\frac 3 5\right)^2 - \left(\frac 2 5\right)^2 =\frac{12}{25}
$$
(b)
$$
p=\frac 3 5\times \left(\frac 2 5\right)^2  +
\frac 2 5\times \left(\frac 3 5\right)^2
=\frac{6}{25}
$$
(c)应该是指胜率大的队伍赢得比赛的概率：
$$
p=\left(\frac 3 5\right)^2 +2\times \frac 2 5\times \left(\frac 3 5\right)^2
=\frac{81}{125}
$$