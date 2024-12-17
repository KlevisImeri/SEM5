exp1: Derivate
$$x(t)=\epsilon(t)-\epsilon(t-\tau)\sin\left( \frac{\pi t}\tau \right)$$
$$x'(t)=(\delta(t)-\delta(t-\tau)\sin\left( \frac{\pi t}{\tau} \right)+(\epsilon(t)-\epsilon(t-\tau)) \frac{\pi}{\tau}\cos\left( \frac{\pi t}{\tau} \right)$$

exp2: Are these stepping in fumctinos?
1. $\epsilon[k-2]$ yes
2. $\sin 2(t-1)$ no
3. $\epsilon(t-1) \sin(2(t-1))$ yes

exp 3  period?
$cos(4t+5) \quad w=2 \frac{\pi}{t} = \frac{\pi}{2}$ periodic
$cos[0.2k] \quad T=\frac{\pi}{0.2}\in \mathbf{I}$  not periodic
$cos[0.17\pi k] \quad L=\frac{2}{0.17}=\frac{200}{17} \in \mathbf{Q}$  periodic


```tikz
\begin{document}

\begin{tikzpicture}
    % Draw the unit circle
    \draw[thick] (0,0) circle (2cm);

    % Draw the x and y axes
    \draw[thick,->] (-2.5,0) -- (2.5,0) node[anchor=west] {$x$};
    \draw[thick,->] (0,-2.5) -- (0,2.5) node[anchor=south] {$y$};

    % Define the angle (e.g., 45 degrees = pi/4)
    \def\angle{45}
    \def\radius{2}

    % Draw angle arc
    \draw[thick,->] (0,0) -- ({\radius*cos(\angle)},{\radius*sin(\angle)}) 
    node[midway, anchor=north east] {$r=1$};

    % Draw angle indicator
    \draw[thick] (0:1cm) arc (0:\angle:1cm);
    \node at (0.8cm, 0.3cm) {$\theta$};

    % Projection on the x-axis (cosine)
    \draw[dashed] ({\radius*cos(\angle)},0) -- ({\radius*cos(\angle)},{\radius*sin(\angle)});
    \node[anchor=north] at ({\radius*cos(\angle)}, 0) {$\cos(\theta)$};

    % Projection on the y-axis (sine)
    \draw[dashed] (0,{\radius*sin(\angle)}) -- ({\radius*cos(\angle)},{\radius*sin(\angle)});
    \node[anchor=east] at (0,{\radius*sin(\angle)}) {$\sin(\theta)$};

    % Draw discrete steps (e.g., for 30°, 60°, etc.)
    \foreach \i in {0,30,60,90,120,150,180,210,240,270,300,330} {
        \draw[thick,->,red] (0,0) -- ({\radius*cos(\i)},{\radius*sin(\i)});
    }

\end{tikzpicture}
\end{document}
```
p
exp 4:
```tikz
\begin{document}
\begin{tikzpicture}
    \draw[thick] (0,0) rectangle (3,2);
    \node at (1.5, 1) {System};
    \draw[thick,->] (-2,1) -- (0,1) node[midway, above] {$u[k]$};
    \draw[thick,->] (3,1) -- (5,1) node[midway, above] {$y[k]$};
\end{tikzpicture}
\end{document}
```

$y[k]=u[k+1]$ Not casual $y[0]=u[1]$

exp 5: linear? time invariant?
CT: $y(t)=5u'(t)$ LTI
$$5(u[k_{1}]+u[k_{2}])'=5(u[k_{1}])'+5(u[k_{2}])'=y[k_{2}]+y{k_{1}}$$
$$5c*u[t]=c*y[t]$$
$$5u[k-i]=y[k-i]$$

DT: $y[k]=y^ku[k]$
$$f(u[k_{1}]+u[k_{2}])=y^k(u[k_{1}]+u[k_{2}]))= y[k_{1}]+y[k_{2}]$$

CT: $g(t)=5u(t)+4$
$$f(c*u(t))=5cu(t)+4\neq c(5u(t)+4)=cf(u(t))$$
so not linear but TI.

ex:
$$y[k]=\frac{1}{4}u[k+1]+\frac{1}{2}u[k]+\frac{1}{4}u[k-1]$$
a. $h[k]=$
b. causual? Not 
c. FIR YES
d BIBO? Stable
$$u[k]=\delta[k]\iff y[k]=h[k]$$
$$h[k]=\frac{1}{4}\delta[k+1]+\frac{1}{2}\delta[k]+\frac{1}{4}\delta[k-1]$$
$$\sum_{k=\infty}^\infty |h[k]| <  \infty \to \frac{1}{4}+\frac{1}{4} +\frac{1}{4} =1 < \infty$$

ex:
$$h[k]=-15 *0.8^k\epsilon [k]+2.5\delta[k]$$
$$u[k]=\epsilon[k]0.6^k$$
$$y[k]=?$$

$$\sum_{i}u[i]h[k-i] = \sum_{k}u[k-i]h[i]$$
$$y[k]=\sum_{i}u[i]h[k-i]=\sum_{i}\epsilon[i]0.6^i(-15 *0.8^{k-i}\epsilon [k-i]+2.5\delta[k-i])$$
$$=-15\sum_{i}0.6^i0.8^{k-i}\epsilon[i]\epsilon[k-i]+2.5\sum_{i}0.6^i\epsilon[i]\delta[k-i]$$$$= -15\sum_{i=0}^{k}0.6^{i}0.8^{k-i} +2.5 \cdot 0.6^{k}$$ k>=0 else 0
 if k>=0 else 0.6^k =0
