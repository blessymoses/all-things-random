from flask import Flask, request

app = Flask(__name__)

boxes = {}


@app.route("/")
def index():
    return "Hello World!"


@app.route("/box", methods=["GET"])
def list_boxes() -> str:
    response = "<p>Here are the boxes!</p>"
    response += "<ul>"
    for color, balls in boxes.items():
        response += f"<li> {color} box - {balls} balls</li>"
    response += "</ul>"
    return response


@app.route("/box/<string:color>", methods=["GET", "POST", "DELETE"])
def manage_box(color) -> str:
    """
    Args:
        str:color - create, delete a box of given color, or return numbers of balls in the box, if one exists
    Returns:
        str: message confirming operation or number of balls in a box
    """
    if request.method == "POST":
        if color in boxes:
            return f"Box '{color}' already exists! Delete it first."
        else:
            boxes[color] = 0
            return f"Empty box '{color}' created."
    elif request.method == "DELETE":
        if color in boxes:
            boxes.pop(color)
            return f"Box '{color}' deleted."
        else:
            return f"Cannot delete box '{color}'. No such box."
    elif request.method == "GET":
        if color in boxes:
            return f"Box '{color}' contains {boxes[color]} balls."
        else:
            return f"No box '{color}'! Create it first"


@app.route("/box/<string:color>/<int:balls>", methods=["PUT"])
def store_balls(color, balls) -> str:
    """
    Args:
        str:color, int:balls - update number of balls in the box, if exists
    Returns:
        str: message confirming operation
    """
    if color in boxes:
        boxes[color] = balls
        return f"Box '{color}' contains {balls} balls."
    else:
        return f"No box '{color}'! Create it first"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
