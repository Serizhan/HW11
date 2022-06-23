from flask import Flask, request, render_template
from utils import get_candidate
from utils import get_candidates_by_name
from utils import get_candidates_by_skill
from utils import load_candidates_from_json

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страничка"""
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route("/candidate/<int:uid>")
def candidate_page(uid):
    candidate: dict = get_candidate(uid)
    if not candidate:
        return "Нет кандидата"
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidate(candidate_name):
    candidates: list = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<skill_name>")
def search_skill_of_candidate(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill=skill_name)


app.run()
