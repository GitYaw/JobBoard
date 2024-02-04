from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Sacramento, CA',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Raleigh, NC',
    'salary': 'Rs. $110,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote, USA'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Tampa Bay, FL',
    'salary': '$120,000'
  }
]

@app.route("/")
def hello_jobs():
  return render_template('home.html', jobs=JOBS, company='Jobs & Co. Ltd.')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)