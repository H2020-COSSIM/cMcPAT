#!/usr/bin/python
import sys
import re
import os
import json
import types
import math
import subprocess as subp
from optparse import OptionParser


mcpat_bin = "mcpat"

class parse_node:
    def __init__(this,key=None,value=None,indent=0):
        this.key = key
        this.value = value
        this.indent = indent
        this.leaves = []
    
    def append(this,n):
        #print 'adding parse_node: ' + str(n) + ' to ' + this.__str__() 
        this.leaves.append(n)

    def get_tree(this,indent):
        padding = ' '*indent*2
        me = padding + this.__str__()
        kids = list(map(lambda x: x.get_tree(indent+1), this.leaves))
        return me + '\n' + ''.join(kids)
        
    def getValue(this,key_list):
        #print 'key_list: ' + str(key_list)
        if (this.key == key_list[0]):
            #print 'success'
            if len(key_list) == 1:
                return this.value
            else:
                kids = list(map(lambda x: x.getValue(key_list[1:]), this.leaves))
                #print 'kids: ' + str(kids) 
                return ''.join(kids)
        return ''        
        
    def __str__(this):
        return 'k: ' + str(this.key) + ' v: ' + str(this.value)

class parser:

    def dprint(this,astr):
        if this.debug:
            print (this.name, astr)

    def __init__(this, data_in):
        this.debug = False
        this.name = 'mcpat:mcpat_parse'
        
        buf = open(data_in)
      
        this.root = parse_node('root',None,-1)
        trunk = [this.root]

        for line in buf:
            	   
            indent = len(line) - len(line.lstrip())
            equal = '=' in line
            colon = ':' in line
            useless = not equal and not colon
            items = list(map(lambda x: x.strip(), line.split('=')))

            branch = trunk[-1]

            if useless: 
                #this.dprint('useless')
                pass 

            elif equal:
                assert(len(items) > 1)

                n = parse_node(key=items[0],value=items[1],indent=indent)
                branch.append(n)

                this.dprint('new parse_node: ' + str(n) )

            else:
                
                while ( indent <= branch.indent):
                    this.dprint('poping branch: i: '+str(indent) +\
                                    ' r: '+ str(branch.indent))
                    trunk.pop()
                    branch = trunk[-1]
                
                this.dprint('adding new leaf to ' + str(branch))
                n = parse_node(key=items[0],value=None,indent=indent)
                branch.append(n)
                trunk.append(n)
                
        
    def get_tree(this):
        return this.root.get_tree(0)

    def getValue(this,key_list):
        value = this.root.getValue(['root']+key_list) 
        assert(value != '')
        return value

#runs McPAT and gives you the total energy in mJs
def main():
    global opts
    usage = "usage: %prog [options] <mcpat output file> <gem5 stats file>"
    parser = OptionParser(usage=usage)
    parser.add_option("-q", "--quiet", 
        action="store_false", dest="verbose", default=True,
        help="don't print status messages to stdout")
    
    (opts, args) = parser.parse_args()
    if len(args) != 2:
        parser.print_help()
        sys.exit(1)
   
    energy = getEnergy(args[0], args[1])
    print ("energy is %f mJ" % energy)
    

def getEnergy(mcpatoutputFile, statsFile):
    leakage, dynamic = readMcPAT(mcpatoutputFile)
    runtime = getTimefromStats(statsFile)
    energy = (leakage + dynamic)*runtime
    print ("leakage: %f W, dynamic: %f W and runtime: %f sec" % (leakage, dynamic, runtime))
    return energy*1000

def readMcPAT(mcpatoutputFile):
    
    print ("Reading simulation time from: %s" %  mcpatoutputFile)
    p = parser(mcpatoutputFile)
    
    leakage = p.getValue(['Processor:', 'Total Leakage'])
    dynamic = p.getValue(['Processor:', 'Runtime Dynamic'])
    leakage = re.sub(' W','', leakage) 
    dynamic = re.sub(' W','', dynamic) 
    return (float(leakage), float(dynamic))
    

def getTimefromStats(statsFile):
    if opts.verbose: print ("Reading simulation time from: %s" %  statsFile)
    F = open(statsFile)
    ignores = re.compile(r'^---|^$')
    statLine = re.compile(r'([a-zA-Z0-9_\.:+-]+)\s+([-+]?[0-9]+\.[0-9]+|[0-9]+|nan)')
    retVal = None
    for line in F:
        #ignore empty lines and lines starting with "---"  
        if not ignores.match(line):
            statKind = statLine.match(line).group(1)
            statValue = statLine.match(line).group(2)
            if statKind == 'simSeconds':
                retVal = float(statValue)
                break	#no need to parse the whole file once the requested value has been found
    F.close()
    return retVal


if __name__ == '__main__':
    main()
