---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
#imports
import numpy as np
import matplotlib.pyplot as plt
import math
e = math.e
pi = math.pi
inf = 10;

def setup_plot(title, xlabel="Time", ylabel="Value"):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.title(title)

def plotd(x, y): # plot discreate
    plt.plot(x,y,'o')
    vdashed(x,y)
    
def vdashed(x, y):
    for xi, yi in zip(x, y):
        plt.vlines(xi, 0, yi, colors='darkgray', linestyles='dashed')

def eps(x):
    return np.where(x>=0,1,0)
    
def delta(x):
    return np.where(x==0,1,0)
    
def dirac(x, epsilon=1e-10):
    return np.where(np.abs(x) <= epsilon, inf, 0)
```

```python

```

# Intro
- Zoltan Horvath
- V1 517
- horvi@evt.bme.hu
- szalay@hvt.bme.hu 
- www.kalotaapitvany.hu/romanika
- Book: G.Fodor: Signals, Systems and Networks ISBN 936 05 7924 3


# Signals

> Mathematical description of the 'interesting part' of the physical process

- **Deterministic** s.   -> for this subject
	- Value at all time t is know (can be calculated)
	- repeatable

- **Stochastic** s.
	- not repeatable
	- similar seeming process(es) gives different results
	- stochastic features that can be detected

Deterministic <-> Stochastic  /oposites

> CT signal  :=  $x=x(t), t\in \mathbb{R}$ <br>
> DT signal := $x=x[t], t\in \mathbb{Z}$


```python
# CT and CV
x = np.linspace(-5, 6, 100)
y = x**2
plt.plot(x, y)
setup_plot("CT and CV")
plt.show()

# CT and DV
x = np.linspace(-5, 6, 100)
y = np.round(x**2, -1)
plt.plot(x, y)
setup_plot("CT and DV")
plt.show()

# DT and CV
x = np.arange(-5, 6, 2)
y = x**2
plt.plot(x, y, 'o')
vdashed(x,y)
setup_plot("DT and CV")
plt.show()

# DT and DV
x = np.arange(-5, 6, 2)
y = np.round(x**2, -1)
plt.plot(x, y, 's')
vdashed(x,y)
setup_plot("DT and DV")
plt.show()
```

## Producing 
-  CTs :=$x(t)$ --sampling(regular)-> $x[k] = x(kT)$ T:=sample period
-  independently from CT S. ex. throwing cube. Ex:
	- k number of throwing
	- x[k] result of throwing
	- k=1,5 (cant be turn into CT's)

Ex sampling:
- $e^{\alpha t}$ <-> $a^k$
- $A\cos(wt)$ <-> $A\cos(\theta k)$


## Main functoins
We only talk about CV:

#### DT Signals
***DT Unit step:***
$$ \epsilon[k] =
\begin{cases} 
0, & k \in \mathbb{Z^-} \\
1, & k \in \mathbb{N}
\end{cases}$$

```python
x = np.arange(-5,6)
y = eps(x)
plotd(x,y)
setup_plot("DT Unit Step", "k", r"$\epsilon[k]$")
```

 ***DT Unit impulse***
 $$\delta[k] = \begin{cases}
 0, k\in \mathbb{Z^-} \\
 1, k=0 \\
 0, k \in \mathbb{Z^+}
 \end{cases}$$

```python
x = np.arange(-5,6)
y = delta(x)
plotd(x,y)
setup_plot("DT unit pulse")
```

 ### Operations
- shifting $x[k]=\delta[k-2]$ (you just +/- left/right the input, here is k);
- windowing:
    - take a window form $-\tau$ to $\tau$
    - $w[k]=\epsilon[k+\tau]-\epsilon[k-\tau-1]$
    - multiply with given $f[k]$
    - $w[k]f[k] = r[k]$ which is the windowed function
- production with convolution (i see it as expanding)
 $$x[k]=\sum^\infty_{i=-\infty}=x[i]\delta[k-i]$$
 $$x[k]=
 \begin{cases}
 2^k & [0,\infty) \\
  0  & (-\infty,0)\\
 \end{cases}
 =\sum_{i=0}^\infty 2^i\delta[k-i]=1\delta[k]+2\delta[k-1]+4\delta[k-2]+...$$

```python
x = np.arange(-5,6)
y = delta(x-2)
plotd(x,y)
setup_plot("Shifting")
plt.show()

x = np.arange(-5,6)
tau = 2
y = eps(x+tau)-eps(x-tau-1)
z = 2*x;
plotd(x,y*z)
setup_plot("Windowing")
plt.show()


x = np.arange(-3,4)
f = np.where(x>=0,2.0**x,0)
n = np.array([delta(x-i) for i in x])
y = np.sum(f*n, axis=0)
# y = np.where(x>=0, np.sum([2.00 ** i * delta(x - i) for i in x], axis=0), 0)
plotd(x,y)
setup_plot("Convolution")
plt.show()


```

1. Unit step with unit impulse
$$\epsilon[k]=\delta[k]+\delta[k-1]+\delta[k-2]..=\sum_0^\infty\delta[k-i]$$
2. Unit impulse with unit step
$$\delta[k]=\epsilon[k]-\epsilon[k-1]$$

```python
x = np.arange(-3,4)

y = np.sum([delta(x-i) for i in range(0,4)], axis=0)
plotd(x,y)
setup_plot("Unit step as sum of unit impulses")
plt.show()

y = eps(x)-eps(x-1)
plotd(x,y)
setup_plot("Unit impulse as sum of unit steps")
plt.show()
```

#### CT signals

ex: $e^{\alpha t}$,  $A\cos(wt)$,

***CT Unit step:*** 
$$\epsilon(t)=
\begin{cases}
0 & t \in \mathbb{R^-}\\ 
1 & t \in [0,\infty)\\
\end{cases}
$$ 



```python
x = np.arange(-3,4, 0.01)
y = eps(x)
plt.plot(x,y)
```

***CT Unit impulse / Dirac - impulse*** 
let:
> $$\delta(t,\tau) = \frac{\epsilon(t) - \epsilon(t-\tau)}{\tau} , \quad 0<t<\tau$$
> $$\text{Dirac-Impulse} =\delta(t)=\lim_{\tau\rightarrow 0} \delta(t,\tau) = \frac{\epsilon(t) - \epsilon(t-\tau)}{\tau}$$

Not a function. Generalized function
$$\delta(0) = \infty \quad$$
Distribution
$$\int_{-\infty}^\infty \delta[t]=1\quad$$ 

> The value may be infty ***but the integral is 1***

```python
t = np.arange(-3,4,0.01);
tau = 2.5;
y = (eps(t)-eps(t-tau))/tau
plt.plot(x,y)
plt.show()
tau = 2;
y = (eps(t)-eps(t-tau))/tau
plt.plot(x,y)
tau = 1;
y = (eps(t)-eps(t-tau))/tau
plt.plot(x,y)
tau = 0.5;
y = (eps(t)-eps(t-tau))/tau
plt.plot(x,y)
tau = 0.2;
y = (eps(t)-eps(t-tau))/tau
plt.plot(x,y)
tau = 0.1;
y = (eps(t)-eps(t-tau))/tau
plt.plot(x,y)
```

### Operations:
 - shifting  $\epsilon(t-2)$
 - windowing:  $f(t)*(e(t-\tau)-e(t+\tau)) = p(t)$ you just cut  a window out.

```python
t = np.arange(-3,4,0.01)
y = eps(t-2)
plt.plot(t,y)
setup_plot("Shifting")
```

```python
t = np.arange(-3,4,0.01)
tau = 1.5;
w = eps(t+tau)-eps(t-tau)
f = 3*t
plt.plot(t,w*f)
setup_plot("Windowing")
```

Ex decomposition of the fucntion with unit step:
$$x(t)=
\begin{cases}
1 & t<0  & \rightarrow \epsilon(-t)-\delta[t]\\ 
2t & 0\leq t<10 & \rightarrow 2t(\epsilon(t)-\epsilon(t-10))\\
e^{-2t} & t\leq 10 & \rightarrow e^{-2t}\epsilon(t-10) \\
\end{cases}
$$
$$x(t)=\epsilon(-t)+ 2t(\epsilon(t)-\epsilon(t-10)) + e^{-2t}\epsilon(t-10)$$

```python
t = np.arange(-5,16,0.01)
y = eps(-t)+2*t*(eps(t)-eps(t-10))+e**(-2*t)*eps(t-10)
plt.plot(t,y)
setup_plot("Decompose with unit step")
```

## Generalized deravitie
> let: <br>
> x(t) := be a func. <br>
> x'(t) := generalized deravitie of x(t) <br>
> then:
> $$x(t)=\int_{t_0}^t x'(\tau)d\tau + x(t_0)$$

Ex:
$$\epsilon(t)= \int_{-\infty}^t\delta(\tau)d\tau$$
$$ \delta(t)=\epsilon'(t)$$

Product with unit step:
$$(x(t)\epsilon(t))' = x'(t)\epsilon(t)+x(0^+)\delta(t)$$

Ex:
$$x(t)=(2+e^{-4t})\epsilon(t) \quad x(0)=3\epsilon(t) $$ 
$$x'(t)=-4e^{-4t}\epsilon(t) + 3\delta(t)$$
$$\int_{0}^t x'(\tau)d\tau+x(0)=[x(t)]^t_0-x(0)=(x(t)+x(0))-x(0)=x(t)$$

```python
inf = 5

t = np.arange(-1,1,0.01)
y = (2+e**(-4*t))*eps(t)
dy = -4*e**(-4*t)*eps(t)+3*dirac(t)
x = 2+e**t*eps(t)
plt.plot(t,y)
plt.plot(t,dy)
plt.plot(x,dy)

setup_plot("Decompose with unit step")
```

Questions: 
1. What exacly is the definition of the Dirac-Impulse?
2. `Ex decomposition of the fucntion with unit step` problem at first case?
3. How would you draw the derivative?
