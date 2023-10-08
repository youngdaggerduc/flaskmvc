from App.database import db

class KarmaRanking(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    karmaID = db.Column(db.Integer, nullable=False)
    upVotes = db.Column(db.Integer, nullable=False, default=0)
    downVotes = db.Column(db.Integer, nullable=False, default=0)
    karmaScore = db.Column(db.Float, nullable=False)
    reviewID = db.Column(db.Integer, db.ForeignKey('reviews.id'), nullable=False)

    def __init__(self, karmaID, upVotes, downVotes, karmaScore, reviewID):
        self.karmaID = karmaID
        self.upVotes = upVotes
        self.downVotes = downVotes
        self.karmaScore = karmaScore
        self.reviewID = reviewID
    
    def to_json(self):
        return {
            'id': self.id,
            'karmaID': self.karmaID,
            'upVotes': self.upVotes,
            'downVotes': self.downVotes,
            'karmaScore': self.karmaScore,
            'reviewID': self.reviewID,
        }
