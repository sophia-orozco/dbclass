import sys
sequence=sys.argv[1]

aa=["phe","phe","leu","leu","leu","leu","leu","leu","ile","ile","ile","met","val","val","val","val","ser","ser","ser","ser","ser",
"ser","pro","pro","pro","pro","thr","thr","thr","thr","ala","ala","ala","ala","tyr","tyr","his","his","gln","gln","asn","asn",
"lys","lys","asp","asp","glu","glu","cys","cys","trp","arg","arg","arg","arg","arg","arg","gly","gly","gly","gly","stop","stop","stop"]
codones=["uuu","uuc","uua","uug","cuu","cuc","cua","cug","auu","auc","aua","aug","guu","guc","gua","gug","ucu","ucc","uca","ucg",
"agu","agc","ccu","ccc","cca","ccg","acu","acc","aca","acg","gcu","gcc","gca","gcg","uau","uac","cau","cac","caa","cag","aau","aac",
"aaa","aag","gau","gac","gaa","gag","ugu","ugc","ugg","cgu","cgc","cga","cgg","aga","agg","ggu","ggc","gga","ggg","uaa","uag","uga"]

for i in range(0,len(sequence),3):
    for j in range(0,len(codones)):
        if(sequence[i:i+3]==codones[j]):
            print(aa[j])
            break
