# Cotu-master
please ensure that python3.7 or upper version is installed.
please download mafft for windows and unzip to the Cotu-master folder or you can use the version I privided, Don't forget cite mafft if you use them for your data.
please download usearch.exe and vsearch.exe or you can use the version I privided, Don't forget cite these two software if you use them for your data

dir/b *.fastq > list.txt
### generate the list.txt file 

python fun.py --filelist list.txt --seq_number 500
###run the Cotu-master to generate Cotu for the sample in the list.txt with the sequence number limited to 500.

python fun.py --filelist list.txt
###run the Cotu-master to generate Cotu for the sample in the list.txt without the sequence number limitation.

python Cotu-generator.py -i alignment-file-name.fasta.fas -r 50 -l 50 -d 5 -id1 0.2 -id2 0.5
###just generate Cotu sequence for the input alignment fasta file.
-i: input file.
-l: Number of alignment bases using id1 stragegy from the left.
-r: Number of alignment bases using id1 stragegy from the right.
-d: The minimum sequencing depth,sample with sequencing depth lower than 5 will be dropt.
-id1: The first sequencing depth strategy,in a certain region of two ends, base number counted larger than the parameter given will ignore gaps and conducted the majority for consensus generation.
-id2: The second sequencing depth strategy,in a certain region of the middle, base number counted larger than the parameter given will ignore gaps and conducted the majority for consensus generation. If not, a gap will be produced in the certain position.
