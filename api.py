import paralleldots
paralleldots.set_api_key('grc6WJnN3qmQeXGd5AsXH1n77zBuh23ELSDDCSadKSM')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
