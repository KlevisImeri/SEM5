| Name: Klevis | Neptun: T4XGKO |
| ---- | ------------- |


# Homework 5

The goal of this homework is to practice the clean code principles. Find your work you have created in the Software project laboratory subject, and look into the final source code that also contains the graphical user interface!

Find 5 examples where one of the clean code principles gets violated! Modify the code so that the clean code principle becomes satisfied! Copy the original and the modified code here!

---
1
**Original code snippet:**
```java
  public void setImageLocation(Point l) {
    imageLocation = l;
  }
```

**Violated clean code principle**: Avoid disinformation
Don’t use ‘O’ and ‘l’ as names, they can be easily confused with 0 and 1

**Modified code snippet:**
```java
  public void setImageLocation(Point location) {
    imageLocation = location;
  }
```


---
2
**Original code snippet:**
```java
      int xPosition = 0;
      for (var pump : cistern.newPumps) {
        PumpView pumpView = new PumpView(pump, gridView);
        pumpView.setLocation(xPosition, 0); 
        pumpViews.add(pumpView);
        add(pumpView, gbc);
        xPosition += 40; 
      }
```

**Violated clean code principle**: Use intention-revealing names
Burned in values with no meaning.

**Modified code snippet:**
```java
  ...
  static final int PUMP_SPACING = 40;
  static final int PUMP_HEIGHT = 0;
  ...
  
      int xPosition = 0;
      for (var pump : cistern.newPumps) {
        PumpView pumpView = new PumpView(pump, gridView);
        pumpView.setLocation(xPosition, PUMP_HEIGHT); 
        pumpViews.add(pumpView);
        add(pumpView, gbc);
        xPosition += PUMP_SPACING; 
      }
      
```

---
3
**Original code snippet:**
```java
  public Pipe insertPump() throws Exception {
    try {
      if (carryPump != null) {
        if (location instanceof Pipe) {
          Output.println("[INSERTING PIPE]", Color.RED);
          String before = toString();
  
          Pipe newPipe = new Pipe(grid);
          List<Element> neighbors = location.getNeighbors();
          location.removeNeighbor(neighbors.get(1));

          carryPump.setInPipe(newPipe);
          carryPump.setOutPipe((Pipe) location);

          // carryPump.addPlayer(this);
          if(neighbors.get(1) instanceof Pump){
            ((Pump)neighbors.get(1)).setOutPipe(newPipe);
          } else {
            neighbors.get(1).addNeighbor(newPipe);
          }

          // here in som cases also the in pipe should be updated

  
          grid.addPipe(newPipe);
          grid.addPump(carryPump);
          carryPump = null;

  
          Output.printChange(before, toString());
          System.out.println(grid);
          return newPipe;
        } else {
          throw new Exception("[You can't insert a Pump at a " + location.type() + "]");
        }
      } else {
        throw new Exception("[You don't have a Pump!]");
      }
    } catch (Exception e) {
      Output.println(e.getMessage(), Color.LIGHT_RED);
      throw e;
    }
  }
```

**Violated clean code principle**: Functions should be small
The function here is to large

**Modified code snippet:**
```java
public Pipe insertPump() throws Exception {
    try {
        validatePumpAndLocation();
        
        String before = toString();
        Pipe newPipe = createNewPipe();
        
        setupNewPipeConnections(newPipe);
        
        finalizeInsertion(newPipe);
        
        Output.printChange(before, toString());
        System.out.println(grid);
        
        return newPipe;
    } catch (Exception e) {
        handleError(e);
        throw e;
    }
}

private void validatePumpAndLocation() throws Exception {
    if (carryPump == null) throw new Exception("[You don't have a Pump!]");
    if (!(location instanceof Pipe)) 
        throw new Exception("[You can't insert a Pump at a " + location.type() + "]");
}

private Pipe createNewPipe() {
    Pipe newPipe = new Pipe(grid);
    carryPump.setInPipe(newPipe);
    carryPump.setOutPipe((Pipe) location);
    return newPipe;
}

private void setupNewPipeConnections(Pipe newPipe) {
    List<Element> neighbors = location.getNeighbors();
    location.removeNeighbor(neighbors.get(1));

    if (neighbors.get(1) instanceof Pump) {
        ((Pump) neighbors.get(1)).setOutPipe(newPipe);
    } else {
        neighbors.get(1).addNeighbor(newPipe);
    }
}

private void finalizeInsertion(Pipe newPipe) {
    grid.addPipe(newPipe);
    grid.addPump(carryPump);
    carryPump = null;
}

private void handleError(Exception e) {
    Output.println(e.getMessage(), Color.LIGHT_RED);
}

```

---
4
**Original code snippet:**
```java
  /*---------------------------------------------main Loop------------------------------------------- */

  /**
   * Executes the main game loop, repeatedly allowing each player to take active and passive actions
   * until the game ends, as determined by user input.
   */

  ...

  /*---------------------------------------------main Loop------------------------------------------- */

  

  /*---------------------------------------------end Game------------------------------------------- */

  /**
   * Concludes the game, displaying the final results including the amounts of water gathered by
   * Plumbers and leaked by Saboteurs.
   */

  public void endGame() {
    Output.println("\n[Game Ended]", Color.LIGHT_BLUE);
    displayResults(grid.getWaterAtCistern(), grid.getWaterAtDesert());
  }


  /**
   * Displays the results of the game, showing how much water was gathered and leaked.
   *
   * @param plumberResult The amount of water gathered by Plumbers.
   * @param saboteurResult The amount of water leaked by Saboteurs.
   */

  public void displayResults(int plumberResult, int saboteurResult) {
    Output.println("The plumber gathered: " + plumberResult + "liters of water",
        Color.LIGHT_MAGENTA);
    Output.println("The saboteurs leaked: " + saboteurResult + "liters of water",
        Color.LIGHT_MAGENTA);
    grid.stopTimers();
  }

  /*---------------------------------------------end Game------------------------------------------- */
```

**Violated clean code principle**: Bad comments: Redundant comments and Section comments 

**Modified code snippet:**
```java
  public void endGame() {
    Output.println("\n[Game Ended]", Color.LIGHT_BLUE);
    displayResults(grid.getWaterAtCistern(), grid.getWaterAtDesert());
  }

  public void displayResults(int plumberResult, int saboteurResult) {
    Output.println("The plumber gathered: " + plumberResult + "liters of water",
        Color.LIGHT_MAGENTA);
    Output.println("The saboteurs leaked: " + saboteurResult + "liters of water",
        Color.LIGHT_MAGENTA);
    grid.stopTimers();
  }

```

---
5
**Original code snippet:**
```java
/**
 * The Main class serves as the entry point for the game, orchestrating the setup, execution, and
 * termination of the game. It manages player selection, game loop, and displaying results.
 */
public class Game {
  PlayersCollection players = new PlayersCollection();
  Grid grid = new Grid();
  Menu menu = new Menu();
  Timer timer = new Timer();
  ....
```

**Violated clean code principle**: Misleading comments.
The class was edited but the comment was not.

**Modified code snippet:**
```java
public class Game {
  PlayersCollection players = new PlayersCollection();
  Grid grid = new Grid();
  Menu menu = new Menu();
  Timer timer = new Timer();
```
