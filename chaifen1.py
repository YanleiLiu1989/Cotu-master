import sys
#from collections import defaultdict
oriFile = sys.argv[1].strip()
name = oriFile.split(".")[0]
linenumber = int(sys.argv[2].strip())
f1 = open(oriFile,"r").readlines()
#f2 = open("{name}.fastq_cons_top".format(name=name),"w")
headinfo = []
seq_tmp = ""
file_count = 0
seq_info = {}
for each in f1:
	if ">" in each:
		seq_tmp = each
		headinfo.append(each)
		seq_info[seq_tmp] = []
	else:
		seq_info[seq_tmp].append(each.strip())
if len(headinfo) < linenumber:
	linenumber = len(headinfo)
for i in range(0,linenumber):
	f2 = open("{name}.fastq_cons_top_copy{i}".format(name=name,i=i+1),"w")
#	print(headinfo[i],"".join(seq_info[headinfo[i]]))##write it to file
	f2.write(headinfo[i])
	f2.write("".join(seq_info[headinfo[i]]))
