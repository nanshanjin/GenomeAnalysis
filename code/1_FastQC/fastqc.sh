#!/bin/bash -L
#SBATCH -A g2019003
#SBATCH -p core
#SBATCH -n 2
#SBATCH -t 00:05:00
#SBATCH -J run_fastqc
#SBATCH --mail-type=ALL
#SBATCH --mail-user Carolina.Barros.8371@student.uu.se
# Load modules
module load bioinfo-tools
module load FastQC/0.11.5
# Your commands
for filename in /domus/h1/carolpb/GenomeAnalysis/data/wgs/*.fastq.gz
    do
        fastqc $filename -o /home/carolpb/GenomeAnalysis/results/1_QC_dna/fastqc_results;
    done
