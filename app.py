from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    q_type = request.form.get('type')
    q_val = request.form.get('value')
    res = None
    try:
        if q_type == 'vehicle':
            url = f"https://vehicleinfobyterabaap.vercel.app/lookup?rc={q_val}"
        elif q_type == 'tg_id':
            url = f"https://tgchatid.vercel.app/api/lookup?number={q_val}"
        elif q_type == 'phone':
            url = f"https://ft-osint-api.duckdns.org/api/number?key=nobitaoptrialkey&num={q_val}"
        
        r = requests.get(url, timeout=10)
        res = r.json()
    except:
        res = {"error": "API Down ya Invalid Input!"}
    return render_template('index.html', result=res)

if __name__ == '__main__':
    app.run(debug=True)
