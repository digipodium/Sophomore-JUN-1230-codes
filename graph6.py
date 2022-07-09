import pygal

chart = pygal.maps.world.SupranationalWorld()
chart.add('Asia',[('asia',1)])
chart.add('Europe',[('europe',1)])
chart.add('Africa',[('africa',1)])
chart.add('North America',[('north_america',1)])
chart.add('South America',[('south_america',1)])
chart.add('Antartica',[('antartica',1)])
chart.add('Australia n islands',[('oceania',1)])
chart.render_in_browser()
