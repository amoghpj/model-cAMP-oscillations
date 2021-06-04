import PyDSTool as dst
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
font = {'family' : 'normal',
        'size'   : 18}
matplotlib.rc('font', **font)
plt.figure(figsize= (8, 6))
# Import model
from gonzales2011_4v import DSargs

g4v = dst.Vode_ODEsystem(DSargs)
g4v.set(tdata=[0,300], pars={'A':0.0001})

PC = dst.ContClass(g4v)
PCargs = dst.args(name='EQ1', type='EP-C')
freepar = 'A'
PCargs.freepars= [freepar]

# Bifurcation analysis settings
PCargs.MaxNumPoints = 300
PCargs.MaxStepSize = 1e-1
PCargs.MinStepSize = 1e-5
PCargs.StepSize = 1e-3

PCargs.LocBifPoints = 'all'
PCargs.SaveEigen = True

PC.newCurve(PCargs)
PC['EQ1'].forward()
PC['EQ1'].info() 

PCargs = dst.args(name='LC1', type='LC-C')
PCargs.freepars = ['A']

# Once the Hopf point H2 is found, continue and identify other special points
PCargs.name = 'LC1'
PCargs.type = 'LC-C'
PCargs.initpoint = 'EQ1:H2'
PCargs.MinStepSize = 0.000001
PCargs.MaxStepSize = .01
PCargs.StepSize = 0.00001
PCargs.MaxNumPoints = 420
PCargs.NumSPOut = 10000;
PCargs.LocBifPoints = []
PCargs.verbosity = 2
PCargs.SolutionMeasures = 'avg'
PCargs.SaveEigen = True
PCargs.StropAtPoints = True
PC.newCurve(PCargs)

PC['LC1'].backward()
PC['LC1'].forward()

PC.display((freepar,'x'),stability=True, figure=4)
PC['LC1'].display((freepar,'x_min'),stability=True, figure=4)

plt.title('Bifurcation diagram parameter A')
plt.xscale('log')
plt.tight_layout()
plt.savefig('./img/bifurcation-points.png', dpi=200)
