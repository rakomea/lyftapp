from flask import Flask, request, abort
import json

app = Flask(__name__)


@app.route('/test', methods=['POST'])
'''
Function  to cut string and return a string containing
every third letter from the original string
1) a character array is initalized to start every thiid character
2) a counter variable to indicate third character - counter is reset
after it reaches 3
returns string made from cut charcaters joined together
'''


def string_cut(string):
    cut_chars = []
    counter = 0
    for char in string:
        counter += 1
        if counter == 3:
            cut_chars.append(char)
            counter = 0
    return "".join(cut_chars)

'''
Function  to parse input string and return JSON object
Use try except to catch any input string errors
run string_cut function and returned processed string
'''


def parse_json():
    try:
        string_to_cut = request.json['string_to_cut']
    except:
        print('POST request error')
        abort(400)
    processed_string = string_cut(string_to_cut)
    returned_json = {
        "return_string": processed_string,
    }
    return json.dumps(returned_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
