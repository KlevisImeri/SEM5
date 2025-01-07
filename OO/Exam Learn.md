#### Concurrency
surrogate
Interlocked		System.Threading
AtomicReference		java.util.concurrent.atomic 
Balking

Double-checked locking, partially constructed object

ThreadLocal<T>
Asynchronous completion token (ACT)
Cancellation token
Task C# Future Java

System.Threading.Tasks
java.util.concurrent.ExecutorService

C#: System.Threading.ReaderWriterLockSlim
java.util.concurrent.locks.ReentrantReadWriteLock

C#: common base class for signals is System.Threading.WaitHandle Java: no common base class for signals

NET: ▪ read-only view: System.Threading.Tasks.Task<T> class ▪ manipulation: System.Threading.Tasks.TaskCompletionSource<T> class ▪ C# also has built-in language constructs for tasks: async/await ▪ Java: ▪ almost read-only (allows cancellation): java.util.concurrent.Future<T> interface ▪ manipulation: java.util.concurrent.FutureTask<T> implementation of Future<T> ▪ unfortunately no clear separation of concerns

#### Desing Patters
Adapter provides a completely different interface
Proxy keeps the interface
Decorator keeps or enhances the interface
flyweight intrinsic state of cached objects is immutable

Adapter usually wraps just one object, while Facade works with an
entire subsystem of objects

Bridge is similar to Adapter, but Bridge separates interface from
implementation, while Adapter is meant to change the interface of an
existing class

Facade defines a new interface for multiple existing objects, while
Adapter tries to make the existing interface of a single object usable

Mediator vs facade:
![[Pasted image 20250104231235.png]]

Facade is similar to Adapter, but defines a new interface, does
not reuse an existing one)

TemplateMethod() is public and sealed (final)

external iterator
internal iterator
robust iterator:

Handlers as Commands: execute different operations (Handlers)
over the same context (Request)
Requests as Commands: execute the same operation (Request)
in different contexts (Handlers)

CoR vs Decorator

State := dynamically chaning the class

![](../Images/Pasted%20image%2020250105205345.png)


Template Method is based on inheritance, Strategy is based on
composition

Command and Strategy look similar, but in Command different
operations can be converted to different Commands, while Strategy
describes different algorithms doing the same operation

Composite: Uniform, Safe


#### API
Planning for extensibility requires going through realistic
scenarios
▪ for each class that can be overridden write at least 3 different
subclasses (as examples or as public classes of the API) to ensure
that it is powerful enough to support a wide range of
requirements

Service Provider Interface (SPI)

Name boolean options so that they are default to false
▪ e.g. visible vs. hidden
 Conservative policy: all concrete classes final/sealed/
 
G15. Strive for property-based APIs for GUI
▪ Don’t make users to initialize everything in constructors
with long parameter list
▪ only the required settings should be constructor parameters

The API should be able to used in 3 lines:

conversely, don’t fail silently
methods should be failure-atomic

Checked exceptions violate OCP
Avoid leaking null-pointer exceptions (use more meneangfull exceptions)

method: contract between method and its client
▪ pre-conditions, post-conditions, side-effects

![](../Images/Pasted%20image%2020250106001219.png)

Which of the following guidelines are common in the API
design principles and in the Clean code principles?
A. Use the local dialect
B. Avoid long parameter lists
C. Design and document for inheritance or else prohibit it
D. Document the API
E. Use convenience methods
F. Favor unchecked exceptions
G. Avoid abbreviations
H. Avoid side-effects

#### Clean Code
O 0
L 1

Don’t use names which vary in small ways
Don’t use noise words like ‘a’, ‘the’, ‘variable’,
‘info’, etc.
▪ theMessage vs. Message
▪ NameString vs. Name
▪ AccountData vs. Account
▪ CustomerObject vs. Customer
Use names that can be pronounced

Blocks within if statements, else statements, while
statements, try-catch statements, and so on should be
one line long
▪ probably that line should be a function call


Journal comments
Attributions and bylines
Commented-out code
Closing brace comments
Banner comments
HTML comments
**Nonlocal Information**
Inobvious connection

▪ Functions should do one thing
▪ error handing is one thing
▪ thus, a function that handles errors should do nothing else
▪ extract the bodies of the try and catch blocks out into functions
of their own

![](../Images/Pasted%20image%2020250106203938.png)

 If something is wrong, throw an exception DONT RETRUN NULL
 
However, if the links in the chain are data structures, LoD
does not apply

![](../Images/Pasted%20image%2020250106205135.png)

Problems of refactoring:
Databases
Interfaces

### Refactoring
Divergent change := the idea is that you start with the class and whilde developing you add more changes to the class witch are divergent (like it takes care of diff UI technologies or diff Driver) => you create a stable class interface and the concreate classes => aka seperate the class into specific thing.

Swith statement aslo incldue null-checking

Caution:
▪ parallel hierarchies may be a deliberate design decision
(e.g. simulating multiple inheritance)


F16. Introduce foreign method
▪ put a new method in the client with the server as parameter
F17. Introduce local extension
▪ create a new subclass of the server with the new methods

F46. Parameterize method
▪ combine similar methods into one method with additional parameters

Consolidate conditional expression

F36. Consolidate duplicate conditional fragments

> Consolidate := combine to one

Replace nested conditional with guard clauses

![](../Images/Pasted%20image%2020250107002822.png)


### Heuristics
C8. Methods should use most of the members in its class

I8. Use protected only for methods and never for attributes


Statis semantics and constrains are that if you know that somthing will have that property from the beggening of tis creaton till the end its called static.

LSP violation -> OCP violation

Release Reuse Equivalency Principle (REP) := versioning

SAP := Stable packages should be abstract packages

SCP := Single choice principle

Common Closure Principle (CCP) vs Common Reuse Principle (CRP)
(changed together)                (Used together)


Signs: is[OfType](), can[DoSomething](), etc.