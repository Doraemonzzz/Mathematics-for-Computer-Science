#### Problem 1

| $P$  | $Q$  | $R$  | $Q \text{ AND } R$ | $P \text{ OR } Q$ | $P \text{ OR } R$ | $P\text{ OR }(Q \text{ AND } R)$ | $(P \text{ OR } Q) \text{ AND }(P \text{ OR } R)$ |
| ---- | ---- | ---- | ------------------ | ----------------- | ----------------- | -------------------------------- | ------------------------------------------------- |
| 1    | 1    | 1    | 1                  | 1                 | 1                 | 1                                | 1                                                 |
| 1    | 1    | 0    | 0                  | 1                 | 1                 | 1                                | 1                                                 |
| 1    | 0    | 1    | 0                  | 1                 | 1                 | 1                                | 1                                                 |
| 1    | 0    | 0    | 0                  | 1                 | 1                 | 1                                | 1                                                 |
| 0    | 1    | 1    | 1                  | 1                 | 1                 | 1                                | 1                                                 |
| 0    | 1    | 0    | 0                  | 1                 | 0                 | 0                                | 0                                                 |
| 0    | 0    | 1    | 0                  | 0                 | 1                 | 0                                | 0                                                 |
| 0    | 0    | 0    | 0                  | 0                 | 0                 | 0                                | 0                                                 |



#### Problem 2

(a)
$$
\neg L \to Q\\
\neg L \to B\\
\neg L \leftrightarrow N\\
\neg Q \to B \\
\neg B
$$
(b)要使得上述命题全真，则$B$必然为F，然后根据上述关系可得

| $L$  | $Q$  | $B$  | $N$  |
| ---- | ---- | ---- | ---- |
| T    | T    | F    | F    |

(c)由填表的过程不难看出使得上述命题全真的情形唯一。



#### Problem 3

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
d_0 =a_{0}\text{ XOR } b_{0},c_0=a_{0} \text{ AND } b_{0}
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



#### Problem 4

因为这里要考虑语义，母亲的话中明显有“如果写完作业，就能看电视”的含义，由于连续不一定可导，所以数学家的话不能翻译为IFF

