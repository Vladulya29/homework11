from flask import Flask, render_template
import utils

app = Flask(__name__)

data = utils.load_candidates_from_json("candidates.json")

@app.route('/')
def page_index():
    return render_template("list.html", candidates=data)

@app.route('/candidate/<int:id>')
def page_candidate(id):
    candidate = utils.get_candidates(id)
    return render_template("single.html", candidate=candidate)

@app.route('/search/<candidate_name>')
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_len=len(candidates))

@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_len=len(candidates), skill=skill_name)


app.run()