from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    url = "http://openapi.foodsafetykorea.go.kr/api/baba58c32c4343b78e78/COOKRCP01/json/1/30"
    response = requests.get(url)
    contents = response.text
    json_data = json.loads(contents)
    
    # API 응답에서 필요한 데이터 추출
    recipes = json_data['COOKRCP01']['row']
    
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    url = "http://openapi.foodsafetykorea.go.kr/api/baba58c32c4343b78e78/COOKRCP01/json/1/30"
    response = requests.get(url)
    contents = response.text
    json_data = json.loads(contents)
    
    # 데이터 출력 (디버깅용)
    print(json_data)
    
    recipes = json_data['COOKRCP01']['row']
    
    return render_template('index.html', recipes=recipes)
