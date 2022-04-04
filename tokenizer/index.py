from flask import Flask, request, json
from fugashi import Tagger

app = Flask(__name__)
@app.route("/japanesetoken", methods=["POST"])
def japanesetoken():
    tagger = Tagger('-Owakati')
    text = request.get_json(force=True)
    print(text)
    word = tagger(text["text"])
    res_dct={i:[str(word[i]), str(word[i].feature.pos1), str(word[i].feature.lemma), str(word[i].feature.cType), str(word[i].feature.cForm), str(word[i].feature.pron), str(word[i].feature.pronBase), str(word[i].pos)] for i in range(0,len(word),)}

    tokenizedtext=json.dumps(res_dct, ensure_ascii=False)
    return tokenizedtext
