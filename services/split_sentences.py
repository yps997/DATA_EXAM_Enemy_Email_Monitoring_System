def process_sentences(sentences, keyword):
    split_sentences = [s.strip() for sentence in sentences for s in sentence.replace('!', '.').split('.') if s.strip()]
    return sorted(split_sentences, key=lambda x: keyword.lower() not in x.lower())


