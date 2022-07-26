import sys


def txt_importer(path_file):
    if path_file.endswith('.txt'):
        try:
            arquivo = open(path_file)
            return arquivo.splitlines()
        except FileNotFoundError:
            sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    else:
        sys.stderr.write('Formato inválido\n')
