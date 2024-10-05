Heuristics:
Desing by responsibility(behavior). No roles, No precedural(Data)

Classes:
C1. Attributes should be private
C2. Do not use non-public members of another class
C3. Keep the number of public methods in class minimal
C4. Implement a minimal set of methods(equals(),ToString(),hashCode()) in all classes
C5. A class should not depend on his users
C6. A class should capture exactly one abstraction  
C7. Keep related data and behavior together
C8. Methods should use most of the members in its class
C9. Model for behavior, not for roles
	- You can always just use variables:
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
R8. The view should be dependent on the model and not the other way around


Questions:
- Strategy pattern?
- If it is an Excepotion does it still violate the heuristic?
- How do I even fix the selected elements in the grid? In java you can get when the object is
clicked. When the pump is clicked it should tell the player somehow that it was clicked
(selected) . Is there a better way then global variables? I mean a better solution would have
been having these selected elements as static methods in the element class but is there a
way without having this 'type' of global variables?
- Can you give examples of violation of the boundaries?