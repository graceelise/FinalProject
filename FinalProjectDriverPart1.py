#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:33:14 2019

@author: ganderson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:08:41 2019

@author: Bowton
"""

#PART 1 DRIVER

import finalProjectCode as fpc


sweptArea, power = fpc.readFile()
turbineSA, turbineP, turbineCOP = fpc.createTestTurbine()
fpc.graphData(sweptArea, power, turbineSA, turbineP)
fpc.bestFitSlope(sweptArea,power)
idealPower = fpc.idealPower(sweptArea)
efficiency = fpc.efficiency(idealPower,power)
fpc.efficiencyGraphs(efficiency, sweptArea, power)
fpc.bestFitSlopeEfficiency(power,efficiency)
fpc.efficiencyHistogram(efficiency)
fpc.meanEfficiency(efficiency)