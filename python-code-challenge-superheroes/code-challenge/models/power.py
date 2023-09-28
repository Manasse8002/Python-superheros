class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    # Define the relationship with HeroPower
    hero_powers = db.relationship('HeroPower', back_populates='power')