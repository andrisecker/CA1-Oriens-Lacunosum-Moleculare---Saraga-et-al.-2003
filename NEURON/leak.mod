TITLE passive membrane channel
                                                                                
UNITS {
        (mV) = (millivolt)
        (mA) = (milliamp)
}
                                                                                
NEURON {
        SUFFIX leak
        NONSPECIFIC_CURRENT i
        RANGE gl, el, i
}
                                                                                
PARAMETER {
	    v		      (mV)
        gl = .00005   (mho/cm2)
        el = -70      (mV)
}
                                                                                
ASSIGNED {
        i (mA/cm2)
}
                                                                                
BREAKPOINT {
        i = gl*(v - el)
}

