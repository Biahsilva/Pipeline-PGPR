from Bio import SeqIO

def minerar_genes(genoma_id):
    
    genes = []

    for rec in SeqIO.parse("banco_de_dados_genes/dados_genes_"+str(genoma_id)+".fasta", "fasta"):
        
        genes.append(rec.name)

    for record in SeqIO.parse("banco_de_dados_complementares/dados_genes_complementares_"+str(genoma_id)+".fasta", "fasta"):

        genes.append(record.name)

    return genes

lista_id = ['CP045993.1', 'CP023748.1', 'CP079719.1', 'CP040881.1']

dicionario_genomas = {}

for genoma_id in lista_id:

    dicionario_genomas[genoma_id] = set(minerar_genes(genoma_id))

genes_hna3_pgpr = set(minerar_genes('HNA3'))

# Comparação HNA3 com HNA3-PGPR
inter_hna3_pgpr = genes_hna3_pgpr.intersection(dicionario_genomas['CP040881.1'])

# Comparação LABIM22 com HNA3-PGPR
inter_labim22_pgpr = genes_hna3_pgpr.intersection(dicionario_genomas['CP045993.1'])

# Comparação LABIM40 com HNA3-PGPR
inter_labim40_pgpr = genes_hna3_pgpr.intersection(dicionario_genomas['CP023748.1'])

# Comparação LABIM44 com HNA3-PGPR
inter_labim44_pgpr = genes_hna3_pgpr.intersection(dicionario_genomas['CP079719.1'])

arquivo = open('resultado_comparacoes.txt','w')

arquivo.write("Informações sobre a Interseção entre os Genomas HNA3 e HNA3-PGPR: \n")
arquivo.write("Quantidade de Genes: {}\n".format(len(inter_hna3_pgpr)))

for i in inter_hna3_pgpr:
    arquivo.write(str(i)+', ')


arquivo.write("\n\nInformações sobre a Interseção entre os Genomas LABIM22 e HNA3-PGPR: \n")
arquivo.write("Quantidade de Genes: {}\n".format(len(inter_labim22_pgpr)))

for i in inter_labim22_pgpr:
    arquivo.write(str(i)+', ')


arquivo.write("\n\nInformações sobre a Interseção entre os Genomas LABIM40 e HNA3-PGPR: \n")
arquivo.write("Quantidade de Genes: {}\n".format(len(inter_labim40_pgpr)))

for i in inter_labim40_pgpr:
    arquivo.write(str(i)+', ')


arquivo.write("\n\nInformações sobre a Interseção entre os Genomas LABIM44 e HNA3-PGPR: \n")
arquivo.write("Quantidade de Genes: {}\n".format(len(inter_labim44_pgpr)))

for i in inter_labim44_pgpr:
    arquivo.write(str(i)+', ')

arquivo.write('\n')
arquivo.close()

#FIM
