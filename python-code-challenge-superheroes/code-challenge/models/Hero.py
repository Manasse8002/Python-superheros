class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)
    # Define the relationship with HeroPower
    hero_powers = db.relationship('HeroPower', back_populates='hero')