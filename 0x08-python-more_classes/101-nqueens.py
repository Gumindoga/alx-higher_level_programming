#!/usr/bin/python3
import sys


def solve_nqueens(n):
    if n < 1:
        return []
    solutions = []
    dfs(n, [], [], [], solutions)
    return solutions


def dfs(n, queens, xy_dif, xy_sum, solutions):
    p = len(queens)
    if p == n:
        solutions.append(queens)
        return None
    for q in range(n):
        if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
            dfs(n, queens+[q], xy_dif+[p-q], xy_sum+[p+q], solutions)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(n)
    for solution in solutions:
        result = []
        for i in range(n):
            result.append([i, solution[i]])
        print(result)


if __name__ == "__main__":
    main()
