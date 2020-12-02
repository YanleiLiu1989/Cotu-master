import os,sys
import argparse
workDir = os.getcwd()
# filelist = sys.argv[1].strip()
parser = argparse.ArgumentParser(prog="fun.py",description="This is a script for practice",usage="python %(prog)s [optional]")
parser.add_argument("--seq_number","-s",type=int,default=None,help="This parameter is used for limiting the number of sequences")
parser.add_argument("--filelist",required=True,type=str,help="Fastq files list")
argv = vars(parser.parse_args())
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
	os.system("python ..\chaifen1.py {each}.fastq_cons 1".format(each=each)) ###extract top1
	os.system("..\\usearch.exe -otutab {work}\{each}.fastq -otus {each}.fastq_cons_top -id 0.8 -strand both -matched {each}_matched.fasta".format(each= each,work=workDir))
	if argv["seq_number"] != None:
		number = argv["seq_number"]
		os.system("python ..\chaifen.py {each}_matched.fasta {number}".format(each=each,number=number))
		os.system("..\mafft --reorder --adjustdirection --globalpair --maxiterate 100 --thread -1 {each}_matched.deal.fasta > {each}_matched.fasta.fas".format(each=each))
	else:
		os.system("..\mafft --reorder --adjustdirection --globalpair --maxiterate 100 --thread -1 {each}_matched.fasta > {each}_matched.fasta.fas".format(each=each))
	os.system("python ..\Cotu-generator.py -i {each}_matched.fasta.fas -r 50 -l 50 -d 5 -id1 0.2 -id2 0.5".format(each=each))
	os.chdir("..")