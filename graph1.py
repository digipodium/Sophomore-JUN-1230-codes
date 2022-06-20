import pygal

numbers = [90,34,67,34,89,43,68,12,45,34]
b = pygal.Bar()
b.add('my numbers',numbers)
b.render_in_browser()
