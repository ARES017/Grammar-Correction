from flask import Flask, render_template
from gramformer import Gramformer
from grammer_correct import set_seed

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing_page.html')


if __name__ == '__main__':
    set_seed(1212)
    gf = Gramformer(models = 1, use_gpu=False) # 1=corrector, 2=detector 
    app.run(debug=True)
