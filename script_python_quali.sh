#!/bin/bash
#
#SBATCH -c 10 # numero de cores
#SBATCH --mail-user=beatrizsilva@alunos.utfpr.edu.br
#SBATCH -t 3-0:00 # tempo em (D-HH:MM) Dia-Hora:Minutos
#SBATCH -w ghidorah
#SBATCH -o slurm.%j.out # STDOUT - Arquivo de Saida
#SBATCH -e slurm.%j.err # STDERR - Arquivo de Erro

module load prog_lang/python-3.9

python3.9 mining_genes.py
