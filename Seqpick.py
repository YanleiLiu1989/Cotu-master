import sys
oriFile = sys.argv[1].strip()
name = oriFile.split("aln")[0]
count = oriFile.split(".")[-1]
linenumber = int(sys.argv[2].strip())
f1 = open(oriFile,"r")
f2 = open("{name}.{count}.deal.fasta".format(name=name,count=count),"w")
seqinfo = []
seq_tmp = ""
line_count = 0
for each in f1:
	each  = each.strip()
	if ">" in each:
		if line_count == 0:
			seq_tmp  = seq_tmp + each+"\n"
			print(seq_tmp)
			line_count += 1
		else:
			if line_count <= linenumber :
				print(seq_tmp)
				f2.write(seq_tmp+"\n")
				line_count += 1
				seq_tmp  =  each+"\n"
	else:
		seq_tmp  += each
		
		