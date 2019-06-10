import numpy as np

def postprocess(simdata):
    # Normalize these columns by the max value within the time range [0,1000] (first 200 time points)
    for col in ('G_act','membrane_Ste5'):   
        g_data = simdata[col]
        peak = np.max(g_data[:200])
        g_data /= peak
        simdata[col] = g_data
    
    # Normalize ste20_bound_ste4 to the value at t=2745
    # which seems to be what the paper did.
    ste_ref = simdata['ste20_bound_ste4'][549]
    simdata['ste20_bound_ste4'] /= ste_ref
    
    return simdata
