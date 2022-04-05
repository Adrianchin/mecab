from flask import Flask, request, json
from fugashi import Tagger

app = Flask(__name__)
@app.route("/japanesetoken", methods=["POST"])
def japanesetoken():
    tagger = Tagger('-Owakati')
    text = request.get_json(force=True)
    print(text)
    word = tagger(text["text"])
    res_dct=[{"id":i, "token":str(word[i]), "wordType":str(word[i].feature.pos1), "tokenRoot":str(word[i].feature.lemma), "conjugationType":str(word[i].feature.cType), "conjugationForm":str(word[i].feature.cForm), "pronunciation":str(word[i].feature.pron), "pronunciationBase":str(word[i].feature.pronBase), "extraInfo":str(word[i].pos)} for i in range(0,len(word),)]

    tokenizedtext=json.dumps(res_dct, ensure_ascii=False)
    return tokenizedtext
