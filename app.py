from flask import Flask, request

import pandas as pd

app = Flask(__name__)

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        json_file = request.files.get('file')
        print(json_file.filename)
        # with open(json_file.filename) as f_input:
        df = pd.read_json(json_file.filename)
        # print(df)
        df.to_csv('data.csv', encoding='utf-8', index=False)
    return '''
    <!doctype html>
    <title>Upload a json file</title>
    <h1>JSON file upload</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''

# insert database related code here
if __name__ == "__main__":
    app.run()