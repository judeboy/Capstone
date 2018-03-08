from app import app, models, db, ma
from .models import Programs, programs_schema
from flask_apispec import use_kwargs, marshal_with
from webargs import fields
from flask import jsonify



@app.route("/api/all_programs")
def get_progs():
    all_programs = Programs.query.all()
    result = programs_schema.dump(all_programs)
    return jsonify(result.data)

@app.route("/api/sean")
def get_sean():
    all_programs = Programs.query.all()
    result = programs_schema.dump(all_programs)
    arr = []
    length = len(result[0])
    for i in result[0]:
        arr.append(i['GovAgency'])
    return jsonify(arr)

@app.route("/api/gov_agencies")
@use_kwargs({'GovAgency': fields.Str()})
@marshal_with(programs_schema)
def list_agencies():
    return Programs.query.filter_by(GovAgency="Small Business Administration").all()
