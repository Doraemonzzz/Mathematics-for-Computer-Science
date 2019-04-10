#### Problem 1

(a)weak partial order

(b)equivalence relation

(c)weak partial order

(d)equivalence relation

(e)none，违反了传递性

(f)empty relation的含义：https://math.stackexchange.com/questions/1550802/what-is-the-empty-relation

因为$R$是empty relation，所以$(a,a)\notin R$，因此自反性不成立；因为$(u,v)\in R$永远为假，所以transitive和asymmetric成立，从而是strict partial order。

(g)equivalence relation

(h)weak partial order



#### Problem 2

(a)7
$$
\varnothing \subset \{1\}\subset\{1,2\}\subset \{1,2,3\}\subset\\
\{1,2,3,4\}\subset \{1,2,3,4,5\}\subset \{1,2,3,4,6\}
$$
(b)如果$\{1,...,6\}$的两个子集元素数量相同，那么这两个集合必然没有包含关系，所以最大的antichain为
$$
2^6=64
$$
(c)minimal:0,maximal:6。minimal集合是minimum，maximum集合是maximum。

(d)只改变minimal部分，minimal为$1$，所以minimal不是minimum。



#### Problem 3

(a)最长递增子列：
$$
1258,1238
$$
最长递减子列：
$$
641,642,643,953
$$
(b)maximal元素：$8,9$

minimal元素：$1,4,6$

(c)$S$的递增序列是$\prec$关系下的chain，递减序列是$\prec​$关系下的antichain

(d)利用Dilworth’s引理即可。



#### Problem 4

(a)略。

(b)$\forall a,a'$，如果
$$
a\ R\ a'
$$
那么
$$
f(a) =f(a'),a\equiv_f a'
$$
反之，如果
$$
a\equiv_f a'
$$
那么
$$
f(a) =f(a'),a\ R\ a'
$$
