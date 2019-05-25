#### Problem 1

(a)设事件发生的概率为$p$，那么示性函数的方差为$p(1-p)$，又因为
$$
p(1-p)\le \frac 1 4
$$
所以方差最大为$\frac 1 4$。

(b)
$$
\begin{aligned}
\mathbb P\left[ \left|{s_n -p}\right| <0.03\right]
& =\mathbb P\left[ \left|{s_n -p}\right| <0.03\right]\\
&\ge 1-\frac 1{1928}\times \frac {0.25}{0.03^2}\\
&\approx0.8559243891194098
\end{aligned}
$$

(c)由上一题可知，等号成立当且仅当
$$
p=\frac 12 
$$
所以
$$
\begin{aligned}
\mathbb P\left[ \left|{s_n -\frac 12 }\right| \le 0.03\right]
&= \mathbb P\left[ \left|{1928\times s_n -964}\right|\le 0.03\times 1928\right]\\
&=  \mathbb P[ 906 \leq 1928\times s_n \leq 1021]\\
&=\frac{\sum_{i=906}^{1021} \left( \begin{array}{c}{1928} \\ {i}\end{array}\right)}{2^{1928}}\\
&\approx 0.9912
\end{aligned}
$$
(d)不是，$0.35\pm 0.03​$只是置信度，不是概率。



#### Problem 2

(a)
$$
\begin{aligned}
\mathbb E[E_{ij}]
&= \mathbb P[B_i =B_j]\\
&=\frac 1 d \\

\mathbb E[E_{ij}^2]
&= \mathbb P[B_i =B_j]\\
&=\frac 1 d \\

\text{Var}[E_{ij}]&= \frac 1 d \left(1-\frac 1 d \right)
\end{aligned}
$$
(b)因为
$$
D= \sum_{i\neq j } E_{ij}
$$
以及两两独立，所以
$$
\begin{aligned}
\mathbb E[D]
&= \sum_{i\neq j } \mathbb E[E_{ij}] \\
&=\frac{n(n-1)}{2d} \\

\text{Var}[D]
&=  \sum_{i\neq j}\text{Var}[E_{ij}]\\
&=\frac {n(n-1)} 2 \frac 1 d \left(1-\frac 1 d \right)
\end{aligned}
$$
(c)根据题意构造随机变量即可，注意此时
$$
\begin{aligned}
\mathbb E[D]
&=\frac{n(n-1)}{2d} \\
& \approx 17.077 \\

\text{Var}[D]
&=  \sum_{i\neq j}\text{Var}[E_{ij}]\\
&=\frac {n(n-1)} 2 \frac 1 d \left(1-\frac 1 d \right)\\
&\approx 17.075
\end{aligned}
$$
结合$D$为整数可得
$$
|D-\mathbb E[D] | < 6 \Leftrightarrow D\in [12, 23]
$$
由切比雪夫不等式可得
$$
\begin{aligned}
\mathbb P[|D-\mathbb E[D] | < 6]
&\ge  1-  \frac{ \text{Var}[D]}{ 36} \\
&> 1- \frac {18}{36} \\
&=\frac 1 2
\end{aligned}
$$



#### Problem 3

$$
\forall \delta >0, \exist n_0 ,\forall n\ge n_0
$$



#### Problem 4

混淆了置信度和概率，实验结果可能是选择效果好的提交。



#### Problem 5

根据
$$
\mathbb P \left[ \left|A_{n}-\mu_{n}\right| \le  \epsilon\right] \ge 1- \frac 1 {n}\frac {\sigma^2}{\epsilon^2}
$$

只要$n$足够大即可。



#### Problem 6

(a)
$$
\begin{aligned}
\mathbb P \left[ \left|A_{n}-\mu_{n}\right| \geq \epsilon\right]
&\le \frac{\text{Var}[A_n]}{\epsilon^2}\\
&=\frac{\sum_{i=1}^n\text{Var}[X_i]}{n^2\epsilon^2}\\
&\le \frac{nb}{n^2\epsilon^2}\\
&=\frac{b}{\epsilon^{2}} \cdot \frac{1}{n}
\end{aligned}
$$
(b)因为
$$
\begin{aligned}
\mathbb P \left[ \left|A_{n}-\mu_{n}\right| \le \epsilon\right]
&=1 -\mathbb P \left[ \left|A_{n}-\mu_{n}\right| > \epsilon\right] \\
&\ge 1 -\frac{b}{\epsilon^{2}} \cdot \frac{1}{n}
\end{aligned}
$$
所以
$$
\lim_{n\to\infty } \mathbb P \left[ \left|A_{n}-\mu_{n}\right| \le \epsilon\right]=1
$$

