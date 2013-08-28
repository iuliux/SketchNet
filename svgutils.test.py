import svgutils.transform as sg
import sys 

#create new SVG figure
fig = sg.SVGFigure("1500px", "1500px")

# load matpotlib-generated figures
fig1 = sg.fromfile('t1.svg')
fig2 = sg.fromfile('t2.svg')

# get the plot objects
plot1 = fig1.getroot()
plot2 = fig2.getroot()
plot2.moveto(280, 0, scale=1.5)
plot2.rotate(45)

# add text labels
txt1 = sg.TextElement(25,20, "A", size=32, weight="bold")
txt2 = sg.TextElement(305,20, "B", size=32, weight="bold")

# append plots and labels to figure
fig.append([plot1, plot2])
fig.append([txt1, txt2])

# save generated SVG files
fig.save("fig_final.svg")
