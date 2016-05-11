import copy
import sys

## find possible solutions for 3 numbers
def routes3(nums):
    routes = [[-nums[0],-nums[1],-nums[2]],
              [-nums[0],-nums[1],nums[2]],
              [-nums[0],nums[1],-nums[2]],
              [-nums[0],nums[1],nums[2]]
    ]
    return routes
    

## find possible solutions for 4 numbers    
def routes4(nums):
    routes = [[-nums[0],-nums[1],-nums[2],-nums[3]],
              [-nums[0],-nums[1],-nums[2],nums[3]],
              [-nums[0],-nums[1],nums[2],-nums[3]],
              [-nums[0],-nums[1],nums[2],nums[3]],
              [-nums[0],nums[1],-nums[2],-nums[3]],
              [-nums[0],nums[1],-nums[2],nums[3]],
              [-nums[0],nums[1],nums[2],-nums[3]],
              [-nums[0],nums[1],nums[2],nums[3]]
    ]
    return routes


## find possible solutions for 5 numbers
def routes5(nums):
    routes = [[-nums[0],-nums[1],-nums[2],-nums[3],-nums[4]],
              [-nums[0],-nums[1],-nums[2],-nums[3],nums[4]],
              [-nums[0],-nums[1],-nums[2],nums[3],-nums[4]],
              [-nums[0],-nums[1],-nums[2],nums[3],nums[4]],
              [-nums[0],-nums[1],nums[2],-nums[3],-nums[4]],
              [-nums[0],-nums[1],nums[2],-nums[3],nums[4]],
              [-nums[0],-nums[1],nums[2],nums[3],-nums[4]],
              [-nums[0],-nums[1],nums[2],nums[3],nums[4]],
              [-nums[0],nums[1],-nums[2],-nums[3],-nums[4]],
              [-nums[0],nums[1],-nums[2],-nums[3],nums[4]],
              [-nums[0],nums[1],-nums[2],nums[3],-nums[4]],
              [-nums[0],nums[1],-nums[2],nums[3],nums[4]],
              [-nums[0],nums[1],nums[2],-nums[3],-nums[4]],
              [-nums[0],nums[1],nums[2],-nums[3],nums[4]],
              [-nums[0],nums[1],nums[2],nums[3],-nums[4]],
              [-nums[0],nums[1],nums[2],nums[3],nums[4]]
    ]
    return routes
    

## basic solver    
def solver(numbers, goal):
    if len(numbers) == 3:
        routes = routes3(numbers)
    elif len(numbers) == 4:
        routes = routes4(numbers)
    else:
        routes = routes5(numbers)
        
    for route in routes:
        if abs(sum(route)) == abs(goal):
            solution = route
            break
    else:
        solution = 'No solution is found'
        
    return solution


## multiply each number by 2 and try to find a solution
def solverTimes2(numbers, goal):    
    for i in range(0,len(numbers)):
        newNumbers = copy.deepcopy(numbers)
        newNumbers[i] = numbers[i] * 2
        solution = solver(newNumbers, goal)
        if type(solution)!=str:
            break
        
    return solution
    

## divide each number by 2 and try to find a solution    
def solverDivide2(numbers, goal):
    for i in range(0,len(numbers)):
        if numbers[i] % 2 == 0:
            newNumbers = copy.deepcopy(numbers)
            newNumbers[i] = numbers[i] / 2
            solution = solver(newNumbers, goal)
            if type(solution)!=str:
                break
    
    return solution
    

## first stage: basic solver
def stage1(numbers, goal):
    solution = solver(numbers, goal)
    return solution
    

## second stage: basic solver with goal = 0
def stage2(numbers):
    solution = solver(numbers, 0)
    return solution


## third stage: try multiplying numbers by 2
def stage3(numbers, goal):
    solution = solverTimes2(numbers, goal)
    return solution
    

## forth stage: try dividing numbers by 2    
def stage4(numbers, goal):
    solution = solverDivide2(numbers, goal)
    return solution
    


def solve(numbers, goal):
    stage1Sol = stage1(numbers, goal)
    if type(stage1Sol) != str:
        solution = stage1Sol
    else:
        stage2Sol = stage2(numbers)
        if type(stage2Sol) != str:
            solution = stage2Sol
        else:
            if raw_input('Do you have a x2 tile? Enter y or n.') == 'y':
                stage3Sol = stage3(numbers, goal)
                if type(stage3Sol) != str:
                    solution = stage3Sol
                    #extraInfo = 'Multiply __ tile by 2.'
                else:
                    stage4Sol = stage4(numbers, goal)
                    if type(stage4Sol) != str:
                        solution = stage4Sol
                        #extraInfo = 'Divide __ tile by 2.'
                    else:
                        if raw_input('Do you have a random tile? Enter y or n.') == 'y':
                            print 'Change a number using the random title and run the program again.'
                            sys.exit()
                        else:
                            solution = 'No solution is found'
            else:
                if raw_input('Do you have a random tile? Enter y or n.') == 'y':
                    print 'Change a number using the random title and run the program again.'
                    sys.exit()
                else:
                    solution = 'No solution is found'
        
    return solution
    




def main():
    numbers = [int(num)
        for num in
        raw_input('Enter the given numbers separated by spaces.').split()
        ]
    goal = input('Enter the goal number.')
    
    solution = solve(numbers, goal)

    print 'The solution is: {}. Dark is + and light is -.'.format(solution)

main()
