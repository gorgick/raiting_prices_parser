import csv
import pygal
from pygal.style import LightSolarizedStyle as LCS, LightenStyle as LS

with open('21vek.csv') as f:
    reader = csv.reader(f)
    list_data = []
    for row in reader:
        list_data.append(row)
    # Del empty data from our csv file
    list_data = list_data[::2]
    for_graphic = []
    # Some prices of grass-cutter didn't have a price, we del them
    for el in list_data:
        if el[1] == '':
            pass
        else:
            for_graphic.append(el)
# Sort our data by price of grass-cutters
for_graphic.sort(key=lambda price: int(price[1]))


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Max and min prices of grass-cutter'
# Make a list of some y_min_max_prices and their x_names for better visualization into the graphic
chart.x_labels = [el[0] for el in for_graphic][:15]+[el[0] for el in for_graphic][-15:]
chart.add('', [int(el[1]) for el in for_graphic][:15]+[int(el[1]) for el in for_graphic][-15:])
chart.render_to_file('grass_cutter.svg')


