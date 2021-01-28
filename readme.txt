please ensure that python3.7 or upper version is installed.
please download mafft for windows and unzip to the Cotu-master folder or you can use the version I privide, Don't forget to cite mafft if you use them for your data
please download usearch.exe and vsearch.exe or you can use the version I privide, Don't forget to cite these two softwares if you use them for your data.
This version just suitable for windows 64 bite operating system.
dir/b *.fastq > list.txt
### generate the list.txt file 

python fun.py --filelist list.txt --seq_number 500
###run the Cotu-master to generate Cotu for the sample in the list.txt with the sequence number limited to 500.

python fun.py --filelist list.txt
###run the Cotu-master to generate Cotu for the sample in the list.txt without the sequence number limitation.

python Cotu-generator.py -i alignment-file-name.fasta.fas -d 5 -id1 0.2 -id2 0.5
###just generate Cotu sequence for the input alignment fasta file.