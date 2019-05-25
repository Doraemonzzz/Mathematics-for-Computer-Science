#### Problem 1

(a)因为
$$
M=  \left[
 \begin{matrix}
0 & 1\\
1 & 0
  \end{matrix}
  \right]
$$
如果
$$
p= \left[
 \begin{matrix}
\frac 12 & \frac 12 
  \end{matrix}
  \right]
$$
那么
$$
p= pM
$$
(b)如果从$x$开始，那么
$$
\begin{aligned}
p&=\left[
 \begin{matrix}
1 & 0
  \end{matrix}
  \right]\\
  pM& = \left[
 \begin{matrix}
0 & 1
  \end{matrix}
  \right]\\
  pM^2 &= \left[
 \begin{matrix}
1 & 0
  \end{matrix}
  \right] =p
\end{aligned}
$$
所以不可能收敛到平稳状态。

(c)
$$
M=  \left[
 \begin{matrix}
 0& 1\\
 0.9 & 0.1
  \end{matrix}
  \right]
$$
求解
$$
\begin{aligned}
p&=pM \\
p_1 + p_2 & =1
\end{aligned}
$$
得到
$$
\begin{aligned}
p_1 & =\frac 9 {19}\\
p_2 & =\frac {10}{19}\\
p &=\left[
 \begin{matrix}
\frac 9 {19}& \frac {10}{19}
  \end{matrix}
  \right]
\end{aligned}
$$
(d)都会趋近于平稳分布。

(e)
$$
M=  \left[
 \begin{matrix}
1& 0 & 0 & 0 \\
\frac 12 & 0 & \frac 12 & 0\\
0 & \frac 12 &0 & \frac 12\\
0 & 0 & 0 & 1
  \end{matrix}
  \right]
$$
求解
$$
\begin{aligned}
p&=pM \\
p_1 + p_2+p_3+p_4 & =1
\end{aligned}
$$
得到
$$
p =\left[
 \begin{matrix}
a & 0 & 0 & 1- a
  \end{matrix}
  \right]
$$
所以有不可数个平稳分布。

(f)将会趋近于
$$
p_3= 0
$$
(g)取
$$
M=  \left[
 \begin{matrix}
0 & 1 & 0\\
1 & 0 & 0\\
0 &\frac 12 &\frac 12 
  \end{matrix}
  \right]
$$
求解
$$
\begin{aligned}
p&=pM \\
p_1 + p_2 +p_3& =1
\end{aligned}
$$
得到
$$
p =\left[
 \begin{matrix}
\frac 12 & \frac 12 & 0
  \end{matrix}
  \right]
$$



#### Problem 2

设
$$
M\in \mathbb R^{n\times n}, p = \left[
 \begin{matrix}
   \frac 1 n & \ldots & \frac 1n
  \end{matrix}
  \right]
$$
$\Rightarrow$：如果均匀分布是平稳分布，那么
$$
p=pM 
$$
所以$\forall j=1,\ldots ,n$，
$$
\begin{aligned}
\sum_{i=1}^n  M_{ij}\times \frac 1 n  &=p_i=\frac 1 n \\
\sum_{i=1}^n  M_{ij}&=1
\end{aligned}
$$
$\Leftarrow$：如果
$$
\sum_{i=1}^n  M_{ij}=1
$$
那么
$$
\sum_{i=1}^n  M_{ij}\times \frac 1 n
$$
所以
$$
p=pM
$$



#### Problem 3

(a)制造很多空网页，将自己的网页连接到这些空网页即可提高$d(v)$

(b)
$$
\begin{aligned}
(dM)_j&=\sum_{i\to j} d_i M_{ij}\\
&= \sum_{i\to j}\frac{\text {outdeg}(i)}{e}\frac 1 {\text {outdeg}(i)}\\
&=\frac{\# \{i\to j\}}{e}\\
&=\frac{\text {outdeg}(i)}{e}
\end{aligned}
$$

