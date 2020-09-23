# Path-Finding-Algorithms-Visualizer
Path Finding Algorithms Visualizer with TkInter<br>
Currently, DFS, BFS, A* are supported.

[Java version is also available.](https://github.com/soma-y1029/Path-Finding-Algorithms-Visualizer-in-Java)

## Performance Observation
Each algorithms' details are below.<br>
<br>
Time for each algorithms are: (including animation time)<br>
In No-Wall maze (two points only), <br>
DFS: 1.996s<br>
BFS: 2.137s<br>
A* : 0.163s<br>
<br>
In Maze:<br>
DFS: 1.907s<br>
BFS: 4.070s<br>
A* : 3.937s<br>
<br>
Observed that informed path finding algorithm fish faster than uninformed search. <br>
Heuristic function have very large commitment to decrease time. <br>
<br>
## Preparation
main.py contains all classes needed to run this program.

As default, there are three maze file. Please download the maze text files into same directory. 

## Buttons
* Option Menu "Choose Algorithm":
Choose any algorithm you like. Current options are DFS, BFS, A*.

* Option Menu "Choose Maze": 
Choose any maze you like. If default maze files are downloaded, you are able to choose from file, no_wall, maze, or multi_point.

* Button "open maze file"
Open maze file from computer. 
You can create your own .txt file and load the maze into the program.
Below are representation in case of you create your own maze.
'-' represents empty space.<br>
'W' represents walls.<br>
'S' represents starting point.<br>
'G' represents goal point. <br>
numbers can be used as goal point instead. In that case, use only numbers. The algorithm retrive the numbered-goal point in order of number.<br>

* Button "Start":
Start program based on chosen algorithm and maze. 

* Button "Reset":
Reset maze board.

* Slider "Time Interval":
Time interval from 0 to 1000 ms (1 sec).
You can change the speed while program is running.

## Algorithm Explanation
For all algorithms, order of neighbor searching is clockwise (top, right, bottom, left).

### DFS
Stack is used for DFS algorithm.
Keep looking for same direction while the direction is available. 
If there is no path for current state, back up and look for different path using backtracking.


![](https://i.imgur.com/AkuPY9J.gif)


### BFS
Queue is used for BFS algorithm.
Look for the neighbors in circular motion until algorithm find goal state. 


![](https://i.imgur.com/8h6swAa.gif)


### A*
Priority queue is used for A* algorithm.
This PQ is based on a sum of greedy function that represents cost from start to current and heuristic fuction that represents cost from current and goal state.


![](https://i.imgur.com/Vyn923Y.gif)

Multipoint destination with A*.

![](https://i.imgur.com/JcZ0gl7.gif)


