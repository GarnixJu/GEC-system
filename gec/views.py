from django.http import JsonResponse
import spacy
import json
import os

from .translate import translate
from errant.parallel_to_diff import parallel_to_diff


nlp = spacy.load(os.environ.get('SPACY_MODEL', 'en'), disable=['ner'])


def correct_it(request):
    if request.is_ajax() and request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        text = data.get('text', '')
    elif request.method == 'GET':
        text = request.GET.get('text', '')
        data = {'text': text}
    else:
        data = {}

    lines = [' '.join(token.text for token in sent)
             for line in text.splitlines() if line.strip()
             for sent in nlp(line.strip()).sents
             ]
    tokenized_text = '\n'.join(lines)
    corrected_text = translate(tokenized_text)

    data['result'] = corrected_text
    diff = [parallel_to_diff(before, after, nlp)
            for before, after in zip(lines, corrected_text.splitlines())]
    data['word_diff'] = '\n'.join(diff)
    data['word_diff_by_sent'] = diff
    return JsonResponse(data)
