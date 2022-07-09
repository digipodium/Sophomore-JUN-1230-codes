import pygal
from pygal.style import BlueStyle

chart = pygal.StackedLine(fill=True, style=BlueStyle, interpolate='cubic')
chart.title = 'Simple LIne Chart'
chart.x_labels = map(str, range(2012,2023)) # create a list of numbers from 2012 to 2022 as strings
chart.add('Lucknow',[56,34,67,89,90,67,62,45,55,32,45])
chart.add('Delhi',[34,56,34,56,67,78,45,67,78,56,34])
chart.render_in_browser()
