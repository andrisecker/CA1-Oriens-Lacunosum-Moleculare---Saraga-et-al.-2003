## CA1 Oriens Lacunosum Moleculare Saraga et al. 2003

Model from: Active Dendrites and Spike Propagation in Multi-compartment Models of Oriens-Lacunosum/Moleculare Hippocampal Interneurons. Saraga F, Wu CP, Zhang L, Skinner FK (2003) [J Physiol 552(3):673-689](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2343469/pdf/tjp0552-0673.pdf)

### NEURON version of model:

This model was originally developed in [NEURON](https://www.neuron.yale.edu/neuron/)

More details on the original NEURON version of this model [here](https://github.com/andrisecker/Saraga2003-CA1-OLM/tree/master/ModelDB_NEURON) (The repository was forked from @agmccrei).

-------------------------------------------------------------------------------------------------------------------------------

### NeuroML2/LEMS version of model

The model has been converted to NeuroML2/LEMS:

More details on the NeuroML2/LEMS version of this model [here](![](https://raw.githubusercontent.com/andrisecker/Saraga2003-CA1-OLM/master/NeuroML2/compre.png)).

The NeuroML2 support is not 100%...
we still have an issue with the m gate variable of the Na+ channels ([.mod file](https://github.com/andrisecker/Saraga2003-CA1-OLM/blob/master/NEURON/Nadend.mod), [.channel.nml file](https://github.com/andrisecker/Saraga2003-CA1-OLM/blob/master/NeuroML2/Nadend.channel.nml)) which is set to the inf value in the original files!

> See the comparison with a short(0.1ms) large(10nA) somatic input (as Fig8 B, right; in the [original paper](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2343469/pdf/tjp0552-0673.pdf)): top NEURON implementation, bottom: NeuroML2 implementation. (black curve - voltage at the soma)

![](https://raw.githubusercontent.com/andrisecker/Saraga2003-CA1-OLM/master/NeuroML2/compre.png)

-------------------------------------------------------------------------------------------------------------------------------

[![Build Status](https://travis-ci.org/andrisecker/CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003.svg?branch=master)](https://travis-ci.org/andrisecker/CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003)
