#### Problem 1

证明：如果$a>\sqrt n ,b>\sqrt n$，那么
$$
a.b > n
$$
与
$$
a.b = n
$$
矛盾



#### Problem 2

这里证明更强的结论：
$$
对于任意素数p,\sqrt p 都是无理数
$$
利用反证法证明，如果$\sqrt p$是有理数，那么$\sqrt p  =\frac m n ,m,n\in \mathbb N且m,n互质$，平方可得
$$
p =\frac{m^2}{n^2} \\ 
p n^2 = m^2
$$
所以$p\mid m^2$，从而$p\mid m$，从而$m=pm_1$，带入上式可得
$$
pn^2= p^2 m_1 ^2 \\
n^2 = pm_1^2
$$
这说明$p\mid n^2$，$p\mid n$，这就与$m,n$互质矛盾



#### Problem 3

结论如下：
$$
无理数的无理次方可能为有理数
$$
考虑$\sqrt{2}^{\sqrt 2}$，如果$\sqrt{2}^{\sqrt 2}$为有理数，那么结论成立，否则$\sqrt{2}^{\sqrt 2}$为无理数，此时考虑$(\sqrt{2}^{\sqrt 2})^\sqrt 2  = \sqrt 2 ^{\sqrt 2 \sqrt 2 }=\sqrt 2 ^2 = 2$，那么结论依旧成立，这就说明了无理数的无理次方可能为有理数。

关于此有一个更强的结论：
$$
几乎所有 (1, ∞) 里的有理数都是某个无理数 a 的 a 次方
$$
参考链接：http://www.matrix67.com/blog/archives/4984



#### Problem 4

反证法，假设$2\log_2 3$为有理数，那么$2\log_2 3=\frac p q,p,q$互质，因此
$$
q \log_2 9 = p\\
 \log_2 9^q = p\\
 9^q = 2^p
$$
左右两边奇偶性不同，显然不可能相等，所以$2\log_2 3$为无理数

