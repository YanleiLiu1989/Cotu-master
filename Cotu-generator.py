import argparse,sys
parse = argparse.ArgumentParser(prog="report",description="a report program",usage='%(prog)s.py [options] -i input_file')
parse.add_argument("-i",help="input file",type=str,required=True)
parse.add_argument("-l",help="Number of alignment bases using id1 stragegy from the left",type=int,default=15)
parse.add_argument("-r",help="Number of alignment bases using id1 stragegy from the right",type=int,default=15)
parse.add_argument("-d",help="The minimum sequencing depth,sample with sequencing depth lower than 5 will be dropt",type=int,default=5)
parse.add_argument("-id1",help="The first sequencing depth strategy,in a certain region of two ends, base number counted larger than the parameter given will ignore gaps and conducted the majority for consensus generation",type=float,default=0.2)
parse.add_argument("-id2",help="The second sequencing depth strategy,in a certain region of the middle, base number counted larger than the parameter given will ignore gaps and conducted the majority for consensus generation. If not, a gap will be produced in the certain position",type=float,default=0.5)
args = parse.parse_args()
deep = args.d
two_end_of_seq = 1-args.id1
middle_seq = 1-args.id2
label = str()
f1 = open ("{filename}".format(filename=args.i),"r")
head = args.i.split(".")[0]
info = []
seq_tmp = str()
line_count = 0
for each_line in f1:
    each_line = each_line.strip()
    if each_line.startswith(">"):
        if seq_tmp == "":    
            continue
        else:
           info.append(seq_tmp)
           seq_tmp = ""
    else:
        seq_tmp = seq_tmp + each_line
DATA = []
total_deepth = int()
if len(info) < deep:
	sys.exit("The deepth is less than {deep}!!!".format(deep=deep))
else:
	total_deepth = len(info)
for a in range(0,len(info[0])-1):
    linshi = {}
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    other_count = 0
    for i in info:
        if i[a] == "A" or i[a] == "a":
            A_count += 1
        elif i[a] == "C" or i[a] == "c":
            C_count += 1
        elif i[a] == "G" or i[a] == "g":
            G_count += 1
        elif i[a] == "T" or i[a] == "t":
            T_count += 1
        elif i[a] == "-":
            other_count += 1
    linshi["A"] = A_count
    linshi["C"] = C_count
    linshi["G"] = G_count
    linshi["T"] = T_count
    linshi["-"] = other_count
    DATA.append(linshi)
#print DATA
start = str()
middle = str()
end = str()
total = str()
left = int(args.l)
right = int(args.r)
for i in range(0,left):
    if int(DATA[i]["-"]) > round(two_end_of_seq*total_deepth):
        first = "-"
#           first = max(DATA[i],key=DATA[i].get)
#           last = str()
        start = start + first
    else:
#        first == "-":
        if "-" in DATA[i].keys():
            del DATA[i]["-"]
        second = max(DATA[i],key=DATA[i].get)
#        if int(DATA[i][second]) >= deep:
        last = second
#   else:
#        last = first
        start = start + last
for i in range (left,len(DATA)-right-1):
    if int(DATA[i]["-"]) > round(middle_seq*total_deepth):
        first = "-"
        middle = middle + first
    else:
       if "-" in DATA[i].keys():
            del DATA[i]["-"]
       a = max(DATA[i],key=DATA[i].get)
       middle = middle + a
#print seq
for i in range (len(DATA)-right-1,len(DATA)):
    first = max(DATA[i],key=DATA[i].get)
    last = str()
    if int(DATA[i]["-"]) > round(two_end_of_seq*total_deepth):
    	  first = "-"
    	  end = end + first
    else:
        if "-" in DATA[i].keys():
        	  del DATA[i]["-"]
        second = max(DATA[i],key=DATA[i].get)
        last = second
#    else:
#        last = first
        end = end + last
total = start + middle + end
total = total.replace("-","")
rest = ">"+head +"_"+"result" + ":" + "consensus_size={depth}".format(depth=len(info))+":"+"sequence_length={length}".format(length=len(DATA))+":"+"consensus_length={length}".format(length=len(total))
f2 = open ("{label}_1.fasta".format(label=args.i),"w")
f2.write(rest + "\n" + total + "\n")
f2.close()
