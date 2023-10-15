from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []


@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'GET':
        return jsonify(todos)
    elif request.method == 'POST':
        data = request.get_json()
        id = len(todos)
        data['id'] = id
        todos.append(data)
        return jsonify({
            "message": "Todo added successfully.",
            'data': data
        })


@app.route("/todos/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    print(id, data)
    for todo in todos:
        if todo["id"] == id:
            todo["title"] = data.get("title", todo["title"])
            todo["status"] = data.get("status", todo["status"])
            return jsonify({"message": "Todo updated successfully."})
    return jsonify({"error": "Todo not found."})


@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    for todo in todos:
        if todo['id'] == id:
            todos.remove(todo)
    return jsonify({"se": "Todo not found."})


if __name__ == '__main__':
    app.run(debug=True)
