import math
import statistics

# our math user function "exp_cos" is defined as f(x) = e^cos(x) - 0.5
def exp_cos(x):
  return math.exp(math.cos(x)) - 0.5

# return True if a and b have the same sign. may be problematic if a or b is zero, but this would be caused by user error
def same_sign(a, b):
  return ((a < 0) == (b < 0))

# our bisection algorithim for finding the zero-root of a function between values a and b
def bisection(user_function, value_a, value_b, max_iterations=99, tolerance=1e-9):

  # count each iteration
  i = 1

  # our first guess and each following guess will be the mean between values a and b
  guess = statistics.mean([value_a, value_b])

  # perform the loop below while the function evaluation of our guess is not (close) to zero, and we have not reached the max iteration
  while (not math.isclose(user_function(guess), 0, abs_tol=tolerance) and i <= max_iterations):

    # print each guess
    print(f"guess {i}: {guess}")

    # set the value of a to the guess if the sign of the function evaluation of the guess and value a are the same
    if same_sign(user_function(guess), user_function(value_a)):
      value_a = guess

    # set the value of b to the guess if the sign of the function evaluation of the guess and value b are the same
    elif same_sign(user_function(guess), user_function(value_b)):
      value_b = guess

    # return null if the sign of the function evaluation of the guess is not the same as either value
    else:
      print(f"\ncaution: the user function has zero roots, more than one root, or asymptotic in the interval [{value_a}, {value_b}]")
      print("try entering new values for a and b\n")
      return None

    # update with a new guess for the next iteration
    guess = statistics.mean([value_a, value_b])

    # increment the iteration
    i += 1

  # if max iterations is reached, the root cannot be confidently located, or requires a greater number of max iterations
  if i > max_iterations:
    print("\ncaution: max iterations exceeded\nnot confident in finding root")
    print("try entering new values for a and b, or increasing the value of max iterations\n")
    return None

  # display root and function evaluation of root (value should be within zero and tolerance)
  else:
    print(f"\nguess {i}: root located\n  x  = {guess}\nf(x) = {user_function(guess)}")
    return guess

bisection(exp_cos, 0, 3)
"""
guess 1: 1.5
guess 2: 2.25
guess 3: 2.625
guess 4: 2.4375
guess 5: 2.34375
guess 6: 2.296875
guess 7: 2.3203125
guess 8: 2.33203125
guess 9: 2.337890625
guess 10: 2.3349609375
guess 11: 2.33642578125
guess 12: 2.337158203125
guess 13: 2.3367919921875
guess 14: 2.33660888671875
guess 15: 2.336700439453125
guess 16: 2.3366546630859375
guess 17: 2.3366317749023438
guess 18: 2.3366432189941406
guess 19: 2.336637496948242
guess 20: 2.3366403579711914
guess 21: 2.336641788482666
guess 22: 2.3366425037384033
guess 23: 2.336642861366272
guess 24: 2.3366426825523376
guess 25: 2.3366425931453705
guess 26: 2.336642548441887
guess 27: 2.336642526090145
guess 28: 2.336642514914274

guess 29: root located
  x  = 2.3366425205022097
f(x) = 4.0067871243110176e-10
"""