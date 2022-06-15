from Bio import Entrez, SeqIO

Entrez.email = 'beatrizsilva@alunos.utfpr.edu.br'

def organizar_dados(genoma_id):
    
    arq = open("banco_de_dados_genes/dados_genes_"+str(genoma_id)+".fasta", 'w')
    arq_faltantes = open("banco_de_dados_genes/dados_genes_faltantes_"+str(genoma_id)+".fasta", 'w')

    for rec in SeqIO.parse("banco_de_dados_genomas/genoma_"+str(genoma_id)+".gb", "genbank"):
        
        for feature in rec.features:

            gene = ""
            header = ""
            aux = 0

            if (feature.type == "CDS"):

                if ('translation' in feature.qualifiers):
                    translation = feature.qualifiers["translation"].pop()
                else:
                    translation = 'AUSENTE'

                
                if ('gene' in feature.qualifiers):

                    gene = feature.qualifiers['gene'].pop()

                else:
                    
                    inference = feature.qualifiers['inference'].pop()
                    indice = inference.find('RefSeq:')
                
                    if not indice == -1:
                        
                        reference_sequence = inference[(indice+7):]
                        handle = Entrez.efetch(db="protein", id=reference_sequence, rettype="gb")

                        for record in SeqIO.parse(handle,'gb'):

                            for feats in record.features:

                                if (feats.type == "CDS") and ("gene" in feats.qualifiers):

                                    gene += feats.qualifiers['gene'].pop() + ' '    
                        
                        if gene == "":

                            aux = 1
                            header = 'inference: ' + str(inference) + ' '

                    else:
                        
                        aux = 1
                        header = 'inference: ' + str(inference) + ' '

                for quali in feature.qualifiers.keys():

                    if quali != 'translation' and feature.qualifiers[quali]:

                        header += str(quali) + ": " + str(feature.qualifiers[quali].pop()) + " "

                if aux == 0:
                    
                    arq.write('>'+gene+' '+header+'\n')
                    arq.write(translation+'\n')

                else:

                    arq_faltantes.write('>'+header+'\n')
                    arq_faltantes.write(translation+'\n')

    arq.close()
    arq_faltantes.close()


lista_id = ['CP045993.1', 'CP023748.1', 'CP079719.1', 'CP040881.1']

for genoma_id in lista_id:
    
    organizar_dados(genoma_id)

#FIM
