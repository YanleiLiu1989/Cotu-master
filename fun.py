import os,sys
import argparse
workDir = os.getcwd()
# filelist = sys.argv[1].strip()
parser = argparse.ArgumentParser(prog="fun.py",description="This is a script for generating Cotu directly from an original fastq file",usage="python %(prog)s [options]")
parser.add_argument("--copy_number","-cn",type=int,default=1,help="This parameter is used for copy number of sequences")
parser.add_argument("--seq_number","-s",type=int,default=None,help="This parameter is used for limiting the number of sequences in sequence alignment")
parser.add_argument("--filelist",required=True,type=str,help="Fastq files list for Cotu generation")
argv = vars(parser.parse_args())
if int(argv["copy_number"]) > 1:
	Type = "Multi"
else:
	Type = "Single"
os.system("dir/b *.fastq > list.txt")
os.mkdir("result")
if argv["filelist"] == None:
	sys.exit("please input the list file")
else:
	filelist = argv["filelist"].strip()
filelistOpen = open(filelist,"r")
for each in filelistOpen:
	os.chdir("result")
	each = each.strip().split(".")[0]
	os.system("..\\vsearch.exe  -cluster_size {work}\{each}.fastq -id 0.98 -clusterout_sort -strand both -consout {each}.fastq_cons".format(work=workDir,each=each))
	os.system("python ..\chaifen1.py {each}.fastq_cons {copy_number}".format(each=each,copy_number=argv["copy_number"])) ###extract top1
	for i in range(0,argv["copy_number"]):
		os.system("..\\usearch.exe -otutab {work}\{each}.fastq -otus {each}.fastq_cons_top_copy{i} -id 0.8 -strand both -matched {each}_matched_copy{i}.fasta".format(each= each,work=workDir,i=i+1))
		if argv["seq_number"] != None:
			number = argv["seq_number"]
			os.system("python ..\chaifen.py {each}_matched_copy{i}.fasta {number}".format(each=each,number=number,i=i+1))
			os.system("..\mafft --reorder --adjustdirection --globalpair --maxiterate 100 --thread -4 {each}_matched_copy{i}.deal.fasta > {each}_matched_copy{i}.fasta.fas".format(each=each,i=i+1))
		else:
			os.system("..\mafft --reorder --adjustdirection --globalpair --maxiterate 100 --thread -4 {each}_matched_copy{i}.fasta > {each}_matched_copy{i}.fasta.fas".format(each=each,i=i+1))
		os.system("python ..\Cotu-generator.py -i {each}_matched_copy{i}.fasta.fas -d 5 -id1 0.2 -id2 0.5 -o {each} -t {type} -cp {i}".format(each=each,i=i+1,type=Type))
	os.chdir("..")
