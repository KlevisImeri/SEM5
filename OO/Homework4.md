| Name: Klevis | Neptun: T4XGKO |
| ---- | ------------- |


# Homework 4

The goal of this homework is to practice the code smells and refactoring patterns. Find your work you have created in the Software project laboratory subject, and look into the final source code that also contains the graphical user interface!

---
1
**Original code snippet:**
```java
  public void changePumpDirection() throws Exception {
    if (location instanceof Pump) {
      ((Pump) location).changeDirection();
    } else if (location instanceof Pipe) {
      throw new Exception("You can't change the direction Pipe!");
    } else if (location instanceof Cistern) {
      throw new Exception("You can't change the direction of cistern!");
    } else if (location instanceof Spring) {
      throw new Exception("You can't change the direction of spring!");
    }
  }
```
**Code smell:** Switch statements | Downcasting 
Another problem here is that exceptions are actually used as logging and not as 'real' exceptions. If the player can't perform the operation when the game should just tell the player what he can't do and nothing should happen. The idea of the exceptions was that the view uses the model and the view can just catch the exceptions and log them graphically. But I think having a singleton logger seams nicer like log4j.
**Refactored code snippet:**
```java

public abstract class Element extends Model {
	...
	abstract public void changePumpDirection();	
	...
}
public class Cistern extends ActiveElement {
	...
	@Override
	public void changePumpDirection() {
		    Output.println("[You can't fix a Cistern!]", Color.LIGHT_RED);
	}
	...
}
public class Spring extends ActiveElement {
	...
	@Override
	public void changePumpDirection() {
		    Output.println("[You can't fix a Spring!]", Color.LIGHT_RED);
	}
	...
}
public class Pipe extends ActiveElement {
	...
	@Override
	public void changePumpDirection() {
		    Output.println("[You can't fix a Pipe!]", Color.LIGHT_RED);
	}
	...
}

//Our method
public void changePumpDirection() {
	location.changeDirection();
}
```


---
2
**Original code snippet:**
```java
  public void fix() { 
    if (location instanceof Pump) {
      ((Pump) location).fix();
    } else if (location instanceof Pipe) {
      ((Pipe) location).fix();
    } else if (location instanceof Cistern) {
      Output.println("[You can't fix a cistern!]", Color.LIGHT_RED);
    } else if (location instanceof Spring) {
      Output.println("[You can't fix a spring!]", Color.LIGHT_RED);
    }
  }
```
**Code smell:** Switch statements | Downcasting 
**Refactored code snippet:**
There are two ways to solve this: 
1. Assuming you don't want to log (You can use Acyclic Visitor but I will use a striped down version of it)
```java
//Somewhere in the package
public interface Fixable { 
	void fix(); 
}

//Our method
 public void fix() { 
	if (location instanceof Fixable) {
		((Fixable) location).fix();
	}
}
```
This doesn't break OCP or the LSP

2. Assuming you want to log (The normal polymorphism inheritance)
```java
public abstract class Element extends Model {
	...
	abstract public void fix();	
	...
}
public class Cistern extends ActiveElement {
	...
	@Override
	public void fix() {
		    Output.println("[You can't fix a cistern!]", Color.LIGHT_RED);
	}
	...
}
public class Spring extends ActiveElement {
	...
	@Override
	public void fix() {
		    Output.println("[You can't fix a spring!]", Color.LIGHT_RED);
	}
	...
}

//Our method
public void fix() { 
	location.fix();
}
```





---
3
**Original code snippet:**
```java
  /**
   * Paints the GridView, including all its elements.
   * Updates the locations of the spring, cistern, and pumps.
   *
   * @param g the Graphics object to protect
   */
  @Override
  public void paint(Graphics g) {
    super.paint(g);
    // Update the locations of the spring and cistern based on the current size of the view.
    Dimension size = getSize();
    
    springView.setLocation(
      0,
      size.height / 2 - springView.getHeight() / 2
    );

    cisternView.setLocation(
      size.width - cisternView.getWidth(),
      size.height / 2 - cisternView.getHeight() / 2
    );

    // Ensure the pumps maintain their set locations.
    for(var pumpView : pumpViews){
      pumpView.setLocation(pumpView.getLocation());
    }


    // Adjust the image size to match the current size of the view.
    this.setImageSize(getSize());
    // for(var pumpView : pumpViews){
    //   pumpView.setLocation(
    //     getWidth()/3 - pumpView.getWidth()/2,
    //     getHeight()/3 - pumpView.getHeight()/2
    //   );
    // }
  }
```
**Code smell:** Comments
We have both unnecessary comments and commented-out code; the code is self-explanatory enough on its own.
**Refactored code snippet:**
```java
  @Override
  public void paint(Graphics g) {
    super.paint(g);
    
    Dimension size = getSize();
    
    springView.setLocation(
      0,
      size.height / 2 - springView.getHeight() / 2
    );

    cisternView.setLocation(
      size.width - cisternView.getWidth(),
      size.height / 2 - cisternView.getHeight() / 2
    );

    for(var pumpView : pumpViews){
      pumpView.setLocation(pumpView.getLocation());
    }

    this.setImageSize(getSize());
  }
```


> [!note]
> I tried to find other parts to refactor but even those are to big (level design change) which would take to much places to refactor or there are actually no parts to refactor because I think our code was extremely clean and nice and well thought. Now that I look back it's really nice to work with.