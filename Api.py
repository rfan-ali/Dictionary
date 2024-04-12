import requests
def getMeaningApi(word):
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    if response.status_code >= 400:
        print("Erroe is loading data")
        return None
    data = response.json()
    return data