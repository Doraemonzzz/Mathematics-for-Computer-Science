#### Problem 1

设
$$
\sum_{i=1}^n i^3 = an^4+bn^3+cn^2+dn+e
$$
令$n=0,1,2,3,4$可得
$$
\begin{cases}
0=e \\
1=a+b+c+d+e\\
9=16a+8b+4c+2d+e \\
36=81a+27b+9c+3d+e \\
100=144a+64b+16c+4d+e
\end{cases}
$$
解得
$$
\begin{cases}
a=\frac 1 4 \\
b= \frac 12 \\
c =\frac 14 \\
d=0\\
e=0
\end{cases}
$$
所以
$$
\sum_{i=1}^n i^3 =\left(\frac {n(n+1)}{2}\right)^2
$$



#### Problem 2

由斯特林公式可得
$$
\begin{aligned}
\ln (n^2 !)
&=\ln \left( \sqrt{2\pi n^2} \left(\frac {n^2} e\right)^{n^2} e^{\epsilon(n^2)}\right)\\
&= n^2 \ln (n^2) -n^2 +\frac 12 \ln (2\pi n^2) +\epsilon(n^2)
\end{aligned}
$$
其中
$$
\frac{1}{12n+1}\le \epsilon(n)\le \frac 1{12n}
$$
所以
$$
\lim_{n\to \infty} \frac{\ln (n^2 !)}{n^2 \ln (n^2) } =1
$$
因此
$$
\ln \left(n^{2} !\right)=\Theta\left(n^{2} \ln n\right)
$$



#### Problem 3

记
$$
f(x)=x^6
$$
那么
$$
I= \int_1^n x^6 dx =\frac 1 7 (n^7-1)
$$
因此
$$
\begin{aligned}
I+f(1) &\le  \sum_{k=1}^n k^6 \le I+f(n)\\
\frac 1 7 (n^7-1)+1 &\le  \sum_{k=1}^n k^6 \le \frac 1 7 (n^7-1) + n^6\\
\frac 1 7=\lim_{n\to \infty} \frac{\frac 1 7 (n^7-1)+1}{n^7}&
\le \lim_{n\to \infty}\frac {\sum_{k=1}^n k^6}{n^7} 
=\lim_{n\to \infty} \frac{\frac 1 7 (n^7-1) + n^6}{n^7}=\frac 1 7
\end{aligned}
$$
因此
$$
\sum_{k=1}^{n} k^{6}=\Theta\left(n^{7}\right)
$$
