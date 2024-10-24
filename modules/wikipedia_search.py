import wikipedia

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError:
        return "Can you be more specific?"
    except wikipedia.exceptions.PageError:
        return "I couldn't find any result."
