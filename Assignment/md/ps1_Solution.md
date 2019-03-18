#### Problem 1

利用反证法，假设$\log_4 6  =\frac m n ,m,n\in \mathbb N且m,n互质$，那么
$$
n\log_4 6  =m\\
\log_4 6^n = m\\
6^n = 4^m\\
3^n = 2^{2m-n}
$$
最后一步显然不可能，所以$\log_4 6 $是无理数



#### Problem 2

考虑如下集合：
$$
N  ::=\{n| n\in \mathbb N , n > 3^{\frac n 3}\}
$$
下面将证明$N$为空集。根据WOP，$N$中存在最小值$n_1$，注意$0,1,2,3,4$满足$n \le 3^{\frac n 3}$，所以$n_1 \ge 4$，由定义可知
$$
n_1 -1 \le 3^{\frac {n_1-1} 3}
$$
那么
$$
n_1 \le 3^{\frac {n_1-1} 3}+1
$$
注意到
$$
3^{\frac {n_1-1} 3}+1 \le   3^{\frac {n_1} 3} \Leftrightarrow 
  3^{-\frac {1} 3}+3^{-\frac {n_1} 3} \le   1
$$
由$n_1 \ge 4$可得
$$
 3^{-\frac {1} 3}+3^{-\frac {n_1} 3}  \le  3^{-\frac {1} 3}+3^{-\frac {4} 3} < 0.925 < 1
$$
从而$3^{\frac {n_1-1} 3}+1 \le   3^{\frac {n_1} 3}$成立，因此
$$
n_1 \le 3^{\frac {n_1-1} 3}+1 \le   3^{\frac {n_1} 3}
$$
这就与$n_1$的定义相矛盾，从而$N$为空集



#### Problem 3

(a)

| $P$  | $Q$  | $P$ IMPLIES $Q$ | $Q$ IMPLIES $P$ | ($P$ IMPLIES $Q$) OR ($Q$ IMPLIES $P$) |
| ---- | ---- | --------------- | --------------- | -------------------------------------- |
| T    | T    | T               | T               | T                                      |
| T    | F    | F               | T               | T                                      |
| F    | T    | T               | F               | T                                      |
| F    | F    | T               | T               | T                                      |

(b)直接取
$$
P\Leftrightarrow Q
$$
注意上式等价于
$$
(P \Leftarrow Q)\text{ AND }(Q \Leftarrow P)\\
(\bar P\text{ OR } Q) \text{ AND } (\bar Q\text{ OR } P)
$$
(c)如果P is valid ，那么没有一个环境可以使得NOT(P)成立，即NOT(P) is not satisfiable，反之也成立。

(d)
$$
S= (\text{NOT } P_1) \text{ OR }  (\text{NOT } P_2) ...  (\text{NOT } P_n)
$$
如果$S$是valid，那么$P_i$不能全为T，所以$P_1,...,P_k$不是consistent，反之，因为$P_i$不能全为T，所以$S$是valid



#### Problem 4

(a)
$$
p_0= a_0 \text{ XOR } 1\\
c = a_0 \text{ AND } 1
$$

(b)如果$b=1$，则$o_i=p_i$，否则$o_i =a_i$，从而
$$
o_{i}=(p_{i} \text{ AND } b)\text{ OR }(a_i \text{ AND } (\text{ NOT }b))
$$
(c)如果$c_{(1)}=1$，那么$c=c_{(2)}$，否则$c=c_{(1)}=0$，从而
$$
c= c_{(1)} \text{ AND }  c_{(2)}
$$
(d)如果$c_{(1)}=1$，那么$p_{i}=r_{i-(n+1)}$，否则$p_i= a_i$，从而
$$
p_{i}=(r_{i-(n+1)} \text{ AND } c_{(1)})\text{ OR }(a_{i} \text{ AND } (\text{ NOT }c_{(1)}))
$$
(e)假设$n=2^k $位需要的操作次数为$T(2^k)$，注意前一半和后一半的加法可以同时完成，完成之后我们只要计算根据$c_{(1)}$的值判断输出结果即可，所以
$$
T(1)= 2\\
T(2^k)= T(2^{k-1})+1\\
T(2^k)= O(k)\\
T(n)= O(\log n)
$$
