from flask import Flask, request
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import pickle
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ps = PorterStemmer()
file1 = os.path.join(app.root_path, 'trained_model/vectorizer.pkl')
file2 = os.path.join(app.root_path, 'trained_model/model.pkl')

def text_transformation(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()

    for i in text:
        if i in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    
    
    return " ".join(y)

def SpamOrNot(text):    
    trfid = pickle.load(open(file1, 'rb'))
    model = pickle.load(open(file2, 'rb'))
    transformed_text = text_transformation(text)
    vectorized_text = trfid.transform([transformed_text])
    result = model.predict(vectorized_text)
    if result[0] == 1:
        return "Spam"
    else:
        return "Not Spam"


@app.route("/", methods=['GET', 'POST'])
# @cross_origin()
def hello():
    if request.method == 'POST':
        a = request.json
        print(a['sentence'])
        b = SpamOrNot(a['sentence'])
        return b
    return "You can only post"


if __name__ == "__main__":
    app.run(debug=True, port=8000)