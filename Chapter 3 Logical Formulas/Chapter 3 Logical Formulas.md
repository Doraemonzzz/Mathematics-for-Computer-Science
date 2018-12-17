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



由于末位加法不需要考虑进位，所以称为half Adder，具体关系如下图：



所以
$$
d_0 =a_{0}\text{ AND } b_{0},c_0=a_{0} \text{ XOR } b_{0}
$$
其余位数的加法要考虑进位问题，所以称为full Adder，具体关系如下图：



首先$a,b$做XOR运算，得到临时结果$s$，然后和之前的进位$c_{in}$再做一次XOR运算，得到最终结果$d$，然后计算进位$c_{out}$，不难看出之前两次运算如果有一次有进位，那么$c_{out}=1$，因此$c_{out} = (c_{in}\text{ AND } s) \text{ OR }(a\text{ AND } b)$

把之前的结果整理归纳可得
$$
d_0 =a_{0}\text{ AND } b_{0},c_0=a_{0} \text{ XOR } b_{0} \\
s_i = a_{i} \text{ XOR } b_{i}, d_i =c_{i-1} \text{ XOR }s_i\\
c_i = (c_{i-1}\text{ AND } s_i) \text{ XOR }(a_{i}\text{ AND } b_{i}) 
$$
(c)从(b)中不难看出每一轮要做$5$次逻辑运算，结合一开始$2$次，所以一共要$5n+2$次