{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n"
     ]
    }
   ],
   "source": [
    "print(\"a\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "aa=[\"phe\",\"phe\",\"leu\",\"leu\",\"leu\",\"leu\",\"leu\",\"leu\",\"ile\",\"ile\",\"ile\",\"met\",\"val\",\"val\",\"val\",\"val\",\"ser\",\"ser\",\"ser\",\"ser\",\"ser\",\n",
    "\"ser\",\"pro\",\"pro\",\"pro\",\"pro\",\"thr\",\"thr\",\"thr\",\"thr\",\"ala\",\"ala\",\"ala\",\"ala\",\"tyr\",\"tyr\",\"his\",\"his\",\"gln\",\"gln\",\"asn\",\"asn\",\n",
    "\"lys\",\"lys\",\"asp\",\"asp\",\"glu\",\"glu\",\"cys\",\"cys\",\"trp\",\"arg\",\"arg\",\"arg\",\"arg\",\"arg\",\"arg\",\"gly\",\"gly\",\"gly\",\"gly\",\"stop\",\"stop\",\"stop\"]\n",
    "codones=[\"uuu\",\"uuc\",\"uua\",\"uug\",\"cuu\",\"cuc\",\"cua\",\"cug\",\"auu\",\"auc\",\"aua\",\"aug\",\"guu\",\"guc\",\"gua\",\"gug\",\"ucu\",\"ucc\",\"uca\",\"ucg\",\n",
    "\"agu\",\"agc\",\"ccu\",\"ccc\",\"cca\",\"ccg\",\"acu\",\"acc\",\"aca\",\"acg\",\"gcu\",\"gcc\",\"gca\",\"gcg\",\"uau\",\"uac\",\"cau\",\"cac\",\"caa\",\"cag\",\"aau\",\"aac\",\n",
    "\"aaa\",\"aag\",\"gau\",\"gac\",\"gaa\",\"gag\",\"ugu\",\"ugc\",\"ugg\",\"cgu\",\"cgc\",\"cga\",\"cgg\",\"aga\",\"agg\",\"ggu\",\"ggc\",\"gga\",\"ggg\",\"uaa\",\"uag\",\"uga\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "sequence=\"augugagagagagau\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "met\n",
      "stop\n",
      "glu\n",
      "arg\n",
      "asp\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,len(sequence),3):\n",
    "    for j in range(0,len(codones)):\n",
    "        if(sequence[i:i+3]==codones[j]):\n",
    "            print(aa[j])\n",
    "            break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
