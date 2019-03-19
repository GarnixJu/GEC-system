from django.http import JsonResponse
import spacy
import json
import os

from .translate import translate
from .wdiff import wdiff


nlp = spacy.load(os.environ.get('SPACY_MODEL', 'en'))


def correct_it(request):
    if request.is_ajax() and request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        text = data.get('text', '')
    elif request.method == 'GET':
        text = request.GET.get('text', '')
        data = {'text': text}
    else:
        data = {}

    tokenized_text = '\n'.join('\n'.join(' '.join(token.text for token in sent) for sent in nlp(line.strip()).sents) for line in text.splitlines() if line.strip())
    corrected_text = translate(tokenized_text)
    data['result'] = corrected_text
    diff = [' '.join(wdiff(before, after)) for before, after in zip(tokenized_text.splitlines(), corrected_text.splitlines())]
    data['word_diff'] = '\n'.join(diff)
    data['word_diff_by_sent'] = diff
    return JsonResponse(data)

