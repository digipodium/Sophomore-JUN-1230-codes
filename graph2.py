import pygal

b = pygal.Bar()
b.add('India',[90,45,76,89])
b.add('China',[89,45,78,34])
b.add('Sri Lanka',[None,None,54,66])
b.render_in_browser()
