import pygal

population = {
'cn':1.6,
'in':1.4,
'us':0.4,
'jp':0.12,
'ae':0.01
}
chart = pygal.maps.world.World()
chart.title='Population of 5 countries'
chart.add('Latest Info', population)
chart.render_in_browser()
