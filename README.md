# Mario-Game
# Instructions to run the game
1. Extract the contents of 20171077_Assign1.tar.gz and change directory to 20171077_Assign1.
2. Run the game by typing the command: python3 game.py

# Unique Features of my game:
1. Code exhibits Object Oriented Concepts
   - Inheritance : My code takes advantage of inheritance in many places. As an example there is one Person class. Enemy, Boss and Mario which are the classes for enemies, Boss Enemy and Mario respectively inherit from this Person class. The Person class has functions which take care about movement of the character and gravity. We know such features are common to both enemies and Mario. As a result reuseability of code increases, one of the prime objectives of OO Concept Inheritance.
   
   - Polymorphism - My code exhibits polymorphism by implementing function overriding in Boss class. The Boss class inherits from Person class but it has another update() which overrides the update() in Person class.
   
   - Encapsulation - The code strictly adheres to the concept of objects and it's data being tied together in an entity called the capsule. This is demonstrated by extensive use of instance variables which are nothing but variables that are tied together with the corresponding object.
   
   - Abstraction - Use of intuitive names like update(), move(), draw_mario() etc. treats these functions as blackboxes and hides the underlying details which makes the code more readable and less tedious.
   
2. One of the unique features is the way I engineered the sound by cutting sound clips from original game to make the jump sound, coin collecting sound, background music and even level completion music as realistic and entertaining as possible.

3. The way I am displaying to the terminal and have decied my frame rate, results in very less screen tearing and ensures the game runs very smoothly.

4. Mario can break the bricks and climb on them as well. Collecting coins gives bonus points to the player.

5. Two levels implemented with different backgorunds. Level 2 is an underground level with double layer bricks that can be broken by climbing one layer. Level 2 is substantially harder with the boss enemy firing at Mario and at the same time gap between two walls(having water) being slightly bigger.

6. Randomly generated map. Randomly generated enemies. But makes sure that obstacles/enemies are generated without any glitch. For example care is taken so that pipes are not generated on water. Similarly two enemies are not generated at the same place or where a pipe exists.

7. Smart boss enemy. Has a pseudo random motion and throws fireballs at Mario. After Mario surpasses it, the Boss enemy starts chasing Mario till the pole and by throwing fire balls at an exponentially faster rate. All these speeds have been thoroughly experimented and tested to give a very enthralling gameplay.
