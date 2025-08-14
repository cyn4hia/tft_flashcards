from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

flashcards = [
    {"question": "Aatrox", "answer": "Mighty Mech", "answer2": "Heavyweight", "answer3": "Juggernaut", "image": "images/aatrox.jpeg"},
    {"question": "Ahri", "answer": "Star Guardian", "answer2": "Sorcerer", "answer3": " ", "image": "images/ahri.jpeg"},
    {"question": "Akali", "answer": "Supreme Cells", "answer2": "Executioner", "answer3": " ", "image": "images/akali.jpg"},
    {"question": "Ashe", "answer": "Crystal Gambit", "answer2": "Duelist", "answer3": " ", "image": "images/ashe.jpg"},
    {"question": "Braum", "answer": "The Champ", "answer2": "Luchador", "answer3": "Bastion", "image": "images/braum.jpg"},
    {"question": "Caitlyn", "answer": "Battle Academia", "answer2": "Sniper", "answer3": " ", "image": "images/cait.jpg"},
    {"question": "Darius", "answer": "Supreme Cells", "answer2": "Heavyweight", "answer3": " ", "image": "images/darius.jpg"},
    {"question": "Dr. Mundo", "answer": "Luchador", "answer2": "Juggernaut", "answer3": " ", "image": "images/mundo.jpg"},
    {"question": "Ezreal", "answer": "Battle Academia", "answer2": "Prodigy", "answer3": " ", "image": "images/ez.jpeg"},
    {"question": "Garen", "answer": "Battle Academia", "answer2": "Bastion", "answer3": " ", "image": "images/garen.jpeg"},
    {"question": "Gnar", "answer": "Luchador", "answer2": "Sniper", "answer3": " ", "image": "images/gnar.jpeg"},
    {"question": "Gangplank", "answer": "Mighty Mech", "answer2": "Duelist", "answer3": " ", "image": "images/gp.jpeg"},
    {"question": "Gwen", "answer": "Soul Fighter", "answer2": "Sorcerer", "answer3": " ", "image": "images/gwen.jpeg"},
    {"question": "Janna", "answer": "Crystal Gambit", "answer2": "Protector", "answer3": "Strategist", "image": "images/janna.jpeg"},
    {"question": "Jarvan IV", "answer": "Mighty Mech", "answer2": "Strategist", "answer3": " ", "image": "images/jarvan.jpeg"},
    {"question": "Jayce", "answer": "Battle Academia", "answer2": "Heavyweight", "answer3": " ", "image": "images/jayce.jpeg"},
    {"question": "Jhin", "answer": "Wraith", "answer2": "Sniper", "answer3": " ", "image": "images/jhin.jpeg"},
    {"question": "Kai'sa", "answer": "Supreme Cells", "answer2": "Duelist", "answer3": " ", "image": "images/kaisa.jpeg"},
    {"question": "Kalista", "answer": "Soul Fighter", "answer2": "Executioner", "answer3": " ", "image": "images/kalista.jpeg"},
    {"question": "Karma", "answer": "Mighty Mech", "answer2": "Sorcerer", "answer3": " ", "image": "images/karma.jpeg"},
    {"question": "Katarina", "answer": "Battle Academia", "answer2": "Executioner", "answer3": " ", "image": "images/kat.jpeg"},
    {"question": "Kayle", "answer": "Wraith", "answer2": "Duelist", "answer3": " ", "image": "images/kayle.jpeg"},
    {"question": "Kennen", "answer": "Supreme Cells", "answer2": "Sorcerer", "answer3": "Protector", "image": "images/kennen.jpeg"},
    {"question": "Kobuko", "answer": "Mentor", "answer2": "Heavyweight", "answer3": " ", "image": "images/kob.jpeg"},
    {"question": "K'sante", "answer": "Wraith", "answer2": "Protector", "answer3": " ", "image": "images/ksante.jpeg"},
    {"question": "Lee sin", "answer": " ", "answer2": "Stancemaster (duelist, executioner, juggernaut)", "answer3": " ", "image": "images/lee.jpeg"},
    {"question": "Leona", "answer": "Battle Academia", "answer2": "Protector", "answer3": " ", "image": "images/leona.jpeg"},
    {"question": "Lucian", "answer": "Mighty Mech", "answer2": "Sorcerer", "answer3": " ", "image": "images/lucian.jpeg"},
    {"question": "Lulu", "answer": " ", "answer2": "Monster Trainer", "answer3": " ", "image": "images/lulu.jpeg"},
    {"question": "Malphite", "answer": "The Crew", "answer2": "Protector", "answer3": " ", "image": "images/malph.jpeg"},
    {"question": "Malzahar", "answer": "Wraith", "answer2": "Prodigy", "answer3": " ", "image": "images/malz.jpeg"},
    {"question": "Naafiri", "answer": "Soul Fighter", "answer2": "Juggernaut", "answer3": " ", "image": "images/naafiri.jpeg"},
    {"question": "Neeko", "answer": "Star Guardian", "answer2": "Protector", "answer3": " ", "image": "images/neeko.jpeg"},
    {"question": "Poppy", "answer": "Star Guardian", "answer2": "Heavyweight", "answer3": " ", "image": "images/poppy.jpeg"},
    {"question": "Rakan", "answer": "Battle Academia", "answer2": "Protector", "answer3": " ", "image": "images/rakan.jpeg"},
    {"question": "Rell", "answer": "Star Guardian", "answer2": "Bastion", "answer3": " ", "image": "images/rell.jpeg"},
    {"question": "Ryze", "answer": "Mighty Mech", "answer2": "Executioner", "answer3": " ", "image": "images/ryze.jpeg"},
    {"question": "Samira", "answer": "Soul Fighter", "answer2": "Edgelord", "answer3": " ", "image": "images/samira.jpeg"},
    {"question": "Senna", "answer": "Mighty Mech", "answer2": "Executioner", "answer3": " ", "image": "images/senna.jpeg"},
    {"question": "Seraphine", "answer": "Star Guardian", "answer2": "Prodigy", "answer3": " ", "image": "images/seraphine.jpeg"},
    {"question": "Sett", "answer": "Soul Fighter", "answer2": "Juggernaut", "answer3": " ", "image": "images/sett.jpeg"},
    {"question": "Shen", "answer": "The Crew", "answer2": "Bastion", "answer3": "Edgelord", "image": "images/shen.jpeg"},
    {"question": "Sivir", "answer": "The Crew", "answer2": "Sniper", "answer3": " ", "image": "images/sivir.jpeg"},
    {"question": "Swain", "answer": "Crystal Gambit", "answer2": "Sorcerer", "answer3": "Bastion", "image": "images/swain.jpeg"},
    {"question": "Syndra", "answer": "Crystal Gambit", "answer2": "Star Guardian", "answer3": "Prodigy", "image": "images/syndra.jpeg"},
    {"question": "Twisted Fate", "answer": "The Crew", "answer2": "Rouge Captain", "answer3": " ", "image": "images/tf.jpeg"},
    {"question": "Udyr", "answer": "Mentor", "answer2": "Duelist", "answer3": "Juggernaut", "image": "images/udyr.jpeg"},
    {"question": "Varus", "answer": "Wraith", "answer2": "Sniper", "answer3": " ", "image": "images/varus.jpeg"},
    {"question": "Vi", "answer": "Crystal Gambit", "answer2": "Juggernaut", "answer3": " ", "image": "images/vi.jpeg"},
    {"question": "Viego", "answer": "Soul Fighter", "answer2": "Duelist", "answer3": " ", "image": "images/viego.jpeg"},
    {"question": "Volibear", "answer": "Luchador", "answer2": "Edgelord", "answer3": " ", "image": "images/voli.jpeg"},
    {"question": "Xayah", "answer": "Star Guardian", "answer2": "Edgelord", "answer3": " ", "image": "images/xayah.jpeg"},
    {"question": "Xin Zhao", "answer": "Soul Fighter", "answer2": "Bastion", "answer3": " ", "image": "images/xin.jpeg"},
    {"question": "Yasuo", "answer": "Mentor", "answer2": "Edgelord", "answer3": " ", "image": "images/yas.jpeg"},
    {"question": "Yone", "answer": "Mighty Mech", "answer2": "Edgelord", "answer3": " ", "image": "images/yone.jpeg"},
    {"question": "Yuumi", "answer": "Battle Academia", "answer2": "Prodigy", "answer3": " ", "image": "images/yuumi.jpeg"},
    {"question": "Zac", "answer": "Wraith", "answer2": "Heavyweight", "answer3": " ", "image": "images/zac.jpeg"},
    {"question": "Ziggs", "answer": "The Crew", "answer2": "Strategist", "answer3": " ", "image": "images/ziggs.jpeg"},
    {"question": "Zyra", "answer": "Crystal Gambit", "answer2": "Rosemother", "answer3": " ", "image": "images/zyra.jpeg"},




]   

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/get_flashcards")

def get_flashcards():
    shuffled = flashcards[:]
    random.shuffle(shuffled)
    return jsonify(shuffled)

if __name__ == "__main__":
    app.run(debug=True)
