# Introduction of Cotu method:
In order to support accurate molecular identification of organisms by means of DNA barcoding, a reference library with high species coverage needs to be constructed as quick and cheap as possible. To reach this goal, high throughput sequencing platforms are indispensable to speed up the processes and lower the costs. In this study, we show that the Illumina Hiseq PE250 is currently the right platform for conventional DNA barcodes. 
Aiming to improve the accuracy and length of output consensus sequences, we developed the new Cotu method under the majority rule (the letter “C” stands for consensus, and Cotu means consensus-based OTU creation method). The major features of the Cotu method are elimination of insertions from occasional reads under majority rule and sequence length extensions at both ends of alignments. The qualities of the beginning and ending bases are usually low and frequently trimmed off, which causes uneven alignments. If the majority rule was used for this situation, shortened consensus sequences would likely be created. We, therefore, apply a threshold of bases on a site (e.g. 20%) to a certain region sequences from both ends (in order to reduce alignment with massive gaps, we firstly removed fake gaps with less than 10% of total base in a certain position which affected the determination of the parameter at the two ends. After fake gap removal, the region of doing majority with more than 20% base data will be determined by self-learning of our software with the principle of when three consecutive base position with more than 50% bases is appeared. If a site in the certain region of beginning and ending regions has the number of bases less than the threshold, the site is considered an incorrect insertion; if a site has bases of more than the threshold number, the site is considered normal and the majority rule is applied. For bases in the middle position, if gap taking more than 50%, this site will be considered as a real gap, otherwise, the position will generate final base based on majority of appeared bases (ignoring gaps).
# To Cotu Master uesrs:
This package is just suitable for 64 bite windows operating system.
Please ensure that python3.7 or upper version was installed.
Please download mafft for windows and unzip to the Cotu-master folder or you can use the version I provided. Don't forget cite mafft if you use it for your data analysis.
Please download usearch.exe and vsearch.exe or you can use the version I provided, Don't forget cite these two softwares if you use them for your data.
Please first open the Cotu Master folder and read readme.txt first.
# How to use Cotu-generator.py
Open cmd.exe, change to Cotu Master working folder and input:

python Cotu-generator.py –help

You will see information below:

useage: python Cotu-generator.py –i input_file [options] For example:

python Cotu-generator.py -i alignment-file.fasta -r 50 -l 50 -d 5 -id1 0.2 -id2 0.5

optional arguments:

-h, --help show this help message and exit

-i: input file.

-l: Number of alignment bases using id1 strategy from the 5’ end.

-r: Number of alignment bases using id1 strategy from the 3’ end.

-d: The minimum sequencing depth, sample with sequencing depth lower than 5 will be dropt.

-id1: The first sequencing depth strategy, in a certain region of two ends, base number counted larger than the parameter given will ignore gaps and conducted the majority for consensus generation.

-id2: The second sequencing depth strategy, in a certain region of the middle, base number counted larger than the parameter given will ignore gaps and conducted the majority for consensus generation. If not, a gap will be produced in the certain position.

Practical examples:
We provide a test data in the Cotu Master package. Three test data in fastq formation were provided.
Open the results folder and find BOP010001.fasta.fas and run the command below:

python Cotu-generator.py -i BOP010001.fasta.fas -r 50 -l 50 -d 5 -id1 0.2 -id2 0.5

###in the first 50 bp from the beginning and ending, 0.2 parameter will be used while in the middle region 0.5 parameter will be used for Cotu generation.

For users who want to generate Cotu for all fasta file in a folder, we provide a cycle command: Please copy Cotu-generator.py into the folder before you run the command.

for %i in (*.fas); do python Cotu-generator.py -i %i -r 50 -l 50 –d 10 –id1 0.2 –id2 0.5

###Run all alignment fasta files for Cotu sequence generation.

The consensus sequences are output as a fasta file for each sample. Document name, sequence length and sequence depth were included in the name of consensus sequence. 

# The purpose of Cotu Master:
In order to facilitate researchers who are not good at bioinformatics, we packaged the main Cotu generation steps together and named “Cotu Master” in the supporting information named (Supporting software.zip). Researcher can get final Cotu sequence directly from a demltiplexed fastq file (with only one gene and one species in the fastq file and without artificial sequences) by using just one simple commands.

# How to use Cotu Master:
Python script fun.py is written for combination of each core steps in Cotu generation. Open cmd.exe, change to Cotu Master working folder and input:

python Cotu-generator.py –help

You will see information below:

useage: python fun.py [options]

This is a script for generating Cotu directly from an original fastq file

-h, --help show this help message and exit

--copy_number COPY_NUMBER, -cn COPY_NUMBER

This parameter is used for copy number of sequences

--seq_number SEQ_NUMBER, -s SEQ_NUMBER

This parameter is used for limiting the number of sequences in sequence alignment

--filelist FILELITE	Fastq files list for Cotu generation

Practical examples:
We provide a test data in the Cotu Master package. Three test data in fastq formation were provided.
Run the Cotu-master to generate Cotu for the sample in the list.txt without the sequence number limitation in mafft alignment.

python fun.py --filelist list.txt

Run the Cotu-master to generate Cotu for the sample in the list.txt with the massive sequence number for mafft limited to 500.

python fun.py --filelist list.txt --seq_number 500

The results of test data were also provided, researchers can compare the results after you operate using test data.

Besides, the package used many softwares already written by other researchers like Usearch and Vsearch. All parameter of each original steps (parameters in former step5-step7) can be changed in the fun.py file according to different researchers’ needs following the command explanation in each software manual.

For Vsearch command manual, please visit https://github.com/torognes/vsearch

For Usearch command manual, please visit http://www.drive5.com/usearch/manual/

For Cotu-generator.py manual, please visit https://github.com/YanleiLiu1989/Cotu-master

