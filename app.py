from flask import Flask, request, jsonify, send_from_directory
from PythonTeacherBot import PythonTeacherBot

app = Flask(__name__)
bot = PythonTeacherBot()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message'].lower().strip()
    level = data['level']
    bot.level = level

    if user_input == "quit":
        return jsonify({"response": "Thank you for learning Python! Goodbye!"})
    elif user_input == "resource":
        bot.provide_resource()
        return jsonify({"response": f"Here's a great resource for {'beginner' if level == '1' else 'intermediate' if level == '2' else 'advanced'} level: {bot.resources['beginner' if level == '1' else 'intermediate' if level == '2' else 'advanced']}"})
    elif user_input == "topic":
        topics = ", ".join(bot.topics[level])
        return jsonify({"response": f"Sure, let's change the topic. Here are some suggestions:\n{topics}\nWhat would you like to discuss?"})
    else:
        response = bot.generate_response(user_input)
        return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)