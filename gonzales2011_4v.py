import PyDSTool as dst

DSargs = dst.args(name='test',
                  varspecs={
		      'r' : 'A*(1-r)/(gamma1 + 1 - r) - (B*z*r)/(gamma1 + r)',
		      'z' : 'N*(x^2  - z)',
		      'p' : 'M*(x^2 - p)',
		      'x' : 'C + G*r - D0*x - (D*p*x)/(gamma0 + x)',
	          },
                  pars={
		      'A' : 1.45,
		      'gamma1' : 0.0004,
		      'N' : 0.032,
		      'C' : 0.044,
		      'D0' : 0.013,
		      'M' : 0.01,
		      'D' : 1.0,
		      'gamma0' : 33.6,
		      'B' : 0.0051,
		      'G' : 1.0,
	          },
                  ics={
		      'r' : 1.0,
		      'z' : 0.1,
		      'p' : 0.1,
		      'x' : 1.0,
	          },
                  tdata=[0,100])

DS = dst.Vode_ODEsystem(DSargs)
