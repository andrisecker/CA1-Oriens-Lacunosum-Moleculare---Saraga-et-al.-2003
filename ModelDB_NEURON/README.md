### Original NEURON scripts for model

Authors summary:

It is well known that interneurons are heterogeneous in their morphologies, biophysical properties, pharmacological sensitivities and electrophysiological responses, but it is unknown how best to understand this diversity. Given their critical roles in shaping brain output, it is important to try to understand the functionality of their computational characteristics. To do this, we focus on specific interneuron subtypes. In particular, it has recently been shown that long-term potentiation is induced specifically on oriens-lacunosum/moleculare (O-LM) interneurons in hippocampus CA1 and that the same cells contain the highest density of dendritic sodium and potassium conductances measured to date. We create multi-compartment models of an O-LM hippocampal interneuron using passive properties, channel kinetics, densities and distributions specific to this cell type, and explore its signaling characteristics. We find that spike initiation depends on both location and amount of input, as well as the intrinsic properties of the interneuron. Distal synaptic input always produces strong back-propagating spikes whereas proximal input could produce both forward and back-propagating spikes depending on the input strength. We speculate that the highly active dendrites of these interneurons endow them with a specialized function within the hippocampal circuitry by allowing them to regulate direct and indirect signaling pathways within the hippocampus.

Fernanda.Saraga@UToronto.ca

To run the scripts, [install NEURON](https://www.neuron.yale.edu/neuron/download) and run:

    git clone https://github.com/andrisecker/CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003.git # clone git repository
    cd CA1-Oriens-Lacunosum-Moleculare---Saraga-et-al.-2003/NEURON
    nrnivmodl  # compile .mod files
    nrngui mosinit.hoc  # runs a simulation
    select a figure by clicking on a figure name

> Note from the ModelDB administrator: A bug noted by Mohamed Sherif and fix provided by Ted Carnevale updates the IA.mod file so that the a,b states change.
