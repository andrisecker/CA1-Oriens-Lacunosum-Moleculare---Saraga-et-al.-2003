from pyneuroml.neuron import export_to_neuroml2
from pyneuroml.neuron.nrn_export_utils import clear_neuron

export_to_neuroml2("../NEURON/initFig9BCase2", "OLM_Fig9BCase2_morph.cell.nml", includeBiophysicalProperties=False)

'''
clear_neuron()
os.chdir('../NeuroML2')  

export_to_neuroml2("create_cell.hoc", "../NeuroML2/OLM_Fig9BCase2.cell.nml", includeBiophysicalProperties=True)
'''
