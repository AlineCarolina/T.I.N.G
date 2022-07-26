import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance._data:
        if i['nome_do_arquivo'] == path_file:
            return
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_importer(path_file)),
        'linhas_do_arquivo':  txt_importer(path_file)
    }
    instance.enqueue(result)
    print(str(result))


def remove(instance):
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
    else:
        file = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write('Posição inválida\n')
