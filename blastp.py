from Bio import SeqIO
from Bio.Blast.Applications import*

def organizar_query(genoma_id):
    
    arq = open("banco_de_dados_queries/query_"+str(genoma_id)+".fasta", 'w')
    lista_genes = []

    for record in SeqIO.parse("banco_de_dados_genes/dados_genes_"+str(genoma_id)+".fasta", "fasta"):

        lista_genes.append(record.name)

    for rec in SeqIO.parse("dados_genes_HNA3.fasta", "fasta"):
        
        gene = str(rec.name)

        if gene not in lista_genes:

            arq.write(">"+str(rec.description)+"\n")
            arq.write(str(rec.seq)+'\n')

    arq.close()

def blastp(genoma_id):

    query = "banco_de_dados_queries/query_"+str(genoma_id)+".fasta"
    subject = "banco_de_dados_genes/dados_genes_faltantes_"+str(genoma_id)+".fasta"
    comando_blastp = NcbiblastpCommandline(query=query, subject=subject, out="resultados_blast/resultado_blast_"+str(genoma_id)+".txt")
    stdout, stderr = comando_blastp()

lista_id = ['CP045993.1', 'CP023748.1', 'CP079719.1', 'CP040881.1']

for genoma_id in lista_id:
    
    organizar_query(genoma_id)
    blastp(genoma_id)

#FIM
