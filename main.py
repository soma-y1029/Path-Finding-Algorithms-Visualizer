import tkinter as tk
from tkinter import filedialog


class Node:
    def __init__(self, parent, position, g=0, h=0):
        self.parent = parent
        self.position = position

        self.g = g
        self.h = h
        self.f = g+h

    def __eq__(self, other):
        return self.position == other.position


NO_WALL = 'no_wall.txt'
DEF_MAZE = 'maze.txt'
DIRECTORY = '/'


class Maze:
    def __init__(self, root):
        self.maze_content = self.get_maze_content(NO_WALL) # load default maze
        self.root = root # store ro /*-+9ot into local

        # initialization
        self.starting_point = (0, 0)
        self.goal_point = (0, 0)
        self.width, self.height = 0, 0
        self.canvas = None  # maze canvas (will be created at maze_config())
        self.size = 50  # size of rectangle
        self.outline_color = '#999999'  # light gray
        self. time_interval = 0

        self.maze_frame = tk.Frame(root, padx=5, pady=5, bg='black') # frame to hold maze canvas
        self.maze_config()

    def pack_maze(self):
        self.maze_frame.pack()  # pack maze_frame
        self.canvas.pack()  # pack maze canvas

    def maze_config(self):
        self.width, self.height = len(self.maze_content[0])-1, len(self.maze_content)  # set width, height
        # create canvas that sit on maze_frame
        self.canvas = tk.Canvas(self.maze_frame, height=self.size * self.height, width=self.size * self.width)
        self.initialize_maze()

    def set_maze(self, maze_file):
        self.maze_content = self.get_maze_content(maze_file)
        self.reset_maze()

    def initialize_maze(self):
        for y, line in enumerate(self.maze_content):
            for x, letter in enumerate(line):
                color = 'white' # base color is white (empty space)
                if letter == 'W': color = 'Black'  # wall color
                elif letter == 'S':
                    color = 'Yellow'  # starting color
                    self.starting_point = (x, y)  # store starting point
                elif letter == 'G':
                    color = 'Green'  # goal color
                    self.goal_point = (x, y)
                # create rectangle for each element
                self.canvas.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,
                                             fill=color, outline=self.outline_color)

    def reset_maze(self):
        # destroy existing maze canvas
        self.canvas.destroy()
        self.maze_config()
        self.canvas.pack() # pack new canvas created in maze_config()

    def load_maze_from_computer(self):
        # user choose own maze file from computer
        maze_file = filedialog.askopenfilename(initialdir=DIRECTORY,
                                               title='Open File',
                                               filetypes=(('Text files','*.txt'), ('all files', '*.*')))

        # return maze_content
        return self.get_maze_content(maze_file)

    def get_maze_content(self, maze_file):
        # open given maze file and extract maze info
        try:
            with open(maze_file, 'r') as maze:
                maze_content = maze.readlines()
        except IOError:
            print(f'file does not exists.')
        return maze_content

    def open_new_maze(self):
        # set maze contnet
        self.maze_content = self.load_maze_from_computer()
        self.reset_maze()

    def change_color(self, point, color):
        x, y = point
        self.canvas.create_rectangle(x*self.size, y*self.size, (x+1)*self.size, (y+1)*self.size,
                                     fill=color, outline=self.outline_color)
        self.canvas.after(self.time_interval, self.canvas.update())

    def change_time_interval(self, time):
        self.time_interval = time

    def is_goal(self, point):
        return point == self.goal_point

    def is_wall(self, point):
        x, y = point
        return self.maze_content[y][x] == 'W'

    def neighbor(self, point):
        neighbor = []
        x, y = point

        # up
        if y != 0 and not self.is_wall((x, y-1)):
            neighbor.insert(0, (x, y-1))
        # right
        if x != self.width-1 and not self.is_wall((x+1, y)):
            neighbor.insert(0, (x+1, y))
        # down
        if y != self.height-1 and not self.is_wall((x, y+1)):
            neighbor.insert(0, (x, y+1))
        # left
        if x != 0 and not self.is_wall((x-1, y)):
            neighbor.insert(0, (x-1, y))
        return neighbor

    def path_found(self, solution):
        for index, point in enumerate(solution):
            # do not write arrow on goal point
            if self.is_goal(point):
                return
            x1, y1 = point
            x2, y2 = solution[index+1]
            self.canvas.create_line((x1 + 0.5) * self.size,
                                    (y1 + 0.5) * self.size,
                                    (x2 + 0.5) * self.size,
                                    (y2 + 0.5) * self.size,
                                    arrow=tk.LAST,
                                    width=3,
                                    fill="yellow")


class Menu:
    def __init__(self, root, maze):
        self.menu_frame = tk.Frame(root, padx=10, pady=10, bg='gray')
        self.time_slider_frame = tk.Frame(root, padx=5, pady=10, bg='gray')
        self.solution_frame = tk.Frame(root, padx=5, pady=10, bg='gray')

        self.maze = maze
        self.algs = ['Choose Algorithm', 'DFS', 'BFS', 'A*']
        self.files = ['Choose Maze', 'no_wall', 'maze']

        self.alg_option = tk.StringVar()
        self.alg_option.set(self.algs[0])

        self.file_option = tk.StringVar()
        self.file_option.set(self.files[0])

        self.alg_menu = tk.OptionMenu(self.menu_frame, self.alg_option, *self.algs)
        self.file_menu = tk.OptionMenu(self.menu_frame, self.file_option, *self.files, command=self.load_pre_set_maze)
        self.open_file = tk.Button(self.menu_frame, text='open maze file', command=self.maze.open_new_maze)
        self.start_button = tk.Button(self.menu_frame, text='Start', command=self.start)
        # self.pause_button = tk.Button(self.menu_frame, text='Pause', command=self.pause)
        self.reset_button = tk.Button(self.menu_frame, text='Reset', command=self.reset)
        self.time_slider = tk.Scale(self.time_slider_frame, from_=0, to=1000, length=200, label='Time Interval',
                                    orient=tk.HORIZONTAL, command=maze.change_time_interval)

    def place_buttons(self):
        self.time_slider_frame.pack()
        self.time_slider.pack()

        self.menu_frame.pack()
        self.alg_menu.grid(row=0, column=0, padx=10)
        self.file_menu.grid(row=0, column=1, padx=10)
        self.open_file.grid(row=2, column=1, padx=10, pady=10)
        self.start_button.grid(row=0, column=4, padx=30)
        # self.pause_button.grid(row=0, column=5, padx=100)
        self.reset_button.grid(row=0, column=5, padx=10)

        self.solution_frame.pack()

    def load_pre_set_maze(self, maze_file):
        if maze_file == self.files[1]:
            maze_file = NO_WALL
        elif maze_file == self.files[2]:
            maze_file = DEF_MAZE
        else:
            return
        self.maze.set_maze(maze_file)

    def start(self):
        selected_maze = self.file_option.get()
        selected_alg = self.alg_option.get()
        soln = []
        if selected_maze == 'no_wall':
            self.maze.set_maze(NO_WALL)
        elif selected_maze == 'Choose Maze':
            pass

        elif selected_maze == 'maze':
            self.maze.set_maze(DEF_MAZE)

        self.maze.initialize_maze()
        if selected_alg == 'DFS':
            alg = Algs('dfs', self.maze)
            soln = alg.run_alg()
            print(f'end of DFS {soln}')
        elif selected_alg == 'BFS':
            alg = Algs('bfs', self.maze)
            soln = alg.run_alg()
            print(f'end of BFS{soln}')
        elif selected_alg == 'A*':
            alg=Algs('astar', self.maze)
            soln = alg.run_alg()
            print(f'end of A*{soln}')

        self.maze.path_found(soln)
        # for node in soln:
        #     tk.Label(self.solution_frame, text=node).pack()

    def reset(self):
        self.maze.reset_maze()


class Algs:
    def __init__(self, alg, maze):
        self.maze = maze
        self.alg = alg

    def run_alg(self):
        if self.alg == 'dfs':
            return self.dfs()
        elif self.alg == 'bfs':
            return self.bfs()
        elif self.alg == 'astar':
            return self.astar()

    def change_color(self, point):
        if point != self.maze.starting_point:
            self.maze.change_color(point, 'cyan')

    def solution_path(self, starting_node, current_node):
        soln = []
        while current_node != starting_node:
            soln.append(current_node.position)
            current_node = current_node.parent
        return soln[::-1]

    def check_visited(self, current, visited, data_structure):
        if current.position not in visited:
            visited.add(current.position)
            self.change_color(current.position)

            for tup in self.maze.neighbor(current.position):
                data_structure.append(Node(parent=current, position=tup, g=current.g+1, h=self.get_heuristic(tup)))
        return data_structure

    def dfs(self):
        visited = set()
        root = Node(parent=None, position=self.maze.starting_point)
        fringe_stack = [root]
        while fringe_stack:
            current = fringe_stack.pop()
            if self.maze.is_goal(current.position):
                return self.solution_path(root, current)

            fringe_stack = self.check_visited(current, visited, fringe_stack)

    def bfs(self):
        visited = set()
        root = Node(parent=None, position=self.maze.starting_point)
        fringe_queue = [root]
        while fringe_queue:
            current = fringe_queue.pop(0)
            if self.maze.is_goal(current.position):
                return self.solution_path(root, current)

            fringe_queue = self.check_visited(current, visited, fringe_queue)

    def astar(self):
        visited = set()
        root = Node(parent=None, position=self.maze.starting_point, g=0, h=self.get_heuristic(self.maze.starting_point))
        priority_queue = [root]
        while priority_queue:
            current = priority_queue.pop(0)
            if self.maze.is_goal(current.position):
                return self.solution_path(root, current)

            priority_queue = self.check_visited(current, visited, priority_queue)
            priority_queue.sort(key=lambda node: node.f)

    def get_heuristic(self, current_point):
        current_x, current_y = current_point
        goal_x, goal_y = self.maze.goal_point

        return abs(current_x - goal_x) + abs(current_y - goal_y)


def main():
    root = tk.Tk()
    root.title('Maze')
    root.configure(bg='gray')
    maze = Maze(root)
    menu = Menu(root, maze)

    menu.place_buttons()
    maze.pack_maze()
    root.mainloop()


if __name__ == '__main__':
    main()


