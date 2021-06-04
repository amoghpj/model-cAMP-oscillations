import matplotlib
font = {'size'   : 14}

matplotlib.rc('font', **font)
matplotlib.rcParams.update({'font.size': 22})
import matplotlib.pyplot as plt
from gonzales2011_4v import DS
# Set initial conditions to low glucose, get steady state
DS.set(pars={'G':0.0})

preshift = DS.compute('test').sample() # This is a python dictionary
preshiftics = {k:preshift[k][-1] for k in DS.variables}

# For varying stresses
Avals = [0.005, 0.014, 1.4]
labels = ['High', 'Intermediate', 'Low']

plt.figure(figsize=(8,6))
timescale = 0.037
stepsize = 0.1
start = int(50.0/(0.037*stepsize))
for A,lab in zip(Avals, labels):
    print(lab)
    # Glucose upshift
    DS.set(ics=preshiftics, pars={'G':1.0,'A':A},tdata=[0,2000])
    p = DS.compute('test').sample(dt=stepsize)
    plt.plot([timescale*t for t in p['t'][start:]], p['x'][start:],
    label=lab)
plt.legend(frameon=False) 
plt.xlabel('time (minutes)')   
plt.ylabel('cAMP (AU)')
plt.title('cAMP dynamics as a function of stress')
plt.tight_layout()
plt.savefig('./img/stress-regimes.png')
