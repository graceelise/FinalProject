#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:36:15 2019

@author: ganderson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:09:24 2019

@author: Bowton
"""

import finalProjectCodePart2 as fpc2

area,length = fpc2.getArea()
sweptArea = fpc2.getSweptArea()
diameter = fpc2.getRotorDiameter(sweptArea)
maxTurbines = fpc2.getMaxTurbines(diameter,length)
xCoordinates, yCoordinates = fpc2.getTurbineCoordinates(maxTurbines,diameter,length)
totalTurbines = fpc2.graphCoordinateList(xCoordinates,yCoordinates,diameter,length)
fpc2.totalPowerOutput(sweptArea, totalTurbines)