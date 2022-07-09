import pygal

chart = pygal.SolidGauge(inner_radius=.70,half_pie=True)
chart.add('Fruits',[{'value':50,'max-value':100}])
chart.add('Vegetables',[{'value':70,'max-value':100}])
chart.add('Cereals',[{'value':30,'max-value':100}])
chart.render_in_browser()
