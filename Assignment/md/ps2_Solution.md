#### Problem 1

(a)
$$
\text{Members}(p, a, b) ::= z\in p \text{ IFF } z=a \text{ OR } z=b
$$
(b)
$$
\text{Pair}(p,a,b)::=\text{Members}(p, a,\text{Members}(q,a,b))
$$
(c)
$$
\text{Second}(p,b)::= \exists a, s.t \  a\in\text{Pair}(p,a,b)
$$



#### Problem 2

$\forall x \in \overline {A\cap B}​$，记
$$
P\triangleq \{x\in A\} ,Q \triangleq \{x\in B\}
$$
那么$ x \in \overline {A\cap B}$等价于
$$
\text{NOT}(P\text{ AND } Q)
$$
上述命题等价于
$$
 \overline P \text{ OR }  \overline Q
$$
所以$x\in \overline A$或$x\in \overline B$，因此
$$
x \in \overline A \cup  \overline B
$$
反之同理。



#### Problem 3

(a)不妨设原始集合为$R_0, S_0​$，经过有限次拼接后并取并集（去重）的集合为$R_1, S_1​$，两者的补集为$\overline {R_1}, \overline {S_1}​$，为了方便说明，记$R_0 \cup S_0​$经过有限次拼接取并后生成的集合为$T​$，那么一共只有四种情形：
$$
R = R_1 ,S=S_1 \\
R = R_1 ,S=  \overline {S_1} \\
R=\overline {R_1}, S =S_1 \\
R = \overline {R_1} ,S=  \overline {S_1}
$$
由对称性，情形2,3只需要讨论一种，这里只考虑情形2。

第一种情形：$\forall x\in R\cap S$，那么$x\in R_1 \cap S_1$，所以$R\cap S$可以由$R_0 \cup S_0$经过有限次拼接取并后生成，这说明$R\cap S$是c-d。

第二种情形：$\forall x\in R\cap S$，那么$x\in R_1 \cap \overline {S_1}$，因此$R\cap S\subset R_1$，所以$R\cap S$可以由$R_0 $经过有限次拼接取并后生成，这说明$R\cap S$是c-d。

第四种情形：$\forall x\in R\cap S$，那么$x\in \overline {R_1}\cap \overline {S_1} = \overline {R_1 \cup S_1}$，注意$R_1 \cup S_1$可以由$R_0 \cup S_0$经过有限次拼接取并后生成，这说明$R\cap S$是c-d。

(b)(c)(d)暂时没思路，略过。

(e)首先$\{00\}^*\cap 0^*$显然不是有限集，其次$\{00\}^*$的补集必然包含长度为奇数的全$0$序列，所以$\overline {\{00\}^*}\cap 0^*$不是有限集，因此$\{00\}^*$不是0-boring。

(f)分四种情形考虑
$$
R是\text{0-finite}, S是\text{0-finite}\\
\overline R是\text{0-finite}, S是\text{0-finite} \\
R是\text{0-finite},\overline  S是\text{0-finite} \\
\overline R是\text{0-finite},\overline  S是\text{0-finite}
$$
由对称性，情形2,3只需要讨论一种，这里只考虑情形2。

第一种情形：
$$
|(R\cup S) \cap 0^* |=|(R\cap 0^* )\cup (S\cap 0^* )|\le  |R\cap 0^* | +|(S\cap 0^* )| <\infty
$$
所以$R\cup S​$是boring。

第二种情形：
$$
|\overline {(R\cup S)} \cap 0^*| =|(\overline R\cap \overline S) \cap 0^*| \le

 |\overline R\cap 0^* | <\infty
$$
所以$R\cup S​$是boring。

第四种情形：
$$
|\overline {(R\cup S)} \cap 0^*| =|(\overline R\cap \overline S) \cap 0^*| \le

 |\overline R\cap 0^* | <\infty
$$
所以$R\cup S$是boring。

(g)分三种情形讨论。

第一种情形， $R,S$都是$\text{0-finite}$，那么
$$
|R.S\cap 0^*| \le |R\cap 0^*| |S\cap 0^*|  <\infty
$$
$R.S​$是boring。

第二种情形，$R$中$S$至少有一个不包含全$0$的字符串以及空串，那么
$$
|R.S\cap 0^*| =0  <\infty
$$
第三种情形，$R,S$都包含全$0$的字符串以及空串，且不都是$\text{0-finite}$，不妨设$R$不是$\text{0-finite}$，那么$\bar R$是$\text{0-finite}$，注意$R,S$包含空串，所以我们有
$$
R\subset R.S
$$
因此
$$
\overline{R.S} \subset \bar R
$$
所以
$$
\begin{aligned}
|\overline{R.S}\cap 0^*|
&\le |\overline{R}\cap 0^*| \\
&<\infty
\end{aligned}
$$
那么$R.S​$是boring。

(h)如果$R​$是boring，那么$\overline R​$也是boring，因为c-d语言是由并，拼接以及补操作构造的，所以由(f)，(g)，(h)可知，c-d语言是boring。