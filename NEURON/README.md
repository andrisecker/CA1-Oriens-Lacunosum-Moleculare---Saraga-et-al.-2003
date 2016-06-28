### NEURON scripts for model

This folder contains files from the original model scripts [ModelDB:28316](https://senselab.med.yale.edu/ModelDB/showModel.cshtml?model=28316) and additional tester scripts (in order to create a .mep file, which against LEMS/NeuroML2 implementation could be tested).

Issues fixed:
- we corrected the initialisation of the gate variables of the (Na+, K+) channels 

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/andrisecker/CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003.git  # clone git repository
    cd CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003/NEURON
    nrnivmodl  # compile .mod files
    nrngui tester_Case2.hoc  # runs a simulation (single cell, current clamp) and saves data into saragaolm.dat

![](https://raw.githubusercontent.com/andrisecker/CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003/master/NEURON/saraga2003olm.png)
