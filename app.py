from flask import Flask, render_template, request, redirect
import openai
import os
import csv

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

def save_lead(name, email):
    with open("leads.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        prompt = request.form.get("prompt")
        save_lead(name, email)
        return redirect(f"/optimize?prompt={prompt}")
    return render_template("index.html")

@app.route("/optimize")
def optimize():
    prompt = request.args.get("prompt")
    optimized_prompt = generate_optimized_prompt(prompt)
    return render_template("result.html", original_prompt=prompt, optimized_prompt=optimized_prompt)

def generate_optimized_prompt(user_prompt):
    system_message = (
        "Sos un experto en creación de prompts para modelos de lenguaje. "
        "Tu tarea es mejorar el siguiente prompt del usuario para que obtenga la mejor respuesta posible."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    app.run(debug=True)