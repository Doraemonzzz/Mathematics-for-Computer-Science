#### Problem 1

(a)
$$
\begin{aligned}
\mathbb P[B]&=\frac 1 {1000}\\
\mathbb P[Y|B]&=0.99\\
\mathbb P[\bar Y|\bar B ]
&= 0.97
\end{aligned}
$$
(b)
$$
\begin{aligned}
\mathbb P[\bar B]
&=1-\mathbb P[B]\\
&=0.999\\

\mathbb P[Y|\bar B]
&= 1- \mathbb P[\bar Y|\bar B]\\
&= 0.03
\end{aligned}
$$
(c)
$$
\begin{aligned}
\mathbb P[Y]&=\mathbb P[B]\mathbb P[Y|B]+
\mathbb P[\bar B]\mathbb P[Y|\bar  B]\\
&= \frac 1 {1000} \times 0.99 + 0.999\times 0.03\\
&=0.03096
\end{aligned}
$$
(d)
$$
\begin{aligned}
p&=\mathbb P[B|Y] \\
&=\frac{\mathbb P[B]\mathbb P[Y|B]}{\mathbb P[B]\mathbb P[Y|B]+
\mathbb P[\bar B]\mathbb P[Y|\bar  B]}\\
&= \frac{\frac 1 {1000} \times 0.99}{0.03096}\\
&=0.03197674418604651
\end{aligned}
$$
(e)该比例即为
$$
\begin{aligned}
p&=\mathbb P[Y|B]\\
&= 0.99
\end{aligned}
$$



#### Problem 2

$$
\begin{aligned}
\mathbb P[S|"F"]
&=\frac{\mathbb P[S\bigcap "F"]}{\mathbb P["F"]}\\
&= \frac {\mathbb P["F"|S]\mathbb P[S]}{
    \mathbb P["F"|S]\mathbb P[S]
    +\mathbb P["F"|\bar S]\mathbb P[\bar S]
}\\
&=\frac { \frac 1 2\times \frac{2}{3}}{
\frac 1 2\times \frac{2}{3} +\frac 1 2 \times  \frac 1 3
}\\
&=\frac  2  3
\end{aligned}
$$



#### Problem 3

$$
p=\frac{\frac 1 2 \times \frac 1{54}}{\frac 1 2 \times \frac 1{54}+ \frac 1 2
\times \frac 1{53}}=\frac {53}{107}
$$



#### Problem 4

定义HHT出现在HTT之前的事件为A，那么
$$
\begin{aligned}
\mathbb P[A]
&=\mathbb P[A|H]\mathbb P[H]+ \mathbb P[A|T]\mathbb P[T]\\
&=\frac 1 2 \mathbb P[A|H] +\frac 1 2  \mathbb P[A]
\end{aligned}
$$
所以
$$
\mathbb P[A] =\mathbb P[A|H]
$$
另一方面
$$
\begin{aligned}
\mathbb P[A|H]
&=\mathbb P[A|HH] \mathbb P[H]+\mathbb P[A|HT] \mathbb P[T]\\
&=\frac{1}{2}\mathbb P[A|HH]  +\frac{1}{2}\mathbb P[A|HT]
\end{aligned}
$$
现在考虑给定前两位$HH$，事件$A$发生的概率，这时候后事件$A​$发生的情形为
$$
HHT,HHHT,HHHHT,\ldots 
$$
所以
$$
\mathbb P[A|HH] =\sum_{i=1}^n \frac 1 {2^i}=1
$$
带入可得
$$
\begin{aligned}
\mathbb P[A|H]
&=\mathbb P[A|HH] \mathbb P[H]+\mathbb P[A|HT] \mathbb P[T]\\
&=\frac{1}{2}  +\frac{1}{2}\mathbb P[A|HT]
\end{aligned}
$$
但是显然有
$$
\begin{aligned}
\mathbb P[A|HT]
&=\mathbb P[A|HT H] \mathbb P[H]+\mathbb P[A|HTT] \mathbb P[T]\\
&= \frac 1 2 \times \mathbb P[A|HT H]  +\frac 1 2 \times 0\\
&=\frac 1 2 \times \mathbb P[A|H]
\end{aligned}
$$
综合之前的讨论得到
$$
\begin{aligned}
\mathbb P[A]
&=\mathbb P[A|H]\\
&=\frac{1}{2}  +\frac{1}{2}\mathbb P[A|HT]\\
&=\frac{1}{2}  +\frac{1}{2} \times \frac 1 2  \times \mathbb P[A|H]\\
&=\frac{1}{2}  +\frac 1 4 \times \mathbb P[A]
\end{aligned}
$$
因此
$$
\mathbb P[A]=\frac 2 3
$$
所以题目中事件发生的概率为
$$
1-\frac 2 3 =\frac 1 3 
$$
参考资料：

https://dicedcoins.wordpress.com/2012/07/19/flip-hhh-before-htt/