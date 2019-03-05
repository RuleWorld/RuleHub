import re

def net2d2d(netfilename, deffilename):
    
    params = dict() # Maps index to (name, initialization)
    reactions = dict() # Maps index to ((reactants), (products), rateconstant)
    species = dict() # Maps index to (name, initialization)
    groups = dict() # Maps index to (name, (matches))
    
    # Read the net file and put the information into Python data structures. 
    with open(netfilename) as f:
        
        
        insection = None
        for line in f:
            line = line.strip()
            
            # Check for "begin" and "end" statements
            m = re.match('begin\s+([a-z]+)',line)
            if m and insection is None:
                insection = m.groups()[0]
                continue
            if re.match('end\s+%s' % insection, line):
                insection = None
                continue
            
            # Add this line to appropriate data structure
            parts = line.split()
            if insection == 'parameters':
                params[int(parts[0])] = (parts[1], parts[2])
            elif insection == 'species':
                species[int(parts[0])] = (parts[1], parts[2])
            elif insection == 'reactions':
                reactions[int(parts[0])] = (tuple([int(x) for x in parts[1].split(',')]), tuple([int(x) for x in parts[2].split(',')]), parts[3])
            elif insection == 'groups':
                groups[int(parts[0])] = (parts[1], tuple(parts[2].split(',')))
            
            
    # Create the corresponding d2d file
    with open(deffilename,'w') as out:
        
        # Write states (species)
        out.write('STATES\n')
        for i in species:
            # just name the species "sp###"
            out.write('sp%i\tC\t"nM"\t"conc."\n' % i)
            
        # Unused section
        out.write('\n\nINPUTS\n')
            
        # Write the reactions
        out.write('\n\nREACTIONS\n')
        for i in reactions:
            react,prod,rate = reactions[i]
            
            # the d2d rate has the reactant(s) explicitly listed
            # TODO support empty reactant and products
            d2drate = '%s*%s' % ('*'.join(['sp%i' % j for j in react]), rate)
            out.write('%s -> %s CUSTOM "%s"\n' % (' + '.join(['sp%i' % j for j in react]), ' + '.join(['sp%i' % j for j in prod]), d2drate))
       
        #Unused section
        out.write('\n\nDERIVED\n')
           
        # Write the observables
        out.write('\n\nOBSERVABLES\n')
        for i in groups:
            # Turn the expressions that could be something like 2*49 into 2*sp49
            formula = '+'.join([re.sub('(\d+)$',r'sp\1',m) for m in groups[i][1]])
            out.write('%s_obs\tC\t"au"\t"conc."\t0\t0\t"%s"\n' % (groups[i][0], formula))
        
        # Not yet sure how this works, but crashes if left blank
        # Copy the format from the Zheng example and hope for the best. 
        out.write('\n\nERRORS\n')
        for i in groups:
            out.write('%s_obs  "%s_std"\n' % (groups[i][0],groups[i][0]))
        
        # Write the initial conditions
        out.write('\n\nCONDITIONS\n')
        for i in species:
            out.write('init_sp%i\t"%s"\n' % (i, species[i][1]))
