from flask import Flask, request, render_template
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key="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")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    # Call Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content
    return render_template('index.html', user_input=user_input, response=response)

if __name__ == '__main__':
    app.run(debug=True)
