import numpy as np
import pandas as pd
import json
from flask import Flask, render_template, request, \
                  jsonify
from get_opportunities import get_opportunities

app = Flask(__name__)

############################################################
# API
############################################################
@app.route("/api", methods=['POST'])  
def api():
    try:
        data_in = request.get_json(force=True)
        keywords_in = data_in

        # get output data   
        keywords, opportunities = get_opportunities(keywords_in)
        data_out = {'keyword_synonym': keywords,
                    'opportunity_id': opportunities}    
        return json.dumps(data_out)
    
    except:
        return jsonify('Invalid parameters!')
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)