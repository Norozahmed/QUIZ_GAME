from flask import Flask, jsonify, request, render_template, send_from_directory

app = Flask(__name__)

questions = [
    {"id": 1, "question": "What does CPU stand for?", "answer": "central processing unit"},
    {"id": 2, "question": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"id": 3, "question": "What does RAM stand for?", "answer": "random access memory"},
    {"id": 4, "question": "What does PSU stand for?", "answer": "power supply unit"},
    {"id": 5, "question": "What does SSD stand for?", "answer": "solid state drive"},
    {"id": 6, "question": "What does HDD stand for?", "answer": "hard disk drive"},
    {"id": 7, "question": "What does USB stand for?", "answer": "universal serial bus"},
    {"id": 8, "question": "What does BIOS stand for?", "answer": "basic input output system"},
    {"id": 9, "question": "What does OS stand for?", "answer": "operating system"},
    {"id": 10, "question": "What does URL stand for?", "answer": "uniform resource locator"},
    {"id": 11, "question": "What does HTTP stand for?", "answer": "hypertext transfer protocol"},
    {"id": 12, "question": "What does HTTPS stand for?", "answer": "hypertext transfer protocol secure"},
    {"id": 13, "question": "What does HTML stand for?", "answer": "hypertext markup language"},
    {"id": 14, "question": "What does CSS stand for?", "answer": "cascading style sheets"},
    {"id": 15, "question": "What does API stand for?", "answer": "application programming interface"},
    {"id": 16, "question": "What does VPN stand for?", "answer": "virtual private network"},
    {"id": 17, "question": "What does LAN stand for?", "answer": "local area network"},
    {"id": 18, "question": "What does WAN stand for?", "answer": "wide area network"},
    {"id": 19, "question": "What does DNS stand for?", "answer": "domain name system"},
    {"id": 20, "question": "What does SQL stand for?", "answer": "structured query language"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.json
    question_id = data['questionId']
    user_answer = data['answer'].lower()
    
    question = next((q for q in questions if q['id'] == question_id), None)
    
    if question:
        is_correct = user_answer == question['answer']
        return jsonify({
            'isCorrect': is_correct,
            'correctAnswer': question['answer']
        })
    
    return jsonify({'error': 'Question not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)