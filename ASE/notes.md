artifacts
T2T transfomations -> LLM'S 
Back-annotation 
CDelivery vs CDeployment
just-in-time validation
___
Task - single transformation
Lifecycle tasks - 
Pipeline view
build vs assemble (no verification)
**lockfiles**
Shared runners: 
Provisioned runners:
Self-hosted runnersp
Build matrix: execute on different platforms by leveraging multiple runners
Development 
Staging 
Production 
Deploy keys
_____
Model driven development
Abstract syntax is the (abstract) data structure of a model, which ***excludes representation-specific*** details.
1 abstract syntax → many textual and visual notations
1 abstract model → many concrete forms in 1 syntax!
1 semantic interpretation → many abstract models
G + lables
Supertypes and subtypes
Direct type
Indirect type
Abstract type
Generalization 
Containment
Aggregation (circular)
___
**sentential form**. A sentential form is a string made up of terminals and nonterminals. It represents a partially derived sequence in the language.
![](../Images/Pasted%20image%2020241217220734.png)
![](../Images/Pasted%20image%2020241217224911.png)
Qualified references (ex: this.a) add context to remove ambiguity
___
Dedicated
- Specific, ad-hoc 
- Using a dedicated code generator 
Template-based 
Serializer-based
___
**Multipass**: The generation process can be done in multiple stages, with each pass refining the output.
Generation gap
What are the problems that can be with the code generation?
___
**Beam search**: keep track of several paths
perplexity
System prompt:
User prompt
distillation (Fine-tuning)
Retrieval-Augmented Generation
Vector search
Neuro-Symbolic Reasoning
___
![](../Images/Pasted%20image%2020241218023552.png) 
Arrival rate = Throughput -> Stable state
Stable
utilization
thrashing
Micro-Benchmark
Macro-Benchmark : indetify bootlenecks, check the performance in increasing problem size
JHM - Library to execute precise Microbenchmarks
SampleTime 
SingleShotTime
class loading && code optimizaition -> warmup
blackhole object
Sampling
Profiling
![](../Images/Pasted%20image%2020241218030522.png)
___
Exploratory Data Analysis (EDA)
Confirmatory Data Analysis
Robust statistics 
Nonparametric statistics – no a priori assumptions
Ordinal - total ordering
Nominal
Percentile
Quartile
IQR=Q3−Q1
Q1−1.5×IQR
Q3+1.5×IQR Whiskers
![](../Images/Pasted%20image%2020241218142600.png)

SonarQube 
SonarLint
Fault hypothesis
Mutans: 𝑀 = {𝑜𝑝1(𝑆), 𝑜𝑝2(𝑆), … , 𝑜𝑝𝑛(𝑆)}
lazy evaluation
condition decisiont vs condition/decision
MC/DC
![](../Images/Pasted%20image%2020241218172659.png)
___
test case = input + test oracle
mplicit errors
assertions
Regression testing
Randoop
Robustness Testing (Fuzz Testing)
Mutation-based fuzzing
Grammar-based fuzzing
Path Feasibility
![](../Images/Pasted%20image%2020241218181607.png)Dynamic Symbolic Execution (DSE
assume assert
```java
public {{ name }}Workflow({% for param in parameters %}{{ param.type }} {{ param.name }}{% if not loop.last %}, {% endif %}{% endfor %}) {
    {%- for param in parameters %}
    this.{{ param.name }} = {{ param.name }};
    {%- endfor %}
}
```
___
![](../Images/Pasted%20image%2020241219010736.png)
___
Pattern-based
Model checking
Theorem proving
Static-Single- Assignment Form 
![](../Images/Pasted%20image%2020241219020020.png)
___
Atomic bundling
**Fault tolerance**