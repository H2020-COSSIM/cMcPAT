# cMcPAT - COSSIM-modified McPAT version. 

This repository includes the modified version of McPAT that is employed in the COSSIM simulation framework. It should be noted that cMcPAT can be used independently of COSSIM as a standalone package incorporating all the changes that have been integrated to the official McpAT v1.3 release.


## Differences between cMcPAT and official McPAT v1.3

### simpleCPU models of gem5

McPAT is developed with certain processor types under consideration. As such it makes a number of assumptions about the presence, size and functioning of different processor components that may not be used in systems using simpleCPU models in gem5. For example, for simpleCPU models, gem5 does not model or report several (micro)architectural structures that are typically found in a processor and therefore the output configuration files (config) do not provide enough information for McPAT. Additionally, by not employing certain structures or using structures with very small sizes, McPAT either reports errors or crashes in such cases.

cMcPAT is modified to handle those cases. On top of that, it adds two Processor Description templates that can be used when trying to model ARM and x86 simpleCPU models from gem5. 

### Improving the accuracy of McPAT

A number of changes have been made to technology specific parameters. The following table summarizes the differences made to the technology.cc file of the cacti component for the Empirical undifferentiated core / FU coefficient :

Technology Node | McPAT v1.3 | cMcPAT
------------ | ------------- | -------------
180nm | 1.5 | 1.0/1.5
90nm | 1 | 1.0/(0.7 * 0.7)
65nm | 0.7 | 1.0/0.7
45nm | 0.7 * 0.7 | 1
32nm | 0.7 * 0.7 * 0.7 | 0.7
22nm | 0.7 * 0.7 * 0.7 * 0.7 | 0.7 * 0.7
16nm | 0.7 * 0.7 * 0.7 * 0.7 * 0.7 | 0.7 * 0.7 *0.7

These changes have been proposed in the paper: 

Xi, Sam Likun, Hans Jacobson, Pradip Bose, Gu-Yeon Wei, and David Brooks. _"Quantifying sources of error in McPAT and potential impacts on architectural studies."_ In 2015 IEEE 21st International Symposium on High Performance Computer Architecture (HPCA), pp. 577-589. IEEE, 2015. 

To validate their effect, cMcPAT has been run against the number reported in the official paper of McPAT (S. Li, J.-H. Ahn,_"McPAT: An integrated power, area, and timing modeling framework for multicore and manycore architectures"_, in Microarchitecture, 2009. MICRO-42. 42nd Annual IEEE/ACM International Symposium on, (pp. 469–480)) using the templates provided in the v1.3 release of McPAT. The table below summarizes the effect of the changes

Processor | Published total power and area | McPAT v1.3 Results | cMcPAT Results | Estimation Improvement (negative numbers indicate a worse result by the cMcPAT)
------------ | ------------- | ------------- | ------------- | -------------
Niagara | 63W / 378mm<sup>2</sup> | 52.59W / 269.70mm<sup>2</sup> | 56.91W / 302.53mm<sup>2</sup> | **41,5%** / **30,3%**
Niagara 2 | 84W / 342mm<sup>2</sup> | 72.97W / 262.51mm<sup>2</sup> | 76.54W / 279.01mm<sup>2</sup> | **32,3%** / **20,8%**
Alpha 21364 | 125W / 396mm<sup>2</sup> | 86.03W / 311.69mm<sup>2</sup> | 85.86W / 299.4mm<sup>2</sup> | -0,4% / -14,6%
Xeon Tulsa | 150W / 435mm<sup>2</sup> | 134.94W / 411mm<sup>2</sup> | 146.33W / 432mm<sup>2</sup> |**75,6%** / **87,5%**
Cortex A9 | 1.9W / 6.7mm<sup>2</sup> | 1.74W / 5.40mm<sup>2</sup> | 1.79W / 5.96mm<sup>2</sup> | **31,3%** / **43,1%**

## Compiling and executing cMcPAT

Please read the [README](mcpat/README) file included in the mcpat folder.

## Using gem5 statistics and configuration files to make proper cMcPAT inputs

Please check the GEM5toMcPAT script included in the Scripts folder.

## Energy Reporting

Please check the print_energy script included in the Scripts folder.

## Using cMcPAT in the context of the COSSIM simulation framework

Please refer to [COSSIM _framework](https://github.com/H2020-COSSIM/COSSIM_framework) repository for all required instructions.

## Licensing

Refer to the [LICENSE](LICENSE) and [COPYING](COPYING.md) files included. Individual license may be present in different files in the source codes.

#### Authors

* Andreas Brokalakis (brokalakis@synelixis.com)

Please contact for any questions.

## Acknowledgments

Code developed for the H2020-COSSIM project.

