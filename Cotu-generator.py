import argparse,sys
def getStartEnd(base_ratio,reverse = False):
    if reverse == False:
        for i in range(len(base_ratio)):
            if base_ratio[i] < 0.5 and base_ratio[i+1] < 0.5 and base_ratio[i+2] < 0.5:
                return i
    else:
        for i in range(len(base_ratio[::-1])):
            if base_ratio[::-1][i] < 0.5 and base_ratio[::-1][i+1] < 0.5 and  base_ratio[::-1][i+2] < 0.5:
                if i == 0:
                    return len(base_ratio)
                else:
                    return len(base_ratio)-i+1
			
parse = argparse.ArgumentParser(prog="Cotu-generator",description="a Cotu generate program",usage='python %(prog)s.py -i input_file [options]. For example: python Cotu-generator.py -i alignment-file.fasta -r 50 -l 50 -d 5 -id1 0.2 -id2 0.5')
parse.add_argument("-i",help="input file",type=str,required=True)
parse.add_argument("-o",type=str,help="Output sample name",required=True)
parse.add_argument("-t","--type",type=str,help="Type of copy [Single or Multi]",required=True)
parse.add_argument("-cp",type=int,help="The ranking of copy number",default=None)
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
	sys.exit("The depth is less than {deep}!!!".format(deep=deep))
else:
	total_deepth = len(info)+1
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


for  i in DATA:
    total_list = i.values()
    total_count = 0
    for each_count in total_list:
        total_count += each_count
    if i["-"]/total_count > 0.9:
        DATA.remove(i)
base_ratio = [i["-"]/(len(info)+1) for i in DATA]
start = str()
middle = str()
end = str()
total = str()
left = getStartEnd(base_ratio)
right = getStartEnd(base_ratio,reverse = True)
if left != 0:
    for i in range(0,left):
        if int(DATA[i]["-"]) > round(two_end_of_seq*total_deepth):
            first = "-"
            start = start + first
        else:
            if "-" in DATA[i].keys():
                del DATA[i]["-"]
            second = max(DATA[i],key=DATA[i].get)
            last = second
            start = start + last
if right == len(DATA):
    right -= 1
for i in range (left,right):
    if int(DATA[i]["-"]) > round(middle_seq*total_deepth):
        first = "-"
        middle = middle + first
    else:
       if "-" in DATA[i].keys():
            del DATA[i]["-"]
       a = max(DATA[i],key=DATA[i].get)
       middle = middle + a
if right != len(DATA):
    for i in range(right,len(DATA)):
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
            end = end + last
total = start + middle + end
total = total.replace("-","")
rest = ">"+head +"_"+"result" + ":" + "consensus_size={depth}".format(depth=len(info))+":"+"sequence_length={length}".format(length=len(DATA))+":"+"consensus_length={length}".format(length=len(total))
if args.type == "Single":
	f2 = open ("{sample}.Cotu.fasta".format(sample=args.o),"w")
else:
	f2 = open("{sample}.Cotu{i}.fasta".format(sample=args.o,i=args.cp),"w")
f2.write(rest + "\n" + total + "\n")
f2.close()
