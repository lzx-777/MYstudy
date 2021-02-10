'''
@Author: Govern 
@Date: 2021-01-21 23:47:52
@Description:
    This is for test 9814 21T0 summer term assignment 1.
    The test cases are in test_case.py, there are cases given by assignment 
    and cases in dict test_case, for each optimal cost from 11 to 40 given two 
    or three start puzzles, generated by IDA* Search.
    Put your class and function in assignment.py file 
'''
from assignment import*
from test_case import*
import time

def test_env():
    for var in search_case:
        print("Using case: ",var)
        for class_name in ["GameFifteenProblem", "GameFifteenProblemEuclidean", "GameFifteenProblemInversions"]:
            print("Testing class: ",class_name)
            puzzle = eval(class_name)(search_case[var],goal)
            print("heuristic: ", puzzle.heuristic(np.array(search_case[var])))
            searcher = AStarSearcher(puzzle)
            start_time = time.time()
            solution = searcher.search()
            end_time = time.time()
            if solution:
                print('Cost: ',  solution.cost)
                print('Time: ',  (end_time - start_time)*1000)
            else:
                print("No solution")
            print("------------------------------------")
        print("************************************")

def test_search():
    for var in search_case:
        print("Using case: ",var)
        for class_name in ["BreadthFirstSearcher", "AStarSearcher", "IterativeDeepeningSearcher", "IterativeDeepeningAStarSearcher", "UniformCostSearcher"]:
            print("Testing class: ",class_name)   
            puzzle = GameFifteenProblem(search_case[var],goal)
            searcher = eval(class_name)(puzzle)
            start_time = time.time()
            solution = searcher.search()
            end_time = time.time()
            if(solution):
                print('Cost: ',  solution.cost)
            else:
                print("No solution")
            print('Time: ',  (end_time - start_time)*1000)
            print("------------------------------------")
        print("************************************")

def test_csp():
    print("TEST CSP")
    csp = grid_to_csp(grid)
    for class_name in ["Searcher", "BreadthFirstSearcher", "IterativeDeepeningSearcher","UniformCostSearcher"]:
        if class_name == "Searcher": print("Testing class: DepthFirstSearcher")
        else: print("Testing class: ", class_name)
        start_time = time.time()
        path = eval(class_name)(Search_from_CSP(csp)).search()
        end_time = time.time()
        if path :
            for loc in path.end():
                grid[loc[0]][loc[1]] = path.end()[loc]
            print(np.array(grid))
        else:
            print("No solution")
        print('Time: ',  (end_time - start_time)*1000)

# def test_special():

if __name__ == "__main__":
    test_env()
    test_search()
    test_csp()
    pass