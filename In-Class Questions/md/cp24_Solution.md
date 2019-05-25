#### Problem 1

(a)因为
$$
\begin{aligned}
\lim_{n\to \infty} \frac{n^2}{3n} &=\infty\\
\lim_{n\to \infty} \frac{3n}{n^2} &=0
\end{aligned}
$$
所以
$$
g=O(f)
$$
由极限为$0​$可得最小的整数$c​$为$1​$，即$n\ge n_0​$时
$$
2n \le n^2 
$$
解得
$$
n\ge 2
$$
所以$n_0=2$

(b)因为
$$
\begin{aligned}
\lim_{n\to \infty} \frac{(3n-7)/(n + 4)}{4} &=\frac{3}{4}\\
\lim_{n\to \infty} \frac{4} {(3n-7)/(n + 4)} &=\frac{4}{3}
\end{aligned}
$$
所以
$$
f=O(g),g=O(f)
$$
对于$f=O(g)​$，最小整数为$1​$，即$n\ge n_0​$时
$$
(3n-7)/(n + 4) \le 4
$$
解得
$$
n\ge -23 
$$
所以$n_0=0$

对于$g=O(f)$，最小整数为$2$，即$n\ge n_0$时
$$
4\le 2(3n-7)/(n + 4) 
$$
解得
$$
n\ge 15
$$
所以$n_0=15$.

(c)不存在大$O​$关系，因为当$n=2k,k\in \mathbb N​$时，
$$
f(2k)=1 ,g(2k)=6k
$$
当$n=2k+1, k\in \mathbb N$时，
$$
f(2k+1)=1+(2k+1)^2 ,g(2k+1)=6k+3
$$



#### Problem 2

(a)

E:
$$
f\sim g,f =\Theta (g)
$$
W:
$$
f=O(g)
$$
S:
$$
f=o(g),f=O(g)\text{ AND NOT }(g=O(f))
$$
(b)
$$
f\sim g\Rightarrow f =\Theta (g) \Rightarrow f=O(g)\\
f=o(g)\Rightarrow f=O(g)\text{ AND NOT }(g=O(f))\Rightarrow f=O(g)
$$



#### Problem 3

因为
$$
\lim_{n\to\infty} 2^n =\infty
$$
所以结论错误。

该证明的错误在于，$n+1$时的结论应该为
$$
2^{n+1} \le c
$$



#### Problem 4

(1)正确
$$
\lim_{n\to\infty} \frac{n^2}{n^2+n}=1
$$
(2)错误，因为
$$
\lim_{n\to\infty} \frac{3^n}{2^n}
=\infty
$$
(3)错误，因为当$n=4k+2,k\in \mathbb N$时，
$$
\sin((4k+2)\pi /2) =1
$$
那么
$$
\lim_{k\to\infty} \frac{(4k+2)^{\sin((4k+2)\pi /2)+1}}{(4k+2)^2}=\lim_{k\to\infty} \frac{(4k+2)^2}{(4k+2)^2}=1
$$
(4)正确
$$
\lim _{n\to\infty} \frac{n}{\frac{3 n^{3}}{(n+1)(n-1)}}=\frac 13 
$$



#### Problem 5

令
$$
f(x)=\log x
$$
那么
$$
\log(n!)=\sum_{i=1}^n \log i=\sum_{i=1}^n f(i)
$$
记
$$
I=\int_{1}^n \log xdx =n \log n-n+1
$$
那么
$$
n \log n-n+1\le\log(n!) \le n \log n-n+1+\log n
$$
所以
$$
\log (n !)=\Theta(n \log n)
$$
