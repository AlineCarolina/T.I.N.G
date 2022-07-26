def exists_word(word, instance):
    result_list = []
    occurrences = []

    for index, line in enumerate(instance._data[0]['linhas_do_arquivo']):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1})

    if len(occurrences) > 0:
        result_list.append({
            "palavra": word,
            "arquivo": instance._data[0]["nome_do_arquivo"],
            "ocorrencias": occurrences,
        })

    return result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
