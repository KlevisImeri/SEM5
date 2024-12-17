from ortools.sat.python import cp_model
import math

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)  # add to model as callback
        self.__variables = variables
        self.__board_size = int(len(variables))
        self.__solutions = []

    def on_solution_callback(self):
        solution = [[0] * self.__board_size for _ in range(self.__board_size)]
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                solution[i][j] = self.Value(self.__variables[i][j])

        self.__solutions.append(solution)

    def get_solutions(self):
        return self.__solutions


def solve_sudoku(board):
  size = len(board)
  model = cp_model.CpModel();
  variables = [[model.NewIntVar(1, size, f'x{i}{j}') for j in range(size)] for i in range(size)]

  for row in variables:
    model.AddAllDifferent(row)

  for j in range(size):
    model.AddAllDifferent([variables[i][j] for i in range(size)])
  
  sizesub = 3
  for i in range(0,size,sizesub):
    for j in range(0,size,sizesub):
      model.AddAllDifferent([variables[i+l][j+k] for k in range(sizesub) for l in range(sizesub)])
  
  for i in range(size):
    for j in range(size):
      if board[i][j]!=0:
        model.Add(variables[i][j]==board[i][j])

  solver = cp_model.CpSolver()
  solution_collector = SolutionCollector(variables)
  # status = solver.SearchForAllSolutions(model, solution_collector)
  status = solver.Solve(model, solution_collector)
  import time
  time.sleep(1) # Sleep for 3 seconds

  return solution_collector.get_solutions()[0]

