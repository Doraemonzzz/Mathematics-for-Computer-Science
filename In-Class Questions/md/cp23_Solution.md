#### Problem 1

不失一般性，假设水和酒初始的数量为$1$。

(a)假设$n$步back-and-forth pouring后第一个杯子中酒的比例为$a_n$，第二个杯子中酒的比例为$b_n$，那么不难看出
$$
\begin{aligned}
&a_0= 0, b_0=1\\
&a_n +b_n=1
\end{aligned}
$$
考虑第$n+1$次back-and-forth pouring，第一步从第一杯中倒$\frac 13​$到第二杯中，此时第二杯中酒的含量为
$$
\frac 1 3 a_n + b_n
$$
第二步从第二杯倒$\frac 1 3​$到第一杯中，那么
$$
\begin{aligned}
a_{n+1} &= \frac 2 3 a_n + \frac 1 3 (\frac 1 3 a_n + b_n)\\
&= \frac 2 3 a_n + \frac 1 3 (\frac 1 3 a_n + 1-a_n)\\
&=\frac 4 9 a_n +\frac 1 3
\end{aligned}
$$
(b)设极限为$a$，令$n\to \infty$可得
$$
\begin{aligned}
a&= \frac 4 9 a+\frac 13 \\
a&=\frac 3 5
\end{aligned}
$$



#### Problem 2

(a)因为要来回，所以$1$加仑水离开的最远距离为$\frac 12 $。

(b)类似例子中的思路，首先带$1​$加仑水，先存放$\frac 1 2​$加仑到距离起点$\frac 14 ​$的距离，这部分共需要花$1​$加仑，接着从起点带着剩下的$1​$加仑出发，走到之前存水的位置时加满水，然后再往前走$\frac 12 ​$的距离后返回，这样恰好可以返回，此时行走的距离为
$$
\frac 1 4+\frac 12 =\frac 3 4
$$
(c)按照题目中的提示思考，首先想办法存储$n-1$加仑的水，假设存储点距离出发点为$a$，那么来回一次可以存储的加仑数为
$$
1-2a
$$
假设来回$k$次，那么总共存储的加仑数为
$$
k(1-2a)
$$
要使得上式为$n-1$，可取
$$
k=n ,a=\frac 1 {2n}
$$
即缓存点距离出发点的距离为$\frac 1{2n}$。注意最后一次运水后缓存点的加仑数为$n-1$，此时将身上剩下的$\frac 1 {2n}$加仑水也存储起来，利用剩下的$n-1$加仑前进，最远的前进距离为$n-1$加仑水前进的最远距离，最后回到存储点用剩下的$\frac 1{2n}$返回出发点即可，如果记按这个策略操作，出发点有$n$加仑水达到的最远距离为$d_n$，那么
$$
d_n =\frac {1}{2n} +d_{n-1}
$$
特别的，我们取
$$
d_1 = \frac 12
$$
所以
$$
\begin{aligned}
d_n
&= \frac 1{2n} +d_{n-1} \\
&= \frac 1{2n} +\frac 1{2(n-1)} +d_{n-2} \\
&= \ldots \\
&=\frac 12 \left(\sum_{i=1}^n \frac 1 i\right)\\
&= \frac 12 H_n
\end{aligned}
$$
(d)令
$$
\begin{aligned}
d_n &=\frac 12 H_n = 10\\
H_n &=20
\end{aligned}
$$
因为$H_n \sim  \ln n$，所以
$$
n \approx e^{20}
$$
大约需要132万年。



#### Problem 3

记
$$
g(x) =f(n)-f(x)\ge 0,0\le x \le n\\
S_1 =\sum_{i=1}^n g(i)=nf(n)-\sum_{i=1}^n f(i)
=nf(n)-S
$$
不难看出$g(x)$单调递增，那么
$$
I_1+f(n)-f(1)=I_1 +g(1) \le S_1 \le I_1 +g(n)=I_1
$$
因为
$$
I_1 =\int_{1}^n (f(n)-f(x))dx= (n-1)f(n)-I
$$
所以
$$
nf(n)-I-f(1) \le nf(n)-S \le (n-1)f(n)-I\\
I+f(n)\le S \le I+f(1)
$$



#### Problem 4

(a)
$$
(m+f)p=mp+fp
$$
(b)
$$
\left((m+f)p +f\right)p =mp^2 +fp^2+fp
$$
(c)第$d​$天的债务为
$$
mp^d +f\left(\sum_{i=1}^d p^i \right)
=mp^d +f \frac{p(1-p^d)}{1-p}
$$
(d)取$m=10,d=365,f=0.1, p=1.01$可得
$$
749.3470300910341
$$



#### Problem 5

因为
$$
T-zT=\sum_{i=1}^ n z^i-nz^{n+1}=\frac{z(1-z^n)}{1-z}-nz^{n+1}
$$
所以
$$
T =\frac{z(1-z^n)}{(1-z)^2}-\frac{nz^{n+1}}{1-z}
$$


