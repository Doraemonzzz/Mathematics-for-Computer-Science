#### Problem 1

(a)略过。

(b)
$$
\begin{aligned}
p_1&=\frac 4 {12}\times \frac 4 {12}+
\frac 5 {12}\times \frac  {7} {12}
+\frac 3 {12}\times \frac  {11} {12}\\
&=\frac{16+35+33}{144}\\
&=\frac{84}{144}\\
&=\frac{7}{12}
\end{aligned}
$$
(c)
$$
\begin{aligned}
p_2
&=\frac{\frac 4 {12}\times \frac 4 {12}}{\frac 7 {12}} \\
&=\frac{4}{21}
\end{aligned}
$$
(d)因为
$$
p_2 \neq  \frac {4}{12}
$$
(e)
$$
p_3 =\frac{\frac{7}{12}\times \frac 5 {12}}{\frac{7}{12}}=\frac 5 {12}
$$



#### Problem 2

(a)略过，直接给出事件发生的概率：
$$
\begin{aligned}
\mathbb P[A]& =\frac 12 \\
\mathbb P[B]& =\frac 12\\
\mathbb P[C]& =\frac 12\\
\mathbb P[D]& =\frac 12
\end{aligned}
$$
(b)
$$
\begin{aligned}
\mathbb P[ABCD] =0\neq  \mathbb P[A]
 \mathbb P[B] \mathbb P[C] \mathbb P[D]
\end{aligned}
$$
(c)显然$A,B,C$相互独立；另外由对称性，只需验证$A,B,D​$相互独立即可
$$
\begin{aligned}
\mathbb P[AB]& =\mathbb P[A]\mathbb P[B]= \frac 1 2 \times \frac  12 \\
\mathbb P[AD]&
= \mathbb P [A] \mathbb P [D]= \frac 1 2 \times \frac  12 \\
\mathbb P[BD]&= \mathbb P [B] \mathbb P [D]= \frac 1 2 \times \frac  12 \\
\mathbb P[ABD]&= \mathbb P[A]\mathbb P [B] \mathbb P [D]
=\frac 1 2 \times \frac 1 2 \times \frac 1 2
\end{aligned}
$$



#### Problem 3

(a)
$$
\exists z ,s.t\ \ E(x,z) \text{ and } E(z, y)
$$
(b)独立的事件有
$$
1,2,3,4,
$$
(c)
$$
\mathbb P[\text{NOT }P(x,y)]
=(1-p^2)^{n-2}
$$
(d)概率为
$$
p(1-r)=p\left(1- (1-p^2)^{n-2}\right)
$$



#### Problem 4

(a)成立
$$
\begin{aligned}
\mathbb P[A\overline B]
&=\mathbb P[A]- \mathbb P[A B]\\
&=\mathbb P[A]-\mathbb P[A]\mathbb P[ B]\\
&=\mathbb P[A](1-\mathbb P[B])\\
&=\mathbb P[A]\mathbb P[\overline B]
\end{aligned}
$$
(b)不一定，考虑投硬币两次的实验：
$$
\begin{aligned}
A&=第一次正面\\
B&=第二次正面\\
C&=奇数个正面
\end{aligned}
$$
(c)不一定，利用(b)即可。

(d) 成立
$$
\begin{aligned}
\mathbb P[A\cap (B\cup C)]
&=\mathbb P[(A\cap B)\cup(A\cap C)]\\
&=\mathbb P[A\cap B]+\mathbb P[A\cap C]
-\mathbb P[A\cap B \cap C]\\
&=\mathbb P[A]\mathbb P[B]+\mathbb P[A]\mathbb P[C]- \mathbb P[A]\mathbb P[B \cap C]\\
&=\mathbb P[A]\left(\mathbb P[B]+
\mathbb P[C]-\mathbb P[B \cap C] \right)\\
&=\mathbb P[A] \mathbb P[B\cup C]
\end{aligned}
$$
