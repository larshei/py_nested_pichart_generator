import matplotlib.pyplot as plt
from setup import chart_config as cfg
from setup import chart_colors

# get total weight (we will scale the sections according to their weight!)
sections_total_weight = 0
for section in cfg["sections"]:
    sections_total_weight += section["weight"]

# 'sections' are fictional, they just tell us how to scale the elements in each donut diagram.
number_of_donuts = 0
for section in cfg["sections"]:
    donuts_in_section = len(section["layers"])
    number_of_donuts = max(donuts_in_section,number_of_donuts)

# width per element in each donuts section
donuts = dict()
donuts["sizes"] = []
donuts["labels"] = []
donuts["element_colors"] = []

colors = [
    chart_colors["red"],
    chart_colors["purple"],
    chart_colors["blue"],
    chart_colors["cyan"],
    chart_colors["cyan5"],
    chart_colors["cyan2"]
]

# go through donuts.
# for each donut, check the elements and scale them.
# store the scaled elements sizes of all sections for this donut
for donut_number in range(0, number_of_donuts):
    element_sizes  = []
    element_colors = []
    element_labels = []
    for section in cfg["sections"]:
        donuts_in_section = len(section["layers"])
        donut_in_section_not_empty = (donuts_in_section >= donut_number + 1)
        section_size = section["weight"] / sections_total_weight
        if donut_in_section_not_empty:
            elements_in_section_donut = len(section["layers"][donut_number]["elements"])
        else:
            elements_in_section_donut = 1

        for element_number in range(0, elements_in_section_donut):
            if cfg["color_by_ring"]:
                color = colors[donut_number]#(color_saturation)
            else:
                color = colors[cfg["sections"].index(section)]#(color_saturation)

            if donut_in_section_not_empty:
                label = section["layers"][donut_number]["elements"][element_number]
            else:
                color = (0,0,0,0)
                label = None

            element_sizes.append(section_size / elements_in_section_donut)
            element_colors.append(color)
            element_labels.append(label)
            

    donuts["sizes"].append(element_sizes)
    donuts["labels"].append(element_labels)
    donuts["element_colors"].append(element_colors)



#create drawarea
colors=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Purples, plt.cm.Oranges]
fig, ax = plt.subplots()
ax.axis('equal')

donut_drawings = [None] * number_of_donuts
donut_radius =0
for donut_number in range(0, number_of_donuts):
    donut_radius =  donut_radius + 0.8 / (donut_number + 1) + 0.2
    donut_radius_next =  donut_radius + 0.8 / (donut_number + 1) + 0.2
    donut_width = donut_radius_next - donut_radius
    color_val = 0.6 - donut_number * 0.1
    print(donuts["element_colors"][donut_number])
    label_distance = (donut_radius - donut_width/2) / donut_radius
    labels =  donuts["labels"][donut_number] if cfg["show_labels"] else None  
    donut_drawings[donut_number], _ = ax.pie(
                                            donuts["sizes"][donut_number], 
                                            labels = labels, 
                                            labeldistance = label_distance,
                                            radius = donut_radius, 
                                            startangle = cfg["start_angle"],
                                            colors = donuts["element_colors"][donut_number] )
    plt.setp( donut_drawings[donut_number], width = donut_radius_next - donut_radius, edgecolor='white')
 
# # First Ring (outside)

# mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6), c(0.6)] )
 
# # Second Ring (Inside)
# mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, labeldistance=0.7, colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
# plt.setp( mypie2, width=0.4, edgecolor='white')
# plt.margins(20,20)

# # show it
plt.show()
