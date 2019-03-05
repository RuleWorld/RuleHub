## Name
Mitra2019

## Description
This folder contains 31 example fitting problems configured for PyBioNetFit. 

## Files
* [problems.xls](problems.xls) - Summary of all included fitting problems

Each folder contains files associated with one fitting problem, including a README.rtf describing the problem and methods. README.rtf files should be viewed offline in a word processor. The folder includes all model (.bngl / .xml) and data (.exp / .prop) files, and one configuration (.conf) file for each algorithm run on that problem. It also contains example output (best fit parameters and model file) for each algorithm.

Additional analysis was done on some of the examples. Such analysis is noted in problems.xls.

## Notes

This folder will be included as Supplementary Information in Mitra, Suderman, et al. "PyBioNetFit and the Biological Property Specification Language" (in preparation). 

PyBioNetFit is available at <http://github.com/lanl/pybnf>.

## Technical information

In most cases, fitting was run using PyBioNetFit v0.2.2 with four algorithms on default settings: differential evolution, asynchronous differential evolution, particle swarm, and scatter search. Fitting was run until a target objective was reached, with the target determined from a known ground truth (if data was synthetic), or from a previously reported fit for the problem. Any differences from this procedure are noted in the individual README files. 
