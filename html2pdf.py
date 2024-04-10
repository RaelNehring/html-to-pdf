import os
import sys
import pdfkit

def obter_nome_arquivo(path_to_file):
    nome_arquivo_com_extensao = os.path.basename(path_to_file)
    nome_arquivo, extensao = os.path.splitext(nome_arquivo_com_extensao)
    return nome_arquivo

arquivo_para_converter = sys.argv[1]
print(f'Arquivo para converter {arquivo_para_converter}')

if len(sys.argv) > 2:
    tamanho_pagina = sys.argv[2]
else:
    tamanho_pagina = 'A4'

print(f'Tamanho da página: {tamanho_pagina}')

# Caminho para o executável wkhtmltopdf
# https://wkhtmltopdf.org/
caminho_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# Caminho para o arquivo HTML de entrada
nome_arquivo = obter_nome_arquivo(arquivo_para_converter)
print(f'Nome arquivo: {nome_arquivo}')

# Caminho para o arquivo PDF de saída
arquivo_saida = r'{}\{}.pdf'.format(os.path.dirname(arquivo_para_converter), nome_arquivo)
print(f'Nome arquivo de saída: {arquivo_saida}')

# Opções para a conversão
configs = {
    'quiet': '',
    'page-size': tamanho_pagina,
    'encoding': "UTF-8",
    'no-outline': None  # Remove o contorno ao redor do PDF
}

# Converter HTML para PDF
pdfkit.from_file(arquivo_para_converter, arquivo_saida, options=configs, configuration=pdfkit.configuration(wkhtmltopdf=caminho_wkhtmltopdf))
