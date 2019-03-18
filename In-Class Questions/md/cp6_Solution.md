#### Problem 1

(a)
$$
(P\text{ AND }\bar Q)\text{ OR }(P\text{ AND } Q) \Leftrightarrow \\
P\text{ AND } (\bar Q\text{ OR } Q )\Leftrightarrow \\
P
$$
(b)

$\Rightarrow$：已知$x\in A$

如果$x\in B$，那么$x\in A\bigcap B$，如果$x\notin B$，那么$x\in A- B$，无论那种情形，都有
$$
x\in (A-B) \bigcup (A\bigcap B)
$$
$\Leftarrow$：已知$x\in (A-B) \bigcup (A\bigcap B)$

那么$x\in A-B$或$x\in A\bigcap B$，无论那种情形， 都有$x\in A$

综上
$$
A= (A-B)\bigcup (A\bigcap B)
$$



#### Problem 2

(a)
$$
\not \exists z.(z\in x)
$$
(b)
$$
\forall u.(u\in x \Leftrightarrow y\in x \text{ OR } z\in x ) 
$$
(c)
$$
\forall z.(z\in x \Rightarrow z\in y)
$$
(d)
$$
(x\subseteq y\bigcup z) \text{ AND }(y\bigcup z\subseteq x)
$$
(e)
$$
\forall u.(u\in x \Leftrightarrow u\in y \text{ AND } u\notin z)
$$
(f)
$$
\forall z.(z \subseteq y \Rightarrow z \in x)
$$
(g)
$$
\forall z.(z\in y\Rightarrow z\in x)
$$




#### Problem 3

(a)因为$(a,b)$有序，而$\{a,b\}$无序

(b)$\{\{1\},\{2\}\}$可以表示$(1,\{2\})$或$(2,\{1\})$

(c)只要说明$\{a,\{a,b\}\}$可以唯一确定$\text{pair}(a,b)$即可。

用$\{c, d\}$表示$\{a,\{a,b\}\}$，如果$c \in d$，那么$a=c, b= d\setminus c$；否则$a=d,b= c\setminus d$



#### Problem 4

假设四个元素为$a,b,c,d$，那么全部可选的集合为
$$
\{ a\},\{b \},\{c \},\{d \}\\
\{ a,b\},\{ a,c\},\{ a,d\},\{b,c \},\{b,d \},\{c,d \} \\
\{ a,b,c\},\{ a,b,d\},\{b,c,d \},\{a,c,d \}
$$
下面分几种情形讨论。

情形一：第一个人选择三个元素，不妨设为$\{a,b,c\}$，那么第二个人选择$\{ d\}$，剩余可选择的集合为：
$$
\{ a\},\{b \},\{c \}\\
\{ a,b\},\{ a,c\},\{b,c \}
$$
这样就可以化为三个元素的情形，所以第二个人胜利。

情形二：第一个人选择一个元素，那么第二个人选择剩余三个元素，这样就可以化为三个元素的情形，所以第二个人胜利。(类似第一种情形)

情形三：第一个人选择两个元素，不妨设为$\{a,b\} $，那么第二个人选择$\{c,d\} $，剩余可选择的集合为：
$$
\{ a\},\{b \},\{c \},\{d \}\\
\{ a,c\},\{ a,d\},\{b,c \},\{b,d \}
$$
接下来进入第二轮，如果第一个人选择一个元素，由对称性，不妨设为$\{a\}$，那么第二个人选择$\{b\}$，剩余可选择的集合为：
$$
\{c\},\{d\}
$$
接下来即为两个元素的情形， 所以第二个人必胜。

如果第一个人选择两个元素，由对称性，不妨设为$\{a,c\}$，那么第二个选择互补的集合$\{b,d\}$，剩余可选择的集合为：
$$
\{ a\},\{b \},\{c \},\{d \}\\
\{ a,d\},\{b,c \}
$$
接下来进入第三轮，如果第一个人选择一个元素，由对称性，不妨设为$\{a\}​$，那么第二个人选择$\{b \}​$，剩余可选择的集合为：
$$
\{c\},\{d\}
$$
接下来即为两个元素的情形， 所以第二个人必胜。

如果第一个人选择两个元素，由对称性，不妨设为$\{a ,d\}$，那么第二个人也选择二元素集$\{b ,c\}$，剩余可选择的集合为：
$$
\{ a\},\{b \},\{c \},\{d \}
$$
接下来必然是一人拿一个的情形， 所以第二个人必胜。