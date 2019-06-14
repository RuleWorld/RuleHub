% Set path
addpath('~/d2d/d2d/arFramework3')

% Load models & data
arInit;
arLoadModel('ModelHistoneZheng');
arLoadData('MethylationData_aggregated_NTKO');
arCompileAll;

arFindInputs;
arSteadyState(1,1,1,-1e7)
arFit
% arLoadPars('bestFit')
arPrint
arPlot
