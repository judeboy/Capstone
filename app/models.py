from app import db, ma

class Programs(db.Model):
    __tablename__= "programs"

    id = db.Column(db.Integer, primary_key=True, index=True)
    ProgTitle = db.Column(db.String(1000),)
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

    def __repr__(self):
        return '<Programs {}>'.format(self.ProgTitle)

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

class Admin(db.Model):
    __tablename__= "admin"

    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return '<Admin {}>'.format(self.username)

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('Username',
        'Password',
        )

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)
