from app import db, ma

class Programs(db.Model):
    __tablename__= "programs"

    id = db.Column(db.Integer, primary_key=True, index=True)
    ProgTitle = db.Column(db.String(1000), unique=True)
    ProgNumber = db.Column(db.String(1000), unique=True)
    GovAgency = db.Column(db.String(1000))
    PubDate = db.Column(db.String(1000))
    AgencyShort = db.Column(db.String(1000))
    WebURL = db.Column(db.String(1000), unique=True)

    def __init__(self, ProgTitle, ProgNumber, GovAgency, PubDate, AgencyShort, WebURL):
        self.ProgTitle = ProgTitle
        self.AgencyShort = AgencyShort
        self.ProgNumber = ProgNumber
        self.GovAgency = GovAgency
        self.PubDate = PubDate
        self.WebURL = WebURL

    def __repr__(prog):
        return '<Programs {}>'.format(prog.ProgTitle)

class ProgramsSchema(ma.Schema):
    class Meta:
        fields = ('ProgTitle',
        'AgencyShort',
        'ProgNumber',
        'GovAgency',
        'PubDate',
        'WebURL')

program_schema = ProgramsSchema()
programs_schema = ProgramsSchema(many=True)
