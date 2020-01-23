from . import ureg, Q_


def si(v):
    try:
        return v.to_base_units().magnitude
    except:
        try:
            return [si(vv) for vv in v]
        except:
            raise RuntimeError('Conversion to SI has failed')

def mach_correction(Ma=0.0):
    """Performs the Prandtl-Glauert compressibility correction."""

    #my own correction:
    beta = max(np.sqrt(abs(1-Ma**2)), np.sqrt(1-0.8**2))

    return 1/beta

    #Follows the formulation of eqn. 55-57 of Box:
    #if Ma < 0.8:
    #    return 1/np.sqrt(1-Ma**2)
    #elif Ma > 1.1:
    #    return 1/np.sqrt(Ma**2-1)
    #else:
    #    return 1/np.sqrt(1-0.8**2)
