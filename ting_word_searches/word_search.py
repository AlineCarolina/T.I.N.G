def get_words(word, instance, boolean):
    result_list = []
    occurrences = []

    for index, line in enumerate(instance._data[0]['linhas_do_arquivo']):
        if word.lower() in line.lower():
            if boolean is True:
                occurrences.append({'linha': index + 1, 'conteudo': line})
            else:
                occurrences.append({'linha': index + 1})

    if len(occurrences) > 0:
        result_list.append({
            'palavra': word,
            'arquivo': instance._data[0]['nome_do_arquivo'],
            'ocorrencias': occurrences,
        })

    return result_list


def exists_word(word, instance):
    return get_words(word, instance, False)


def search_by_word(word, instance):
    return get_words(word, instance, True)
