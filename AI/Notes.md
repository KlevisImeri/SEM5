- Reflex Agent
- Planning Agent 

Search 
- State space (vertices)
- Successor function (edges)
- Start - Goal
- Solution the path

World state vs State space

State space graph vs Search Tree

DFS - stack

Complete - 
Optimal - 

A* stop when deque goal

admissable 

H1 dominates H2

CPS
- Variables
- Domains
- Constrain
- Solution assigment satisfiing

CSP forward checking 
- Each vertex has a color. When you assign a color all the neighboors loos that color.
- here we dealt with contrains 

X -> Y  for all x each color they should exits an assigmetn of color to the y that works
You try to keep the arc consistens by remocving colors. If you cant you 
Forward checking
![](../Images/Pasted%20image%2020241121221314.png)

Full arch consistency is full filtering

Even if you force arch contistincey you will still backtrack
![](../Images/Pasted%20image%2020241121222010.png)


Filtering:
- Arc consitency
	- Full
	- Or just forward checking

Ordering:
 - Minimun remaining value : which has less (Variable)
 - Lest Constraning Value (the one that rulest out the fewest amout of values) (Values)
 - You can use both of them


The whole idea is how to make the bactracking better

Many possible formalizations, one is:
▪ States: S (start at s0)
▪ Players: P={1...N} (usually take turns)
▪ Actions: A (may depend on player / state)
▪ Transition Function: SxA → S
▪ Terminal Test: S → {t,f}
▪ Terminal Utilities: SxP → R

![](../Images/Pasted%20image%2020241121230425.png)

![](../Images/Pasted%20image%2020241121230432.png)

alpha - Max value in the path
beta - Min value in the path


Model -> the states when the sentance is true
	![](../Images/Pasted%20image%2020241121231819.png)