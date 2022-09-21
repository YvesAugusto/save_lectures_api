import json, os

def save_results_to_json(results, FILEPATH):
    try:
        with open(FILEPATH, 'w') as FILE:
            json.dump(results, FILE)
    except FileNotFoundError:
        return {}, "O caminho do arquivo não existe", 404
    except:
        return {}, "Não consegui salvar os resultados em JSON", 424
    return results, "Resultados foram salvos no JSON", 200