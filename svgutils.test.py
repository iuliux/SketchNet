import svgutils.transform as sg
import math

#create new SVG figure
fig = sg.SVGFigure("1500px", "1500px")

# load matpotlib-generated figures
fig1 = sg.fromfile('mpt1.svg')
fig2 = sg.fromfile('mpt2.svg')

up1 = fig1.find_id('MP_1_u').root
print up1
rg1 = fig1.find_id('MP_1_r').root
up2 = fig2.find_id('MP_1_u').root
rg2 = fig2.find_id('MP_1_r').root

fig1scale = math.sqrt((float(up1.get('x1')) - float(up1.get('x2')))**2 + (float(up1.get('y1')) - float(up1.get('y2')))**2)
fig2scale = math.sqrt((float(up2.get('x1')) - float(up2.get('x2')))**2 + (float(up2.get('y1')) - float(up2.get('y2')))**2)
print fig1scale, fig2scale
midscale = (fig1scale + fig2scale) / 2.
fig1_normscale = fig1scale / midscale
fig2_normscale = fig2scale / midscale
print fig1_normscale, fig2_normscale

displacement = (float(up1.get('x1'))*fig2_normscale - float(up2.get('x1'))*fig1_normscale, float(up1.get('y1'))*fig2_normscale - float(up2.get('y1'))*fig1_normscale)

# get the plot objects
plot1 = fig1.getroot()
plot2 = fig2.getroot()
plot1.moveto(500, 500, scale=fig2_normscale)
plot2.moveto(500 + displacement[0], 500 + displacement[1], scale=fig1_normscale)

# TODO: Rotation
# plot2.rotate(45)

# add text labels
txt1 = sg.TextElement(25,20, "A", size=32, weight="bold")
txt2 = sg.TextElement(305,20, "B", size=32, weight="bold")

# append plots and labels to figure
fig.append([plot1, plot2])
fig.append([txt1, txt2])

# save generated SVG files
fig.save("fig_final.svg")
