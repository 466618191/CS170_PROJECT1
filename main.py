
from asyncio import QueueEmpty
import copy
import sys
# Global Variables keep check status of queue
goal = ([1, 2, 3], [4, 5, 6], [7, 8, 0])
nodes_counter = 0
max = 0
queue = []  # nodes
q_size = 0
checker = True
seen = []


# 'node'


class node:
    def __init__(self, a):
        self.puzzle = a  # create the node
        self.fval = 0  # f(n)
        self.gval = 0  # g(n)
        self.hval = 0  # h(n)


def expand(queue, QUEUEING_FUNCTION):
    # mention global
    global nodes_counter  # nodes expanded
    global max  # max numbers in queue
    global q_size  # temp queue size will be check for max later
    global seen  # the node we already expanded
    global alltest  # test all 3 modes
    child_container = []

    # https://stackoverflow.com/questions/67209910/how-to-return-the-index-of-an-element-in-a-2d-array-in-python
    # Coordinates of 0 and store the current 0's location
    for i, j in enumerate(queue[0].puzzle):

        if 0 in j:
            index = (i, j.index(0))
            c = j.index(0)
            r = i
            break

# up right left down
# move to left
    if c > 0:
        # Whether to allow storage into queue
        allow = 1
        # temp Variables are used to pass values. and make position change and then store to child node
        temp1 = copy.deepcopy(queue[0].puzzle)
        temp = queue[0].puzzle[r][c-1]  # left
        temp1[r][c-1] = 0  # change position store to temp var
        temp1[r][c] = temp  # pass element
        # queue length for check Whether this node has been previously expanded
        length = len(seen)
        # print(temp1)
        if temp1 == goal:  # goal checker
            print("-------------------")
            print(temp1[0])
            print(temp1[1])
            print(temp1[2])
            print("-------------------")
            print("===============find goal!!!!================")
            #print("with f(n): "+str(queue[0].gval+1+queue[0].hval))
            print("Depth: " + str(queue[0].gval+1))
            print("Number of nodes: " + str(nodes_counter))
            print("Max queue size: "+str(max))
            sys.exit()
        i = 0
        while i < length:  # See if this node has been expanded

            if seen[i].puzzle == temp1:

                i = length+1
                allow = 0  # if true we don't allow append to queue

            i = i+1

        if allow == 1:

            child = copy.deepcopy(node(temp1))  # expanded node's child
            child.gval = queue[0].gval+1

            # children container to store the node we expanded after check up down right left return it and store to queue
            child_container.append(copy.deepcopy(child))
            # queue.append(copy.deepcopy(child))

            # this node we already seen
            seen.append(copy.deepcopy(child))

            nodes_counter = nodes_counter+1
            q_size = len(queue)
            # check max length of queue
            if max < q_size:
                max = q_size

    # right
    # same logic
    # for nxn we can replace 2 to n-1
    if c+1 <= 2:

        allow = 1
        temp1 = copy.deepcopy(queue[0].puzzle)
        temp = queue[0].puzzle[r][c+1]
        temp1[r][c+1] = 0
        temp1[r][c] = temp
        # queue length for check Whether this node has been previously expanded
        length = len(seen)
        # goal checker
        if temp1 == goal:
            print("-------------------")
            print(temp1[0])
            print(temp1[1])
            print(temp1[2])
            print("-------------------")
            print("===============find goal!!!!================")
           # print("with f(n): "+str(queue[0].gval+1+queue[0].hval))
            print("Depth: " + str(queue[0].gval+1))
            print("Number of nodes: " + str(nodes_counter))
            print("Max queue size: "+str(max))
            sys.exit()
        i = 0

        while i < length:

            if seen[i].puzzle == temp1:
                # print("find2!!!!")

                i = length+1
                allow = 0

            i = i+1
            # print("number2")
            # print(i)

        if allow == 1:

            child = copy.deepcopy(node(temp1))
            child.gval = queue[0].gval+1

            child_container.append(copy.deepcopy(child))
            # queue.append(copy.deepcopy(child))
            seen.append(copy.deepcopy(child))
            nodes_counter = nodes_counter+1
            if max < q_size:
                max = q_size

    #up and down
    # up
    # same logic
    if r > 0:

        allow = 1
        temp1 = copy.deepcopy(queue[0].puzzle)
        temp = queue[0].puzzle[r-1][c]
        temp1[r-1][c] = 0
        temp1[r][c] = temp
        length = len(seen)
        if temp1 == goal:
            print("-------------------")
            print(temp1[0])
            print(temp1[1])
            print(temp1[2])
            print("-------------------")
            print("===============find goal!!!!================")
            print("with f(n): "+str(queue[0].gval+1+queue[0].hval))
            print("Depth: " + str(queue[0].gval+1))
            print("Number of nodes: " + str(nodes_counter))
            print("Max queue size: "+str(max))
            sys.exit()
        i = 0

        while i < length:

            if seen[i].puzzle == temp1:
                # print("find3!!!!")
                i = length+1
                allow = 0

            i = i+1
            # print("number3")
            # print(i)

        if allow == 1:

            child = copy.deepcopy(node(temp1))
            child.gval = queue[0].gval+1

            child_container.append(copy.deepcopy(child))
            # queue.append(copy.deepcopy(child))
            seen.append(copy.deepcopy(child))
            nodes_counter = nodes_counter+1
            if max < q_size:
                max = q_size
   # for nxn replace 2 with n
    if r+1 <= 2:
        allow = 1
        temp1 = copy.deepcopy(queue[0].puzzle)
        temp = queue[0].puzzle[r+1][c]
        temp1[r+1][c] = 0
        temp1[r][c] = temp
        length = len(seen)
        if temp1 == goal:
            print("-------------------")
            print(temp1[0])
            print(temp1[1])
            print(temp1[2])
            print("-------------------")

            print("===============find goal!!!!================")
            print("with f(n): "+str(queue[0].gval+1+queue[0].hval))
            print("Depth: " + str(queue[0].gval+1))
            print("Number of nodes: " + str(nodes_counter))
            print("Max queue size: "+str(max))

            sys.exit()
        i = 0

        while i < length:

            if seen[i].puzzle == temp1:
                # print("find4!!!!")

                i = length+1
                allow = 0

            i = i+1
            # print("number4")
            # print(i)

        if allow == 1:

            child = copy.deepcopy(node(temp1))
            child.gval = queue[0].gval+1

            child_container.append(copy.deepcopy(child))
            # queue.append(copy.deepcopy(child))
            seen.append(copy.deepcopy(child))
            nodes_counter = nodes_counter+1
            if max < q_size:
                max = q_size

    queue.pop(0)  # pop out the node we expanded
    return child_container

# general search=>main “driver” program from Project_1_The_Eight_Puzzle_CS_170_2022.pdf


def general(problem, QUEUEING_FUNCTION):
    #global Variables
    global nodes_counter  # number of nodes we checked
    global max  # max of queue
    global q_size  # current queue size
    global seen  # the node we already checked
    global queue  # The node(nodes) we haven't checked yet
    child_container2 = []  # Temporary storage of node generated by expand
    global alltest  # test all 3 modes
    if QUEUEING_FUNCTION == 1 or 2 or 3:
        print("Staring Search")
        print("-------------------")
        print(problem[0])
        print(problem[1])
        print(problem[2])
        print("-------------------")
        # temp=matrix
        basic_node = node(problem)
       # print(basic_node.puzzle)
        # shallow copy only creates a copy of object not for the elements
        queue.append(copy.deepcopy(basic_node))
        q_size = +1  # queue size +1
        nodes_counter = +1
        max = q_size  # initialize max queue size
        queue[0].gval = 0  # initialize g(n)
        queue[0].hval = 0  # initialize h(n)

        # first node means we already seen
        seen.append(queue[0])
        # temp.append(copy.deepcopy(queue[0]))
        while True:

            # node = REMOVE-FRONT(nodes) I put to the expanding state that let me easy to handle queue(nodes) and debugging

            # sort funtion only need for Manhattan_Distance_and_misplaced
            if QUEUEING_FUNCTION == 2 or QUEUEING_FUNCTION == 3:
                # sort funtion(for Manhattan_Distance_and_misplaced By analyzing fval from large to small):https://stackoverflow.com/questions/16310015/what-does-this-mean-key-lambda-x-x1
                # queue = sorted(queue, key=lambda node: node.fval) #that time I only thought about f(n). didn't consider the depth so it caused more depth
                # https://www.programiz.com/python-programming/methods/built-in/sorted    added second condition
                queue = sorted(queue, key=lambda a: (a.gval + a.hval, a.gval))
        # failure checker
            if (len(queue)) == 0:
                return "failure"

            print(
                # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
                f"expanding node with g(n)={queue[0].gval} h(n) = {queue[0].hval} Puzzle:")
            print("-------------------")
            print(queue[0].puzzle[0])
            print(queue[0].puzzle[1])
            print(queue[0].puzzle[2])
            print("-------------------")
            temp1 = copy.deepcopy(queue[0].puzzle)
            # check goal
            if temp1 == goal:
                print("===============find goal!!!!================")
                #print("with f(n)"+str(queue[0].gval+1+queue[0].hval))
                print("Depth: " + str(queue[0].gval+1))
                print("Number of nodes: " + str(nodes_counter))
                print("Max queue size: "+str(max))

                sys.exit()
            # expand(queue,QUEUEING_FUNCTION)
            # expand the first node of queue and return the new nodes generated by the algorithm
            child_container2 = expand(queue, QUEUEING_FUNCTION)
            # store child if not meet goal for next iteration
            for q in child_container2:
                # QUEUEING-FUNCTION selector
                if QUEUEING_FUNCTION == 1:  # Manhattan_Distance_and_misplaced use else condition
                    q.hval = 0  # Uniform Cost Search always 0
                    q.fval = 0
                else:
                    q.hval = Manhattan_Distance_and_misplaced(
                        q.puzzle, QUEUEING_FUNCTION)
                    q.fval = q.gval+q.hval
                # append node to nodes(queue)
                queue.append(copy.deepcopy(q))


# ========================================================================================
# Manhattan_Distance I asked my classmate and he told me the basic logic and done by myself
def Manhattan_Distance_and_misplaced(problem, choice):
    sum = 0
    hconter = 0
    goal_index_row = 0
    goal_index_c = 0
    real_index_row = 0
    real_index_c = 0
    if choice == 3:
        # number 1-9
        for l in range(1, 9):

            for q in range(0, 3):
                for w in range(0, 3):
                    # The correct location of this value in the goal matrix
                    if goal[q][w] == l:
                        goal_index_row = q
                        goal_index_c = w
                    # current position
                    if problem[q][w] == l:
                        real_index_row = q
                        real_index_c = w
           # absolute value between rows and columns distance
            sum = sum+abs(real_index_row - goal_index_row) + \
                abs(real_index_c-goal_index_c)

    if choice == 2:
        # matrix
        for z in range(0, 3):
            for x in range(0, 3):
                # if not same then sum+1
                if goal[z][x] != problem[z][x]:
                    sum = sum+1
    return sum


def convert(list):
    # This was my first time writing code in python and I found it easier to manipulate the position of each "brick" using tuples
    return tuple(list)


if __name__ == '__main__':

    sample = ([1, 2, 3], [5, 0, 6], [4, 7, 8])  # sample

    print("1.Sample puzzle 2.Enter you puzzle with 1 number with ENTER each time")
    inputc = input()
    inputc = int(inputc)
    # print(type(inputc))
    if inputc == 2:  # https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
        puzzle = []
        print("Enter the entries rowwise for 3x3 matrix:")
        for i in range(3):
            a = []
            for j in range(3):
                a.append(int(input()))
            puzzle.append(a)
            # convert to tuple
        puzzle = convert(puzzle)

    else:
        puzzle = sample
    print("-------------------")
    print(puzzle[0])
    print(puzzle[1])
    print(puzzle[2])
    print("-------------------")
    print("search method")
    print('1. Uniform Cost Search.')
    print('2. A* with the Misplaced Tile heuristic.')
    print('3. A* with the Manhattan Distance heuristic.')
    selection = int(input())
    # general_search
    general(puzzle, selection)
