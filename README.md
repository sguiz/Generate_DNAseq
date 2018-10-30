# Generate_DNAseq
Short python script to automatically generate annotated genbank DNA sequence from an excel file with a list of DNA part sequences and an excel file with the information to generate various device sequences.

To use this script, you have to:
1 - Install the Bio package
2 - Download the short python script: Generate_DNA_seq.py 
3 - Create a CSV file with the list of your DNA part sequence of interest (an example of sequence list: List_seq.csv). This list should be composed of two columns, the first column for the name fo the part and the second for the DNA sequence, each row corresponding to a different part.
4 - Create a CSV file with the list of device (an example for the generation of the DNA sequences of two devices: Example.csv). This list should be composed of two times more columns than the number of sequences to generate, indeed each device requires two columns: one column for the list of DNA part and a second one for their orientations. For each device, place in the first row and in two columns the name of the device, then place the name and orientation of each part of the device sequentially from 5' to 3' end of the device. For the orientation, 1 corresponds to forward and -1 to reverse.
5 - To generate the varous sequences, use the last line of the code which is for now commented (remove the # in front of the line). 
You have to change the argument of the function design_DNAsequence, 1: CSV file corresponding to devices that you want to generate, 2: your directory, where do you want to save the gb files, 3: the list of sequences, 4: the number of devices.

As example: 
`design_DNAsequence('Example.csv', 'Your_directory', 'List_seq.csv', 2)`
