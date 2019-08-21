## Name
Mitra2019Likelihood

## Description
A series of parallel tempering jobs designed to illustrate the use of qualitative data as part of Bayesian uncertainty quantification.

The original model of IgE-mediated degranulation in mast cells is published in:

Harmon, B., Chylek, L.A., Liu, Y., Mitra, E.D., Mahajan, A., Saada, E.A., Schudel, B.R., Holowka, D.A., Baird, B.A., Wilson, B.S., Hlavacek, W.S., Singh, A.K., 2017. Timescale separation of positive and negative signaling creates history-dependent responses to IgE receptor stimulation. Scientific Reports 7, 15586. https://doi.org/10.1038/s41598-017-15568-2

Here, synthetic data was generated, taking the published parameterization as the ground truth, and the synthetic data was used in parallel tempering runs in PyBioNetFit. Each subdirectory contains configuration of a parallel tempering run using a different amount of qualitative data (or quantitative data in the case of ``problem_quant``). The series of runs illustrates that with a large amount of purely qualitative data, it is possible to find nontrivial quantitative confidence intervals on parameter values. 

## Files
* [model_ground.bngl](model_ground.bngl) - Model with ground truth parameters
* [problem4](problem4) - Files needed to run parallel tempering in PyBioNetFit, in which the data consists of 4 qualitative measurements, each with two possible outcomes (the secondary degranulation is less than or greater than the primary degranulation)
* [problem8](problem8) - Files for 8 qualitative measurements
* [problem16](problem16) - Files for 16 qualitative measurements
* [problem32](problem32) - Files for 32 qualitative measurements
* [problem64](problem64) - Files for 64 qualitative measurements
* [problem4_3cat](problem4_3cat) - Files for 4 qualitative measurements in which each measurement has three possible outcomes (the secondary degranulation is less than, greater than, or within error of the primary degranulation)
* [problem8_3cat](problem8_3cat) - Files for 8 three-category qualitative measurements
* [problem16_3cat](problem16_3cat) - Files for 16 three-category qualitative measurements
* [problem32_3cat](problem32_3cat) - Files for 32 three-category qualitative measurements
* [problem64_3cat](problem64_3cat) - Files for 64 three-category qualitative measurements


## Notes

All data in this set of examples is synthetic, generated from the provided ground truth model. Added error is Gaussian with a standard deviation of 7e3. For qualitative data, the inequalities were written based on the quantitative outputs with added error of the ground truth model.
