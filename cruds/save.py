import json, os

def save_results_to_json(results, FILEPATH):
    try:
        with open(FILEPATH, 'w') as FILE:
            json.dump(results, FILE)
    except:
        return False, "Não consegui salvar os resultados em JSON", 424
    return True, "Resultados foram salvos no JSON", 200