Heuristics:
Desing by responsibility(behavior). No roles, No precedural(Data)

Classes:
C1. Attributes should be private
	- DRY
C2. Do not use non-public members of another class
	- package/internal/friend 
C3. Keep the number of public methods in class minimal
	- ISP
C4. Implement a minimal set of methods
	- equals(),ToString(),hashCode()
	- `operator==, operator=, operator<<`
C5. A class should not depend on his users
	- OCP and LSP
	- ADP
	- resolve using DIP
C6. A class should capture exactly one abstraction  
	- Visitor, Strategy
C7. Keep related data and behavior together
	- TDA DRY
	- Eceptions: ORM and DTO
C8. Methods should use most of the members in its class
	- Exceptions: ORM and DTO classes, utility classes are OK
C9. Model for behavior, not for roles
	- You can always just use variables:
	- Exceptions: empty leaves are allowed if behavior is separated from the class, e.g. visitor design pattern
```java
Person Mother = new Person();
Person Father = new Person();
```

Responsibility:
R1. Distribute responsibility horizontally evenly
	- Horizontally means in the same layer of abstraction
R2. Avoid god classes
R3. Avoid classes with only accessor methods
R4. Avoid classes which should be methods
R5. Model the real world
R6. Model at the appropriate abstraction level
R7. Model only within the domain boundaries of the system
	- do not model physical devices outside the system
	- do not model users and external systems, only provide an
interface for them
R8. The view should be dependent on the model and not the other way around

A1. Minimize the number of collaborating classes
	- ISP and DIP to decrease dependency
A2. Minimize the number of different method calls between collaborating classes
	- DRY  ISP 
A3. Distribute responsibilities in containment relationships
A4. Prefer containment over association
A5. A container object should use the contained objects
A6. A contained object should not use its container object
A7. Contained objects should not communicate with each other directly


I1. Inheritance should always be behavior specialization
I2. Prefer containment over inheritance
I3. Shared data without shared behavior should be in a containment relationship
I4. Shared data with shared behavior should be in a common superclass
I5. Move common data and behavior as high as possible in the inheritance hierarchy
I6. A common interface should only be inherited if the behavior is also shared
I7. A class should not depend on its descendants
I8. Use protected only for methods and never for attributes
I9. The inheritance hierarchy should be deep, but at most seven levels deep
I10. Abstract classes should be at the root of the inheritance hierarchy
I11. Roots of the inheritance hierarchy should be interfaces or abstract classes
I12. Never test for the type of an object, use polymorphism instead
I13. Never encode behavior with enum or int values, use polymorphism instead
I14. Don’t create type or capability discriminator methods
I15. Do not confuse objects with descendants, beware of single instance descendants


7 layers 7 classes

Questions:
- Strategy pattern?
- If it is an Excepotion does it still violate the heuristic?
- How do I even fix the selected elements in the grid? In java you can get when the object is
clicked. When the pump is clicked it should tell the player somehow that it was clicked
(selected) . Is there a better way then global variables? I mean a better solution would have
been having these selected elements as static methods in the element class but is there a
way without having this 'type' of global variables?
- Can you give examples of violation of the boundaries?