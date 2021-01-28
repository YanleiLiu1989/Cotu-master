import sys
oriFile = sys.argv[1].strip()
name = oriFile.split(".")[0]
linenumber = int(sys.argv[2].strip())
f1 = open(oriFile,"r")
f2 = open("{name}.deal.fasta".format(name=name),"w")
seqinfo = []
seq_tmp = ""
line_count = 0
for each in f1:
	each  = each.strip()
	if ">" in each:
		if line_count == 0:
			seq_tmp  = seq_tmp + each+"\n"
			line_count += 1
		else:
			if line_count <= linenumber :
				f2.write(seq_tmp+"\n")
				line_count += 1
				seq_tmp  =  each+"\n"
	else:
		seq_tmp  += each
		
		