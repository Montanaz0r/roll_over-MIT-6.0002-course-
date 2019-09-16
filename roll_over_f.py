# roll_over_f.py - checks how to maximize value of equation by setting up certain variables.

#Score = ((60 – (a+b+c+d+e))*F + a*ps1 + b*ps2 + c*ps3 + d*ps4 + e*ps5
# Objective:
# Given values for F, ps1, ps2, ps3, ps4, ps5
# Find values for a, b, c, d, e that maximize score
#
# Constraints:
# a, b, c, d, e are each 10 or 0
# a + b + c + d + e ≥ 20


def constants(F, ps1, ps2, ps3, ps4, ps5):
    '''defining list of constants: F and from ps1 to ps5'''
    scalar = F
    list_of_constants = [ps1, ps2, ps3, ps4, ps5]
    return (scalar, list_of_constants)

def roll_over(scal, const):
    '''rolls over equation checks how to maximize the score'''
    vars = ['a', 'b', 'c', 'd', 'e']
    choices = []                            # list of choices (0 or 10 for each)
    gained_value = {}                       # value gained, checked only in case choice was 0 instead of 10
    F_scalar_value = 10 * scal              # scalar value will check what value we are adding to equation
    for i in range(len(vars)):              # in case we chooce varible to be 0 and not 10
        ps_value = const[i] * 10
        if F_scalar_value > ps_value:
            choices.append(0)
            gained_value[F_scalar_value - ps_value] = i
        else:
            choices.append(10)
    print(f'dictionary of gained value: {gained_value}')
    if sum(choices) == 10:                                   # checking if sum of our choices meets the constraint
        print('sum of our choices is equal to 10')
        lowest_value = min(gained_value.items())[1]          # dropping the lowest value in gained_values list in order
        print(f'currently dropping {lowest_value}...')       # to meet constraints.
        print(f'changing {choices[lowest_value]} to 10')
        choices[lowest_value] = 10
    elif sum(choices) == 0:                                  # checking if sum of our choices meets the constraint
        lowest_key, lowest_value = min(gained_value.items()) # searching for lowest value and key of this value to later
        print(f'dropping {lowest_value}...')                 # pop this item from the dictionary.
        print(f'changing {choices[lowest_value]} to 10')
        choices[lowest_value] = 10
        print(f'removing lowest value item {gained_value[lowest_key]}. Now checking for second lowest')
        gained_value.pop(lowest_key)
        lowest_key, lowest_value = min(gained_value.items())
        print(f'dropping {lowest_value}...')
        print(f'changing {choices[lowest_value]} to 10')
        choices[lowest_value] = 10

    assert sum(choices) >= 20                                # final check if our solutions meets constraints.
    solutions = dict(zip(vars, choices))                     # saving solution as dictionary (pairs - variable:choice)
    print(f'This is the best solution to equation: {solutions}.')
    return solutions

def solve_equation(scal, const, solution):
    '''solving equation, returning score'''
    ps1, ps2, ps3, ps4, ps5 = const
    Score = ((60 - sum(solution.values())) * scal + (solution['a'] * ps1) + (solution['b'] * ps2) + (solution['c'] * ps3) +
             (solution['d'] * ps4) + (solution['e'] * ps5))
    print(f'our solution scored: {Score} points.')
    return Score


con = constants(F=2, ps1=1, ps2=1, ps3=-1, ps4=-2, ps5=1)     # set your own constant values which will be indicated in
scal, const = con                                             # the equation.
solution = roll_over(scal, const)                             # roll over it
score = solve_equation(scal, const, solution)                 # solve the equation for max score.


