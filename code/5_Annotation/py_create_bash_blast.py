genes_info=[]
start=[]
bases=[]
genename=[]
with open ("genes.csv", "r") as file:
    for line in file:
        genes_info.append(line.strip().split(","))
    for i in range(len(genes_info)):
        start.append(genes_info[i][0])
        bases.append(genes_info[i][2])
        genename.append(genes_info[i][3])

with open("blast.sh", "w") as bash:
    bash.write("#!/bin/bash -l\n")
    bash.write("#SBATCH -A g2019003\n")
    bash.write("#SBATCH -p core\n")
    bash.write("#SBATCH -n 4\n")
    bash.write("#SBATCH -t 04:00:00\n")
    bash.write("#SBATCH -J run_blast\n")
    bash.write("#SBATCH --mail-type=ALL\n")
    bash.write("#SBATCH --mail-user Carolina.Barros.8371@student.uu.se\n\n")
    bash.write("module load bioinfo-tools blast\n\n")
    for i in range(len(start)):
        bash.write("cat genome_oneline.txt | awk '{print substr($0,"+"{},{}".format(start[i], bases[i])+")}' > temp.txt\n")
        bash.write("blastn -db nt -query temp.txt -out gene"+str(i+1)+".out\n")
