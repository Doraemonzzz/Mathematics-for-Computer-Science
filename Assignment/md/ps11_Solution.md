#### Problem 1

(a)每行$4$个格子，每个格子有$3$种颜色选择，所以每行共有$81$种模式，因此$82$行中至少两个模式相同。

(b)选择模式相同的两行即可。

(c)每行$4$个格子选两个着相同颜色，一共的方法为$C_4^2\times 3=18​$。



#### Problem 2

关于$n$做数学归纳法，记
$$
P(n)=对于n张红黑卡牌，选择最上面的卡赢的策略为\frac 12
$$
$n=1$时结论显然，假设$n\le k$时结论成立，现证$n=k+1$时结论成立。假设有$s$个红牌，$t​$个黑牌，那么第一张为红色的概率为
$$
p=\frac{2^{s+t-1}}{2^{s+t}}=\frac 1 2
$$
记$k$张牌按此策略赢的概率为$p_k$，所以$k+1$张牌按此策略赢的概率为
$$
p_{k+1}=\frac 1 2 \times \frac 12 + \frac 12 \times p_k =
\frac 12 \times \frac 12 + \frac 12 \times \frac 12  =\frac 12
$$



#### Problem 3

用$A_1$表示红桃$A$，$A_2$表示黑桃$A$，$J$表示$Jack$，用$(a,b)$表示实验结果，其中$a$为没有选择的卡牌，$b$为丢弃的卡牌。

(a)实验结果为
$$
(A_1,A_2),(A_1,J)\\
(A_2,A_1),(A_2,J)\\
(J,A_1),(J,A_2)
$$
并且
$$
\begin{aligned}
\mathbb P[(a,b)]=\frac 1 6
\end{aligned}
$$
1.$[K\ge 1]$为
$$
(A_1,A_2),(A_1,J)\\
(A_2,A_1),(A_2,J)\\
(J,A_1),(J,A_2)
$$
2.
$$
(A_2,A_1),(A_2,J)\\
(J,A_1),(J,A_2)
$$
3.
$$
(A_2, A_1),(J,A_1)
$$
4.
$$
(A_1,A_2),
(A_2,A_1)\\
(J,A_1),(J,A_2)
$$


(b)$K=2​$表示
$$
(J,A_1),(J,A_2)
$$
所以
$$
\begin{aligned}
\mathbb P[K=2|E_1]
&=\frac 1 3\\

\mathbb P[K=2|E_2]
&=\frac 12\\

\mathbb P[K=2|E_3]
&=\frac 12\\

\mathbb P[K=2|E_3]
&=\frac 12
\end{aligned}
$$
(c)
$$
p= \frac{C_{d-1}^{h-1}}{C_d^h}=\frac h d
$$
(d)
$$
\begin{aligned}
\mathbb P[K=2 |A_1\text{is in your hand}]&=\frac {\mathbb P[K=2 \text{ and }A_1\text{is in your hand}]}
{\mathbb P[A_1\text{is in your hand}]}\\
&=\frac{\mathbb P[K=2] \mathbb P[A_1\text{is in your hand} | K=2]}{\frac h d}\\
&=\frac{\mathbb P[K=2]\times 2/a}{\frac h d}\\
&=\mathbb P[K=2] \times \frac{2d}{ah}
\end{aligned}
$$
(e)因为
$$
\begin{aligned}
\mathbb P[\text{the revealed card is an Ace}]
&=\frac{\sum_{k=1}^ aC_a^k \times C_{d-a}^{h-k}}{C_d^h} \times \frac {k} h\\
&=\frac{\sum_{k=1}^ a kC_a^k \times C_{d-a}^{h-k}}{h\times C_d^h}  \\
&=\frac{\sum_{k=1}^ a aC_{a-1}^{k-1} \times C_{d-a}^{h-k}}{h\times C_d^h} \\
&=\frac{a C_{d-1}^{h-1}}{h\times C_d^h}\\
&=\frac{a C_{d-1}^{h-1}}{h\times  \frac d h C_{d-1}^{h-1}} \\
&=\frac{a}{d}\\
 \mathbb P[\text{the revealed card is an Ace} |K=2]
 &=\frac{2}{h}
\end{aligned}
$$
所以
$$
\begin{aligned}
\mathbb P[K=2 |\text{the revealed card is an Ace}]
&=\frac {\mathbb P[K=2 \text{ and }\text{the revealed card is an Ace}]}
{\mathbb P[\text{the revealed card is an Ace}]}\\
&=\frac{\mathbb P[K=2] \mathbb P[\text{the revealed card is an Ace} |K=2]}
{\mathbb P[\text{the revealed card is an Ace}]}\\
&=\frac{\mathbb P[K=2]\times \frac{2}{h}}{\frac{a}{d}}\\
&=\mathbb P[K=2] \times \frac{2d}{ah}\\
&=\mathbb P[K=2 |A_1\text{is in your hand}]
\end{aligned}
$$

