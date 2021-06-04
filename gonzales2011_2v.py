import PyDSTool as dst
import matplotlib.pyplot as plt

DSargs = dst.args(name='test',
                  varspecs={
		      'p' : 'M*(x^2 - p)',
		      'x' : 'C0 - D0*x - (D*p*x)/(gamma1 + x)',
	          },
                  pars={
		      'M' : 0.01,
		      'D' : 1.0,
		      'gamma1' : 33.6,
		      'C0' : 0.044, # C = 0.044
		      'D0' : 0.013,
	          },
                  ics={
		      'x' : 0.5,
		      'p' : 1.0,
	          },
                  fnspecs={'shs':(['sig','summation'],'1/(1+e^(-sig*summation))')},
                  tdata=[0,10])

DS = dst.Vode_ODEsystem(DSargs)
p = DS.compute('test').sample()
