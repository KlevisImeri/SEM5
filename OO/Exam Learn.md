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