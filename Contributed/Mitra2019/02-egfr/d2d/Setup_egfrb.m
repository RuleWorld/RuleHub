% Set path
addpath('~/d2d/d2d/arFramework3')

% Load models & data
arInit;
arLoadModel('egfr');
arLoadData('egfrData');
arCompileAll;

% set parameters for parameter estimation and optimization
% Use bigger range than in BNF job so I don't have to figure out how to set param bounds individually
ar.lb(:)   = -8;
ar.ub(:)   = 1;
% Use these incantations the same as Boehm
ar.config.atol = 1e-8;
ar.config.rtol = 1e-8;
ar.config.optim.TolFun = 1e-8;
ar.config.optim.TolX = 1e-8;
ar.config.maxsteps = 1e5;

% set constant parameters by analogy to Boehm
arSetPars('egf_tot',1.2e6, 0, 0);
arSetPars('egfr_tot',1.8e5, 0, 0);
arSetPars('Grb2_tot',1.0e5, 0, 0);
arSetPars('Shc_tot',2.7e5, 0, 0);
arSetPars('Sos_tot',1.3e4, 0, 0);
arSetPars('Grb2_Sos_tot',4.9e4, 0, 0);

arFit
% arLoadPars('bestFit')
arPrint
arPlot
