WordOnTheStreet is a real-time public sentiment analysis web application. It fetches recent Reddit comments discussing any user-specified topic or keyword and evaluates public sentiment using the VADER sentiment analysis engine.

---

How It Works:<br>
WordOnTheStreet utilizes VADER (*Valence Aware Dictionary and sEntiment Reasoner*), a lexicon and rule-based sentiment analysis tool specifically tuned for social media text.<br><br>
Known Limitations:<br>
Please treat scores as an aggregate snapshot rather than an absolute truth:<br>
1. Targeting Ambiguity: Rule-based tools score sentence emotion as a whole rather than who the emotion is directed toward (e.g., *"The ban on {KEYWORD} is terrible"* scores negatively even if the user is defending the keyword).
2. Sarcasm & Slang: Sarcastic comments, ironical memes, and obscure online acronyms can bypass dictionary rules.
3. Demographic Bias: Results reflect active Reddit commenters and may not represent global offline public opinion.
4. Language: VADER works natively only on English text. It relies on a fixed, human-curated English sentiment lexicon and specific grammatical rules tuned for English social media.


---

Project Structure:<br>

WordOnTheStreet/<br>
├── app.py                      # Flask backend & Reddit API fetching logic <br>
├── requirements.txt            # Python dependencies <br>
├── templates/<br>
│   └── index.html              # HTML5 UI, CSS, and dynamic JS gradient logic<br>
└── README.md                   # Project documentation

---

How to Run Locally:<br><br>
Prerequisites:<br>
Make sure you have Python 3.8+ installed on your system<br><br>

1. Clone the Repository:<br>
git clone [https://github.com/Daksh2k5/WordOnTheStreet.git](https://github.com/Daksh2k5/WordOnTheStreet.git)<br>
cd WordOnTheStreet<br>

2. Install Dependencies:<br>
pip install -r requirements.txt<br>
python -c "import nltk; nltk.download('vader_lexicon')"<br><br>

3. Run the Application:<br>
python app.py<br>

4. Access in Web Browser:<br>
Open your browser and navigate to:<br>
http://127.0.0.1:5000