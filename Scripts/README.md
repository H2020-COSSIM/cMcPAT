# cMcPAT - Scripts 

## cGEM5 to cMcPAT convertion script

The GEM5ToMcPAT.py conversion script uses the output files of cgem5 (gem5 stats and config files) in order to create an .xml file that can be used as input to cMcPAT. In order for the script to work a template .xml file providing a description of the processor is also required. 

The script can be used with the generic versions of gem5 and McPAT (available from the official gem5 and McPAT repositories).
It should be noted that the script works with the following versions of gem5 and McPAT:
- cgem5 and cMcPAT
- McPAT v1.3
- gem5 March 2022 release (v21.2.1).

The GEM5toMcPAT.py is attributed to Daya Khudia's [GEM5toMcPAT](https://bitbucket.org/dskhudia/gem5tomcpat) tool. However a series of changes have been made to address the following:

- proper handling of 'nan' cases
- certain errors appeared when using "atomic simple" cpu models in gem5
- the original tool does not account for the changes made in recent versions of gem5 (stats.txt and config.json have new fields or different entries). As such it would crash without producing proper output. Changes made in this version account for these modified stats.txt and config.json outputs of recent gem5 while taking steps to prevent the conversion script from crashing when more recent versions of gem5 break the standard form of these files.

All changes made by Andreas Brokalakis, Synelixis Solutions (brokalakis@synelixis.com)

### How to use the script

1. This is a python script. Make sure python is installed and change the permissions of the file to executable.

2. Usage:

```
GEM5toMcPAT.py [options] <gem5 stats file> <gem5 config file (json)> <mcpat template xml file> -o <output xml file>
```

3. Available options:

```
-h, --help	show help message and exit
-q, --quiet	don't print status messages to stdout
```


## cMcPAT print_energy script

By default McPAT reports power and not energy. The print_energy.py script performs a simple calculation of the energy consumed during an execution by combining the overall execution time as provided in the gem5 stats file and the average power consumed as provided by the output of McPAT.

The script can be used with the generic versions of gem5 and McPAT (available from the official gem5 and McPAT repositories).
It should be noted that the script works with the following versions of gem5 and McPAT:
- cgem5 and cMcPAT
- McPAT v1.3
- gem5 March 2022 release (v21.2.1)

The print_energy.py is a simplified version of Daya Khudia's [GEM5toMcPAT](https://bitbucket.org/dskhudia/gem5tomcpat) tool, incorporating all changes addressed in the GEM5toMcPAT.py available in this repository, in addition with a few enhancements to speed up the process.

### How to use the script

1. This is a python script. Make sure python is installed and change the permissions of the file to executable.

2. Usage:

```
print_energy.py [options] <mcpat output file> <gem5 stats file> 
```

3. Available options:

```
-h, --help	show help message and exit
```

## Authors

* Andreas Brokalakis (brokalakis@synelixis.com)

Please contact for any questions.

## Acknowledgments

Code developed for the H2020-COSSIM project.
