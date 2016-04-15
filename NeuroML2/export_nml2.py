from pyneuroml.neuron import export_to_neuroml2
from pyneuroml.neuron.nrn_export_utils import clear_neuron

export_to_neuroml2("../NEURON/tester_Case2.hoc", 
                   "SaragaOLM_Case2.cell.nml", 
                   includeBiophysicalProperties=True,
                   known_rev_potentials={'IA':-100, 'Ih':-32.9})

