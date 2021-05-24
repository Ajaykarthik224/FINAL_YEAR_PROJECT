import json
import matplotlib.pyplot as plt


def show_graph(subdivision):
    file = open('data/data.json')
    data = json.load(file)
    years = []
    rainfall = []
    count = 0
    for i in data['records']:
        if(i['subdivision'] == subdivision) and count % 10 == 0:
            if i['annual'] == 'NA':
                continue
            else:
                rainfall.append(int(float(i['annual'])))
                years.append(i['year'])

        count += 1

    plt.scatter(years, rainfall, label="stars", color="green",
                marker="*", s=30)

    plt.xlabel('Year')
    plt.ylabel('Rainfall in mm')
    plt.title('Annual Rainfall')

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.show()


# show_graph('Andaman & Nicobar Islands')
