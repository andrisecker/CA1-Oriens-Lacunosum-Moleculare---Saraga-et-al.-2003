from pyneuroml.neuron import export_to_neuroml2
from pyneuroml.neuron.nrn_export_utils import clear_neuron

export_to_neuroml2("../NEURON/SaragaOLM_Case2.hoc", "SaragaOLM_Case2.nml", includeBiophysicalProperties=True)

