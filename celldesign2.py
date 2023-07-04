from sympy.plotting import plot_parametric
from sympy import Symbol, cos, sin


def draw_heart():
  t = Symbol('t')
  x = 16 * sin(t) ** 3
  y = 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)

  p = plot_parametric(x, y, autoscale=True, title='heart', show=False)
  p[0].line_color = 'pink'
  p.show()
