import svgutils.transform as sg
import geomutils

xmlnsmap = {'svg': 'http://www.w3.org/2000/svg'}


def _get_MP(skname, sk, mp_id):
    '''
    skname = the name of the sketch
    sk = sketch object returned by load_sketch()
    nMP = the number ID of the MountingPoint to be returned
    '''
    mpstart = 'MP_' + skname
    if mp_id:
        mpstart += '_' + str(mp_id)

    baseQuery = '//svg:line[starts-with(@id, "%s")'
    endswithQuery = '"%s" = substring(@id, string-length(@id) - 1)]'
    u = sk.root.xpath(baseQuery % mpstart + ' and ' + endswithQuery % '_u', namespaces=xmlnsmap)
    r = sk.root.xpath(baseQuery % mpstart + ' and ' + endswithQuery % '_r', namespaces=xmlnsmap)

    return (u, r)


def register_sketches(skname1, sk1, skname2, sk2, mp1=1, mp2=1):
    def parse_line(elem):
        return ((float(elem.get('x1')), float(elem.get('y1'))),
                (float(elem.get('x2')), float(elem.get('y2'))))

    print _get_MP(skname1, sk1, mp1)

    # Get mounting points guide lines
    up1 = parse_line(sk1.find_id('MP_' + skname1 + '_' + str(mp1) + '_u').root)
    rg1 = parse_line(sk1.find_id('MP_' + skname1 + '_' + str(mp1) + '_r').root)
    up2 = parse_line(sk2.find_id('MP_' + skname2 + '_' + str(mp2) + '_u').root)
    rg2 = parse_line(sk2.find_id('MP_' + skname2 + '_' + str(mp2) + '_r').root)

    # Compute scales to make the two figures match in size
    fig1scale = geomutils.line_len(up1)
    fig2scale = geomutils.line_len(up2)
    midscale = (fig1scale + fig2scale) / 2.  # The average of the two scales
    fig1_normscale = fig1scale / midscale
    fig2_normscale = fig2scale / midscale
    print '--scales-->', fig1scale, fig2scale
    print '--normscales-->', fig1_normscale, fig2_normscale

    # 2D displacement of the second figure
    displacement = (up1[0][0]*fig2_normscale - up2[0][0]*fig1_normscale,
                    up1[0][1]*fig2_normscale - up2[0][1]*fig1_normscale)

    # Get the plot objects
    plot1 = sk1.getroot()
    plot2 = sk2.getroot()
    plot1.moveto(0, 0, scale=fig2_normscale)
    plot2.moveto(0 + displacement[0], 0 + displacement[1], scale=fig1_normscale)

    # Rotation
    plot1.rotate(-90 - geomutils.line_angle(up1), up1[0][0], up1[0][1])
    plot2.rotate(-90 - geomutils.line_angle(up2), up2[0][0], up2[0][1])

    # TODO: Flip if needed

    # Create new SVG figure
    fig = sg.SVGFigure("1500px", "1500px")  # FIXME: hardcoded size

    # Append plots and labels to figure
    fig.append([plot1, plot2])
    return fig


def load_sketch(figname):
    '''
    Loads SVG sketch file and returns an object
    '''
    return sg.fromfile(figname + '.svg')


if __name__ == '__main__':
    figname1 = 'flying-thing'
    figname2 = 'mpt2'
    # Load test figures
    fig1 = load_sketch(figname1)
    fig2 = load_sketch(figname2)

    # Match and combine the two figures
    regfig = register_sketches(figname1, fig1, figname2, fig2)

    # Save generated SVG file
    regfig.save("fig_final.svg")
