#### Problem 1

(a)$R^{-1}$具有传递性

由定义我们有
$$
x\ R\ y\Leftrightarrow y\ R^{-1}\ x
$$
$\forall a,b,c​$，假设我们有
$$
a\ R^{-1}\ b, b\ R^{-1}\ c
$$
那么
$$
b\ R\ a, c\ R\ b
$$
由$R$的传递性，我们有
$$
c\ R\ a
$$
即
$$
a\ R^{-1}\ c
$$
(b)$R\cap S$具有传递性

$\forall a,b,c​$，假设我们有
$$
a(R\cap S)b, b(R\cap S)c
$$
下面将证明
$$
a(R\cap S)c
$$
由定义，我们有
$$
a\ R\ b,a\ S\ b,b\ R\ c,b\ S\ c
$$
由$R,S$的传递性，我们有
$$
a\ R\ c,a\ S\ c
$$
因此
$$
a(R\cap S)c
$$
(c)$R\circ R$具有传递性

讨论之前先回顾二元关系复合的定义：
$$
a \ R\circ S\ c
$$
当且存在$b$，使得
$$
a\ R\ b且b\ S\ c
$$
$\forall a,b,c$，假设我们有
$$
a \ R\circ R\ b,b\ R\circ R\ c
$$
那么存在$d,e$，使得
$$
a\ R\ d,d\ R\ b,b\ R\ e,e\ R\ c
$$
由传递性，我们有
$$
a\ R\ e, e\ R\ c
$$
因此
$$
a\ R\circ R\ e
$$
(d)不具有传递性，例如取$R$为小于等于，$S$为整除关系。



#### Problem 2

(a)$R_1\cap R_2$是等价关系。

自反性：$\forall a$，我们有
$$
a\ R_1\ a, a\ R_2\ a
$$
所以
$$
a\ R_1\cap R_2\ a
$$
对称性：$\forall a, b$，假设我们有
$$
a\ R_1\cap R_2\ b
$$
所以
$$
a\ R_1\ b, a\ R_2\ b
$$
那么必然有
$$
b\ R_1\ a, b\ R_2\ a
$$
因此
$$
b\ R_1\cap R_2\ a
$$
传递性：$\forall a,b,c$，假设我们有
$$
a\ R_1\cap R_2\ b, b\ R_1\cap R_2\ c
$$
所以
$$
a\ R_1\ b, a\ R_2\ b\\
b\ R_1\ c, b\ R_2\ c
$$
所以
$$
a\ R_1\ c,a\ R_2\ c
$$
因此
$$
a\ R_1\cap R_2\ c
$$
(b)定义集合为一个学校的学生，定义$R_1$为年龄相同，定义$R_2$为两人同班，取
$$
a为1班，15岁\\
b为2班，15岁\\
c为2班，16岁
$$
那么
$$
a\ R_1\cup R_2\ b,b\ R_1\cup R_2\ c
$$
但是不能推出
$$
a\ R_1\cup R_2\ c
$$



#### Problem 3

$G_1$和$G_2$不同构，因为$G_1$中只存在一个长度为$5$的闭环，但是$G_2 $中存在两个。

$G_1​$和$G_3​$不同构，因为$G_1​$中不存在长度为$3​$的闭环，但$G_3​$中存在$6-8-10​$。

$G_1$和$G_4$不同狗，因为$G_1$中不存在长度为$9$的闭环，但$G_4$中存在。

$G_2 $和$G_3$不同构，因为$G_2$中存在两个长度为$5$的闭环，但$G_3$中存在至少三个。

$G_2 ​$和$G_4​$不同构，因为$G_2​$中存在两个长度为$5​$的闭环，但$G_4​$中存在至少三个。

$G_3 $和$G_4$同构，映射如下：
$$
1\leftrightarrow 1\\
6\leftrightarrow 10\\
5\leftrightarrow 9\\
2\leftrightarrow 2\\
9\leftrightarrow 8\\
7\leftrightarrow 3\\
10\leftrightarrow 7\\
8\leftrightarrow 4\\
4\leftrightarrow 6\\
3\leftrightarrow 5
$$



#### Problem 4

(a)反例为一条线段和一个三角形。

(b)Inductive case错误，因不一定要直接添加边，可以删除一条边后再添加两条边。

