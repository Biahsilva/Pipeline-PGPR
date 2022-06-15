from Bio import Entrez, SeqIO

Entrez.email = 'beatrizsilva@alunos.utfpr.edu.br'

def download_genoma(genoma_id):
    
    saida = open('banco_de_dados_genomas/genoma_'+str(genoma_id)+'.gb','w')
    handle = Entrez.efetch(db='nuccore', id=genoma_id, rettype='gb')
    seqRecord = SeqIO.read(handle, format='gb')
    handle.close()
    saida.write(seqRecord.format('gb'))
    saida.close()

lista_id = ['CP045993.1', 'CP023748.1', 'CP079719.1', 'CP040881.1']

for genoma_id in lista_id:

    download_genoma(genoma_id)

#FIM
