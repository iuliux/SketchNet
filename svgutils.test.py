import svgutils.transform as sg
import math


def line_angle(line):
    p1, p2 = line
    xDiff = p2[0] - p1[0]
    yDiff= p2[1] - p1[1]

    return math.degrees(math.atan2(yDiff, xDiff))


def register_sketches(sk1, sk2, mp1=1, mp2=1):
    def parse_line(elem):
        return ((float(elem.get('x1')), float(elem.get('y1'))),
                (float(elem.get('x2')), float(elem.get('y2'))))

    # Get mounting points guide lines
    up1 = parse_line(sk1.find_id('MP_' + str(mp1) + '_u').root)
    rg1 = parse_line(sk1.find_id('MP_' + str(mp1) + '_r').root)
    up2 = parse_line(sk2.find_id('MP_' + str(mp2) + '_u').root)
    rg2 = parse_line(sk2.find_id('MP_' + str(mp2) + '_r').root)

    # Compute scales to make the two figures match in size
    fig1scale = math.sqrt((up1[0][0] - up1[1][0])**2 + (up1[0][1] - up1[1][1])**2)
    fig2scale = math.sqrt((up2[0][0] - up2[1][0])**2 + (up2[0][1] - up2[1][1])**2)
    midscale = (fig1scale + fig2scale) / 2.  # The average of the two scales
    fig1_normscale = fig1scale / midscale
    fig2_normscale = fig2scale / midscale
    print '--scales-->', fig1scale, fig2scale
    print '--normscales-->', fig1_normscale, fig2_normscale

    # 2D displacement of the second figure
    displacement = (up1[0][0]*fig2_normscale - up2[0][0]*fig1_normscale,
                    up1[0][1]*fig2_normscale - up2[0][1]*fig1_normscale)

    # Get the plot objects
    plot1 = fig1.getroot()
    plot2 = fig2.getroot()
    plot1.moveto(0, 0, scale=fig2_normscale)
    plot2.moveto(0 + displacement[0], 0 + displacement[1], scale=fig1_normscale)

    # Rotation
    plot1.rotate(-90 - line_angle(up1), up1[0][0], up1[0][1])
    plot2.rotate(-90 - line_angle(up2), up2[0][0], up2[0][1])

    # TODO: Flip if needed

    # Create new SVG figure
    fig = sg.SVGFigure("1500px", "1500px")

    # Append plots and labels to figure
    fig.append([plot1, plot2])

    return fig


# load matpotlib-generated figures
fig1 = sg.fromfile('mpt1.svg')
fig2 = sg.fromfile('mpt2.svg')

# save generated SVG files
regfig = register_sketches(fig1, fig2)

regfig.save("fig_final.svg")
