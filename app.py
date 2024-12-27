from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/full_form')
def full_form():
    return render_template('full_form.html')

@app.route('/full_form_result', methods=['GET'])
def full_form_result():
    project_name = request.args.get('project_name')
    requested_by = request.args.get('requested_by')
    camera_name = request.args.get('camera_name')
    product_type = request.args.get('product_type')
    # Procesar más campos según sea necesario
    result = {
        "project_name": project_name,
        "requested_by": requested_by,
        "camera_name": camera_name,
        "product_type": product_type
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')












