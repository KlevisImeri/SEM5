
$$\begin{align}
x[k+1]=Ax[k]+\underline{b}u[k] \\
y[k]=\underline{c}x[k] + Du[k]
\end{align} \quad x^T=[x_{1}, x_{2} , \dots, x_{n}]$$
$$y[k]=\begin{cases}
C^Tx[0]+Du[0]  \quad k=0\\
c^TA^kx[0]+\sum_{i=0}^{k-1}C^TA^{k-1-i}Bu[i]+Du[k] \quad k\in \mathbf{Z}_{+}
\end{cases}$$

$$\begin{align}
x_{1}[k+1]=0x_{1}[k]-0.24x_{2}[k]-0.24u[k] \\
x_{2}[k+1]=x_{1}[k]+x_{2}[k]+1.5u[k] \\
y[k]=x_{2}[k]+u[k] \\
u[k]=\epsilon[k]0.5^k \to y[k]=?
\end{align}$$
$$X[k+1]=\begin{bmatrix}
x_{1}[k+1] \\
x_{2}[k+1]
\end{bmatrix} = \begin{bmatrix}
0 & -0.24 \\
1 & 1
\end{bmatrix} \begin{bmatrix}
x_{1}[k] \\
x_{2}[k]
\end{bmatrix} + \begin{bmatrix}
-0.24 \\
1.5
\end{bmatrix} u[k]$$
$$y[k]=\begin{bmatrix}
0 & 1
\end{bmatrix}\begin{bmatrix}
x_{1}[k] \\
x_{2}[k]
\end{bmatrix}+1u[k]$$
$$y[0]=1\epsilon[0]0.5^0=1$$
$$A^k_{n\times n}= \sum_{i=1}^n \lambda_{i}^kL_{i} \quad L_{i}=\Pi_{p=1 p\neq i}^n \frac{{A-\lambda_{p}I}}{\lambda_{i}-\lambda{p}}$$


$$y[k]=\sum_{i=0}^{k-1-i}c^TA^{k-i-1}Bu[i]=\sum_{i=0}^{k-1-i}\underline{c}^T(\lambda_{1}^{k-i-1}L_{1}+\lambda_{2}^{k-i-1}L_{2})\underline{b}u[i]=\sum_{i=0}^{k-i-1}(k_1\lambda_{1}^{k-1-i}+k_{2}\lambda_{2}^{k-i-1})u[k]$$

$$A=\begin{bmatrix}
0 & -0.24 \\
1 & 1
\end{bmatrix}$$
$$|A-\lambda I|=|\lambda I-A|=\begin{bmatrix}
\lambda & 0.24 \\
-1 & \lambda-1
\end{bmatrix}=\lambda^2-\lambda +0.24$$
$$\lambda_{1}=0.6, \lambda_{2}=0.4$$
$$L_{1}=\frac{{A-\lambda_{2} I}}{\lambda_{1}-\lambda_{2}}=\begin{bmatrix}
-2 & -1.2 \\
5 & 3
\end{bmatrix}$$
$$L_{2}=\frac{{A-\lambda_{1} I}}{\lambda_{2}-\lambda_{1}}=\begin{bmatrix}
3 & 1.2 \\
-5 & -2
\end{bmatrix}$$
Check:
$$L_{1}+L_{2}=I$$
$$k_1=c^TL_{1}b=\begin{bmatrix}
0 & 1
\end{bmatrix} \begin{bmatrix}
-2 & -1.2 \\
5 & 3
\end{bmatrix}\begin{bmatrix}
-0.24  \\
1.5
\end{bmatrix}=3.3$$$$k_{2}=c^TL_{2}b=-1.8$$
$$y[k]=\sum_{i=0}^{k-1}(3.3\cdot 0.6^{k-1-i}+1.8\cdot 1.4^{k-1-i})\epsilon[k]\cdot 0.5^i+1\cdot u[k]\cdot 0.5^k$$
$$y[k]=3.3 \cdot 0.6^{k-1}\sum_{0}^{k-1}\left( \frac{0.5}{0.6} \right)^i+1.8 \cdot 1.4^{k-1}\sum_{0}^{k-1}\left( \frac{0.5}{1.4} \right)^i+\epsilon[k]0.5^k$$
$$=(33\cdot0.6^k+18\cdot0.4^k-14\cdot 0.5^k)\epsilon[k]$$
The Free part is the one with the one with Eigen values and the other part is the the exited part.