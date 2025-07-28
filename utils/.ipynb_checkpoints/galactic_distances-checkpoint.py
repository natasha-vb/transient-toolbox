def galactic_distances(glat, glong, d):
    import numpy as np

    # angle from galactic centre
    if glong > 180:
        theta = 360.0 - glong
    else:
        theta = glong

    theta_rad = np.deg2rad(theta)

    # x and y lengths of triangle 1 
    # formed from sun, source position, and line towards Galctic centre
    tri1_x = d * np.sin(theta_rad)
    tri1_y = d * np.cos(theta_rad)
    
    # distance from Galactic centre to source/ hypotenuse of triangle 2
    # triangle 2 y distance is difference between distance from sun to Galactic centre, 8.3 kpc
    # and y distance from triangle 1
    tri2_y = 8.3 - tri1_y
    tri2_z = np.sqrt(tri2_y**2 + tri1_x**2)

    # height above Galactic plane
    h = d * np.tan(np.deg2rad(glat))

    return tri2_z, h
