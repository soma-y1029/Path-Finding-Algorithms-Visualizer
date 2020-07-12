# Path-Finding-Algorithms-Visualizer
Path Finding Algorithms Visualizer with TkInter
Currently, DFS, BFS, A* are supported.


## Preparation
main.py contains all classes needed to run this program.

As default, there are two maze file. Please download two maze text file into same directory. 

## Buttons
* Option Menu "Choose Algorithm":
Choose any algorithm you like. Current options are DFS, BFS, A*. (more are coming!)

* Option Menu "Choose Maze": 
Choose any maze you like. If two default maze file are downloaded, you are able to choose from two file, no_wall or maze. 

* Button "open maze file"
Open maze file from computer. 
You can create your own .txt file and load the maze into the program.
Below are representation in case of you create your own maze.
'-' represents empty space.<br>
'W' represents walls.<br>
'S' represents starting point.<br>
'G' represents goal point. <br>

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
Stack is used for DFS data structure.
Keep looking for same direction while the direction is available. 
If there is no path for current state, back up and look for different path using backtracking.
![](https://i.imgur.com/7tjfBEZ.gif)


### BFS
Queue is used for BFS data structure.
Look for the neighbors in circular motion until algorithm find goal state. 
![](https://i.imgur.com/4yVrX0f.gif)


### A*
Priority queue is used for A* data structure.
This PQ is based on a sum of greedy function that represents cost from start to current and heuristic fuction that represents cost from current and goal state.
![](https://i.imgur.com/8zpCMAa.gif)
