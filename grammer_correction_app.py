import status
from datetime import datetime
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
            return {
                "timestamp": datetime.now().timestamp(),
                "msg": "Failed",
                "payload": {
                    "correctedText": "",
                    "edits": ""
                },
                "status": status.HTTP_400_BAD_REQUEST
            }

        if input_sentence:
            try:
                sentence_list = tokenize_sentences(input_sentence)
                updated_sentence, sentence_edits = grammer_correct(gf, sentence_list)

                if updated_sentence:
                    return {
                        "timestamp": datetime.now().timestamp(),
                        "msg": "Success",
                        "payload": {
                            "correctedText": updated_sentence,
                            "edits": sentence_edits
                        },
                        "status": status.HTTP_200_OK
                    }
                
                else:
                    return {
                        "timestamp": datetime.now().timestamp(),
                        "msg": "Failed",
                        "payload": {
                            "correctedText": "",
                            "edits": ""
                        },
                        "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                    }

            except:
                return {
                "timestamp": datetime.now().timestamp(),
                "msg": "Failed",
                "payload": {
                    "correctedText": "",
                    "edits": ""
                },
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            }

        else:
            return {
                "timestamp": datetime.now().timestamp(),
                "msg": "No input text",
                "payload": {
                    "correctedText": "",
                    "edits": ""
                },
                "status": status.HTTP_200_OK
            }

if __name__ == '__main__':
    set_seed(1212)
    gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector 
    app.run(debug=True)
