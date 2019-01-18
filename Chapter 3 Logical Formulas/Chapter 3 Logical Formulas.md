#### Problem 3.1

新的真值表为

| $P$  | $Q$  | $P$ IMPLIES $Q$ |
| ---- | ---- | --------------- |
| T    | T    | T               |
| T    | F    | F               |
| F    | T    | F               |
| F    | F    | F               |

不难看出新的$\Rightarrow$即为AND关系



#### Problem 3.2

(a)$R$ AND NOT($Q$)

(b)$P$ AND $Q$ AND $R$

(c)$R$ IMPLIES $P$

(d)$P$ AND NOT($Q$) AND $R$



#### Problem 3.3

因为这里要考虑语义，母亲的话中明显有“如果写完作业，就能看电视”的含义，由于连续不一定可导，所以数学家的话不能翻译为IFF



#### Problem 3.4

代码如下：

```python
def f(n):
    if n == 1:
        return [["T"], ["F"]]
    else:
        temp = f(n - 1)
        r1 = [i + ["T"] for i in temp]
        r2 = [i + ["F"] for i in temp]
        return r1 + r2
result = f(5)
for i in result:
    print(" ".join(i))
```



#### Problem 3.5

(a)该题即为模拟二进制数和一位的二进制数的加法，两个二进制相加是用XOR运算，进位是用AND运算，所以可得：
$$
c_0 =b\\
s_k = a_{k} \text{ XOR } c_{k},
c_{k} = a_{k-1}\text{ AND } s_{k-1}
$$
(b)利用(a)一位一位相加，把上述过程用下图表示，$d_i$表示结果，$c_i$表示进位：

![](https://github.com/Doraemonzzz/Mathematics-for-Computer-Science/blob/master/photo/Chapter%203/C3P5_1.png?raw=true)

由于末位加法不需要考虑进位，所以称为half Adder，具体关系如下图：

![](https://github.com/Doraemonzzz/Mathematics-for-Computer-Science/blob/master/photo/Chapter%203/C3P5_2.png?raw=true)

所以
$$
d_0 =a_{0}\text{ AND } b_{0},c_0=a_{0} \text{ XOR } b_{0}
$$
其余位数的加法要考虑进位问题，所以称为full Adder，具体关系如下图：

![](https://github.com/Doraemonzzz/Mathematics-for-Computer-Science/blob/master/photo/Chapter%203/C3P5_3.png?raw=true)

首先$a,b$做XOR运算，得到临时结果$s$，然后和之前的进位$c_{in}$再做一次XOR运算，得到最终结果$d$，然后计算进位$c_{out}$，不难看出之前两次运算如果有一次有进位，那么$c_{out}=1$，因此$c_{out} = (c_{in}\text{ AND } s) \text{ OR }(a\text{ AND } b)$

把之前的结果整理归纳可得
$$
d_0 =a_{0}\text{ AND } b_{0},c_0=a_{0} \text{ XOR } b_{0} \\
s_i = a_{i} \text{ XOR } b_{i}, d_i =c_{i-1} \text{ XOR }s_i\\
c_i = (c_{i-1}\text{ AND } s_i) \text{ OR }(a_{i}\text{ AND } b_{i})
$$
(c)从(b)中不难看出每一轮要做$5$次逻辑运算，结合一开始$2$次，所以一共要$5n+2$次



#### Problem 3.6

(a)
$$
p_0= a_0 \text{ XOR } 1\\
c = a_0 \text{ AND } 1
$$

(b)如果$b=1$，则$o_i=p_i$，否则$o_i =a_i$，从而
$$
p_{i}=(p_{(i)} \text{ AND } b)\text{ OR }(a_i \text{ AND } (\text{ NOT }b))
$$
(c)如果$c_{(1)}=1$，那么$c=c_{(2)}$，否则$c=c_{(1)}=0$，从而
$$
c= c_{(1)} \text{ AND }  c_{(2)}
$$
(d)如果$c_{(1)}=1$，那么$p_{i}=r_{i-(n+1)}$，否则$p_i= a_i$，从而
$$
p_{i}=(a_{i} \text{ AND } c_{(1)})\text{ OR }(r_{i-(n+1)} \text{ AND } (\text{ NOT }c_{(1)}))
$$
(e)假设$n=2^k $位需要的操作次数为$T(2^k)$，注意前一半和后一半的加法可以同时完成，所以
$$
T(1)= 2\\
T(2^k)= T(2^{k-1}) +3k+1\\
T(2^k)= \frac 3 2 k^2 +\frac 5 2 k + 2 \\
T(n)= \frac 3 2 \log ^2n  +\frac 5 2 \log n +2
$$



#### Problem 3.7

(a)如果用真值表，需要$2^5=32$行

(b)要使得上式为True，那么$M$为True，$N$为False，如果$P$为True，那么$Q,R,S$为True；如果$P$为False，那么$Q,R,S$为False，所以一共有两种truth environments 

#### Problem 3.8

- 1.S，$M:T,Q:T$时成立

- 2.S，$M:F,P和Q任意$时成立

- 3.S，$M:T,P:F$时不成立，$M:T,Q:T$时成立

- 4.S，$P:T,Q:F$时不成立，$P:T,Q:T$时成立

- 5.注意
  $$
  (\overline {P}\text{ AND } \overline {Q})= \text{ NOT }(P \text{ OR Q})
  $$
  所以S，$P:F,Q:F$时成立

- 6.S，$P:F,Q:F,M:F$时成立

- 7.S，$P:F,Q:T$时成立

- 8.V

  | $P$  | $Q$  | $\overline {P}$ | $\overline {Q}$ | $P \text{ XOR }Q$ | $\overline {P}\text{ OR } \overline {Q}$ |
  | ---- | ---- | --------------- | --------------- | ----------------- | ---------------------------------------- |
  | T    | T    | F               | F               | F                 | F                                        |
  | T    | F    | F               | T               | T                 | T                                        |
  | F    | T    | T               | F               | T                 | T                                        |
  | F    | F    | T               | T               | F                 | T                                        |

- 9.S，$P,Q,M$都为$T$时成立



#### Problem 3.9

第一个式子只有在$P,Q,R$全为$F$时才为$F$，否则都为$T$。第二个式子如果$P,Q,R$全为$F$时则为$F$，否则至少存在一个$T$，不妨设为$P$，如果$Q,R$都是$T$，那么$P$ AND $Q$ AND $R$为$T$；如果$Q,R$都是$F$，那么$P$ AND (NOT $Q$)为$T$；如果一个为$T$，一个为$F$，那么$P$ AND (NOT $Q$)和$Q$ AND NOT ($P$)至少有一个为$T$，从而第二个式子也只有$P,Q,R$全为$F$时才为$F$，否则都为$T$。因此结论成立。



#### Problem 3.10

由狄摩根律即可得到，这里略过穷举。



#### Problem 3.11

(a)

| $P$  | $Q$  | $P$ IMPLIES $Q$ | $Q$ IMPLIES $P$ | ($P$ IMPLIES $Q$) OR ($Q$ IMPLIES $P$) |
| ---- | ---- | --------------- | --------------- | -------------------------------------- |
| T    | T    | T               | T               | T                                      |
| T    | F    | F               | T               | T                                      |
| F    | T    | T               | F               | T                                      |
| F    | F    | T               | T               | T                                      |

(b)(NOT(P OR Q)) OR (P AND Q)

(c)如果P is valid ，那么没有一个环境可以使得NOT(P)成立，即NOT(P) is not satisfiable，反之也成立。

(d)
$$
S= (\text{NOT } P_1) \text{ OR }  (\text{NOT } P_2) ...  (\text{NOT } P_n)
$$
如果$S$是valid，那么$P_i$不能全为T，所以$P_1,...,P_k$不是consistent，反之，因为$P_i$不能全为T，所以$S$是valid



#### Problem 3.12

(a)
$$
\neg L \to Q\\
\neg L \to B\\
\neg L \leftrightarrow N\\
\neg Q \to B \\
\neg B
$$
(b)要使得上述命题全真，则必然有$B$为F，然后根据上述关系可得

| $L$  | $Q$  | $B$  | $N$  |
| ---- | ---- | ---- | ---- |
| T    | T    | F    | F    |

(c)由填表的过程不难看出使得上述命题全真的情形唯一。



#### Problem 3.13

(a)因为
$$
A \text{ IFF }B = (A\text{ IMPLIES } B) \text{ AND }(B\text{ IMPLIES } A)
$$
所以
$$
A \text{ IFF }B = (\text{NOT}(A)\text{ OR } B) \text{ AND }(\text{NOT}(B)\text{ OR } A)
$$
对于异或运算
$$
A \text{ XOR }B =
(\text{NOT}(A)\text{ AND } \text{NOT}(B)) \text{ OR } 
(A\text{ AND } B)
$$
(b)
$$
A \text{ AND }B = \text{NOT}(\text{NOT}(A)\text{ OR } \text{NOT}(B))
$$
(c)
$$
\text{NOT}(A \text{ AND }B) 
=(\text{NOT } A) \text{ OR }(\text{NOT } B)
$$
