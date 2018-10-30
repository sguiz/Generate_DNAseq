# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:53:26 2017

@author: sarahguiziou
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:34:13 2016

@author: sarahguiziou
"""

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqFeature import SeqFeature, FeatureLocation
import string
import pandas as pd

__author__  = 'Sarah Guiziou <guiziou@cbs.cnrs.fr>'
__license__ = 'MIT'
__version__ = '1.0'
    
"""
CREATE DICO SEQ

Extracte from a csv file, a dictionnary of DNA sequences.

"""    
    
def create_dico_seq(name_file):

    list_seq=pd.read_csv(name_file, sep=";",usecols=[0,1], names=['name','seq'])
    dico_seq={}
    
    for X in range(0,len(list_seq)):
        dico_seq[list_seq['name'][X]]=list_seq['seq'][X]
    
    return dico_seq

"""
GB CREATE

From the sequence list (composed of the DNA seq, name and orientation)
Generation of a gb file

"""

def gb_create(sequence, name, directory):

    # initialization of the DNA sequence
    DNA_seq=''
    
    # loop in sequence list to generate the string corresponding to the DNA sequence of the device.
    for seq in sequence:
        DNA_seq+=seq[0]

    # creation of the formated DNA sequence for the genbank file
    seq_final=Seq(DNA_seq, IUPAC.unambiguous_dna)
    record = SeqRecord(seq_final,
                   id='NA', # random accession number
                   name=name,
                   description='Synthetic sequence')
    
    # initialization of the variable len_seq 
    len_seq=0
    
    # loop in sequence list to generate the genbank feature of the sequence
    for feat in sequence:
        
        feature = SeqFeature(FeatureLocation(start=len_seq, end=len_seq+len(feat[0])), id=feat[1], type=feat[1], strand=feat[2])
        record.features.append(feature)
        len_seq+=len(feat[0]) 

    # Save as GenBank file
    output_file = open(directory+'/'+name+'.gb', 'w')
    SeqIO.write(record, output_file, 'genbank')
    output_file.close()

"""
DESIGN DNA SEQUENCE

Inputs:
1. Input file (csv file)
2. Output directory: where to save the generated DNA sequences
3. Dico_file: file with list of DNA sequences
4. Number_seq: number of sequences for generation
From the sequence list (composed of the DNA seq, name and orientation)
Generation of a gb file

"""

def design_DNAsequence(input_file, output_directory, dico_file, number_seq):
    
    # To reverse complement sequences
    old_chars = "ACGTacgt"
    replace_chars = "TGCAtgca"
    tab = string.maketrans(old_chars,replace_chars)  
    
    dico=create_dico_seq(dico_file)
    col_nb=[]
    col_name=[]
    
    for col in range(0, number_seq*2):
        col_nb.append(col)
        
    for seq in range(0, number_seq):
        col_name.append('seq'+str(seq+1))
        col_name.append('or'+str(seq+1))
    
    input_seq=pd.read_csv(input_file, sep=";", usecols=col_nb, names=col_name)
   
    for seq in range(1, number_seq+1):
        sequence=[]

        for X in range(1, len(input_seq['seq'+str(seq)])):
            if input_seq['seq'+str(seq)][X]!=input_seq['seq'+str(seq)][X]:
                break
            else:
                DNA_name=input_seq['seq'+str(seq)][X]
                OR=input_seq['or'+str(seq)][X]
                
                if OR=='-1':
                    DNA=dico[DNA_name].translate(tab)[::-1]
                    OR=-1
                else:
                    DNA=dico[DNA_name]
                    OR=+1
                    
                sequence.append([DNA, DNA_name, OR])
                
        gb_create(sequence, input_seq['seq'+str(seq)][0], output_directory)

   
"""TEST of the design DNA function"""    
"""DESIGN DNA SEQUENCE

Inputs:
1. Input file (csv file)
2. Output directory: where to save the generated DNA sequences
3. Dico_file: file with list of DNA sequences
4. Number_seq: number of sequences for generation
From the sequence list (composed of the DNA seq, name and orientation)
Generation of a gb file"""

#design_DNAsequence('Example.csv', '/Users/sarahguiziou/Desktop/generation_seq/results', 'List_seq.csv', 12)
