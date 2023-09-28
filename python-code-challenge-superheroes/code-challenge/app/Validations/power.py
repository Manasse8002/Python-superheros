strength = db.Column(db.String(20), nullable=False)

from sqlalchemy import orm, exc

def validate_strength(context, strength):
    if strength not in ['Strong', 'Weak', 'Average']:
        raise exc.ValidationError("Strength must be 'Strong', 'Weak', or 'Average'.")

class HeroPower(db.Model):
    # Other fields...
    strength = db.Column(db.String(20), nullable=False, validate=validate_strength)
    # Other columns...

