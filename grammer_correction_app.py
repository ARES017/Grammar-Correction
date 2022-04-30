from flask import Flask, request, render_template
from gramformer import Gramformer
from grammer_correct import set_seed, tokenize_sentences, grammer_correct

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def landing_page():
    if request.method == "GET":
        return render_template('landing_page.html', result="")
    
    elif request.method == "POST":
        try:
            input_sentence = request.json["inputText"]
        except KeyError:
            input_sentence = None

        if input_sentence:
            # sentence_list = tokenize_sentences(input_sentence)
            return {
                "payload": input_sentence
            }
            # updated_sentence, corrected_sentece_edit_list = grammer_correct(gf, sentence_list)

            # if updated_sentence:
            #     return render_template('result.html', result=updated_sentence)
            # else:
            #     return render_template('result.html', result=input_sentence)
        
        else:
            return {
                "payload": ""
            }

if __name__ == '__main__':
    set_seed(1212)
    # gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector 
    app.run(debug=True)
