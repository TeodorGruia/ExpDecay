def percent_Decrease(x,a):
  '''
  Retuns the percentage of decrease for a pair of numbers.

  x: Int Older
  a: Int Newer
  '''
  percentDecrease = (x-a)/x

  return percentDecrease
def main_Decay(y, a, b, x):
  '''
  Returns non-algebraic exponential decay

  y: Int Final amount remaining 
  a:Iint Initial Amount
  x: Dec time factor
  b: dec percent change (decimal form)
  '''
