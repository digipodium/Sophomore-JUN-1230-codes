import pygal

chart = pygal.Pie(half_pie=True)
chart.title='Our Movie Rating'
chart.add('Kung fu Panda',7)
chart.add('Anabelle',3)
chart.add('Avengers:End Game',9.5)
chart.add('Free Guy',8)
chart.add('Karate Kid',2)
chart.render_in_browser()
