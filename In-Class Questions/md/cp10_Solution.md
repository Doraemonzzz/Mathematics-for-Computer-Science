#### Problem 1

(a)$x$属于F18推出$2^x$属于F18。因为$2^x$的反函数为$\log_2 x $，所以$\log_2 x $属于F18。因为$-1$属于F18，所以$-\log_2 x$属于F18，因此$2^{-\log_2 x} =\frac 1 x $属于F18。

(b)首先考虑Base case：

因为$\frac  {dx}{dx}=1​$，所以$x​$的导数属于F18。

因为常数的导数为$0​$，所以常数的导数属于F18。

注意$\frac {d \sin x}{dx} = \cos x =\sin (x +\frac \pi 2)​$。因为$x, \frac \pi 2 ​$属于F18，所以$x+\frac \pi 2 ​$属于F18；因为$\sin x​$属于F18，所以$\sin (x+\frac \pi 2)​$属于F18，因此$\sin x​$的导数属于F18。

Base case验证完成。

接下来考虑Constructor cases：

由Structural Induction，假设$f, g​$属于F18，我们将推出由$f,g​$生成的元素也属于F18，注意由假设可得$f',g'​$属于F18。

(1)
$$
(f+g)'=f'+g' \in F18
$$
(2)注意
$$
f'g ,fg'\in F18
$$

$$
(fg)'=f'g+fg' \in F18
$$
(3)注意
$$
2^g, g', \ln 2 \in F18
$$

$$
(2^g)'=2^g g' \ln 2 \in F18
$$
(4)由(a)可知$h(x)=\frac 1 x \in F18$，所以
$$
(f^{-1}(x))' = \frac{1}{f'(y)} =h(f'(y))\in F18
$$
(5)将$f'$和$g$复合可得
$$
f'(g(x))\in F18
$$
所以
$$
\big(f(g(x))\big)' = f'(g(x)) g'(x) \in F18
$$



#### Problem 2

(a)首先考虑Base case:

显然$\lambda \in \text{Erasable}​$，因此Base case成立。

接着考虑Constructorcase:

由Structural Induction，假设$s,t​$属于RecMatch且属于Erasable，我们将推出$[s]t​$属于Erasable。

由归纳假设，首先将$s$消除，那么剩余$[]t$，所以接着将$[]$消除，剩余$t$，由归纳假设可知$t$可以被消除，因此$[s]t​$属于Erasable。

(b)

(1)Basecase:

此时$n=0​$，$x=\lambda \in \text{Erasable}​$，所以$x\in \text{RecMatch}​$。

(2)此时$n=2$，所以$x=[]$，显然$x\in \text{RecMatch}$。

(3)因为$y\in \text{RecMatch}​$，所以由定义可知$x=py \in \text{RecMatch}​$。

(4)因为$t\in  \text{Erasable}​$，所以$t'\in  \text{Erasable}​$，注意$|t'|<|t|​$，所以由归纳假设可知$t'\in \text{RecMatch}​$，那么$x​$可以由$s,t'​$构造产生，因此$x\in  \text{RecMatch}​$。

(5)首先因为$y\in \text{Erasable}​$，那么其最左边的元素必然为$[​$，又因为可擦，所以必然存在可擦的$s,t​$，使得$y=[s]t​$，所以$y​$只能是这种形式。因为$y​$是由$x​$擦去一组$[]​$产生，所以或者擦去了最左侧的$[]​$，或者擦去了$s​$中的$[]​$，或者擦去了$t​$中的$[]​$，一共只有这三种情形。



#### Problem 3

(a)Basecase:
$$
1\in S
$$
Constructorcases:
$$
如果n \in S，那么2n, 3n,5n\in S
$$
(b)对集合元素变形可得
$$
2^k 3^{2k+m}5^{m+n}=18^k 15^m 5^n
$$
所以定义如下：

Basecase:
$$
1\in T
$$
Constructorcases:
$$
如果n \in T，那么18n, 15n,5n\in T
$$
(c)

Basecase:
$$
(n,n)\in L ,n\in \mathbb Z
$$
Constructorcases:
$$
如果(a,b)\in L，那么(a\pm 3, b)\in L
$$
(d)Basecase：

因为
$$
n-n=0
$$
所以
$$
(n,n)\in L
$$
Constructorcases:

假设$(a,b)\in L$，那么
$$
a-b =3 k, k\in \mathbb Z
$$
因此
$$
a\pm 3 -b=3(k\pm 1)
$$
所以
$$
(a\pm 3, b)\in L
$$
因此结论成立。

(e)$\forall (a, b)\in L$，那么$a-b= 3k,k\in \mathbb Z $。

如果$k=0$，那么
$$
(a,b)=(a,a)\in L'
$$
如果$k>0​$，那么
$$
(a,b)=(b+3k,b) \in L'
$$
如果$k<0$，那么
$$
(a,b)=(a+3k,b)= (a-(-3k),b)\in L'
$$
因此结论成立。

(f)上述定义是确定的，由(e)的讨论即可得出。



#### Problem 4

(a)
$$
G_{1,2}=\lang\text{bintree}, \lang\text{leaf, lose} \rang , 
 \lang\text{leaf, win} \rang \rang \\
 G_1= \lang\text{bintree},\lang\text{leaf, win}  \rang,G_{1,2} \rang \\
 G=\lang\text{bintree},G_1,\lang\text{leaf, win} \rang \rang
$$
(b)Basecase：

如果$G=\lang\text{leaf}, l \rang​$，那么
$$
\text{flatten}(G)=(l)
$$
Constructorcases:

如果$G=\lang\text{bintree}, G_1,G_2 \rang$，那么
$$
\text{flatten}(G)=\text{flatten}(G_1)+\text{flatten}(G_2)
$$
其中加号表示拼接操作。

(c)Basecase：

左边为
$$
2.\text{length}(\text{flatten}(G))= 2
$$
右边为
$$
|G|+1 = 2
$$
所以Basecase等式成立。

Constructorcases:

如果$G=\lang\text{bintree}, G_1,G_2 \rang​$，且$G_1,G_2​$满足等式，那么
$$
\begin{aligned}
2.\text{length}(\text{flatten}(G))
&=2.\text{length}(\text{flatten}(G_1))+
2.\text{length}(\text{flatten}(G_2)) \\
&=|G_1|+1 + |G_2|+1 \\
&=|G|+1
\end{aligned}
$$
所以Constructorcases等式成立。