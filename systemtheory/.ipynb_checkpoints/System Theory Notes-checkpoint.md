### Intro
Zoltan Horvath
V1 517
horvi@evt.bme.hu
szalay@hvt.bme.hu
www.kalotaapitvany.hu/romanika

book:
G.Fodor: Signals, Systems and Networks ISBN 936 05 7924 3

Signals:

> Mathematical description of the 'interesting part' of the physical process

- Deterministic s.   -> for this subject
	- Value at all time t is know (can be calculated)
	- repeatable

- Stochastic s.
	- not repeatable
	- similar seeming process(es) gives different results
	- stochastic features that can be detected

Deterministic <-> Stochastic  /oposites

| indep.var/dep.var. | CT  | DT  |                   |                                |
| ------------------ | --- | --- | ----------------- | ------------------------------ |
| Continouse value   |     |     | output is float   | <- this one we care about (PC) |
| discrete value     |     |     | output is integer |                                |

> CT signal  :=  $x=x(t), t\in \mathbb{R}$
> DT signal := $x=x[t], t\in \mathbb{R}$

Producing 
-  CTs :=$x(t)$ --sampling(regular)-> $x[k] = x(kT)$ T:=sample period
-  independently from CT S. ex. throwing cube. Ex:
	- k number of throwing
	- x[k] result of throwing
	- k=1,5 (cant be turn into CT's)


(ex):
	$e^{\alpha t}$ <-> $a^k$
	$A\cos(wt)$ <-> $A\cos(\theta k)$

unit step:
$$ \epsilon[k] =
\begin{cases} 
0, & k \in \mathbb{Z} \\
1, & k \in \mathbb{N}
\end{cases}$$

 unit impulse 
 $$\delta[k] = \begin{cases}
 0, k\in \mathbb{Z^-} \\
 1, k=0 \\
 0, k \in \mathbb{Z^+}
 \end{cases}$$
 operation:
  - shifting $x[k]=\delta[k-2]$
  - windowing
  - production with convolution
  - $$x[k]=\sum^\infty_{i=-\infty}=x[i]\delta[k-i]$$
  
  $$x[k]=\sum\delta[k-i]*2^k=1\delta[k]+2\delta[k-1]+4\delta[k-2]+...$$

1.  unit step with unit impulse
	$$\epsilon[k]=\delta[k]+\delta[k-1]+\delta[k-2]..=\sum_0^\infty\delta[k-i]$$
3. unit impulse with unit step
	$$\delta[k]=\epsilon[k]-\epsilon[k-1]$$


CT signals
ex: $e^{\alpha t}$,  $A\cos(wt)$,

untit step: $\epsilon(t)=0, t \in R^-, 1 \in R^+$  e(0)=1 sometimes
Dirac - impulse $$ \delta(t,\tau) = \frac{\epsilon(t) - \epsilon(t-\tau)}{\tau} , 0<t<\tau$$

$$\int \delta[t]=1$$

Operations:
 - shifting  $\epsilon(t-2)$
 - windowing:  g(t)*2e(t+2) = p(t) you just cut  a window out


>  The generalized deravitie:= x'(t) from which x(t) can be constructed

$$x(t)=\int_{t_0}^t x'(\tau)d\tau + x(t_0)$$$$\epsilon(t)= \int_{\infty}^t\delta(\tau)d\tau$$ => $$ \delta(t)=\epsilon(t)$$

$\epsilon(t)x(t)$ -> x'(t)=(x(t)e(t))' = x'(t)e(t)+x(+0)\delta[t]

x(t) = (2+e^-4t)e(x)
x'(t)=-4e^-4te(t) + 3*d(t)