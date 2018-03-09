from app import app, models
from .models import Programs, programs_schema
from flask import jsonify, request


@app.route("/")
def get_progs():
    all_programs = Programs.query.all()
    result = programs_schema.dump(all_programs)
    return jsonify(result.data)

@app.route("/api/agency")
def agenciesOnly():
    all_programs = Programs.query.all()
    result = programs_schema.dump(all_programs)
    arr = []
    for i in result[0]:
        arr.append(i["ProgTitle"])
        arr.append(i["GovAgency"])
        arr.append(i["WebURL"])
    return jsonify(arr)

# @app.route("/api/")
# def practice():
#     one_program = Programs.query.all()
#     result = programs_schema.dump(one_program)
#     response = jsonify(result.data.AgencyShort)
#     return response
