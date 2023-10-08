# Import the necessary modules
from App.database import db

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    message = db.Column(db.String(300), nullable=False)
    upvote = db.Column(db.Integer, nullable=True)
    downvote = db.Column(db.Integer, nullable=True)
 
    def __init__(self, student_id, message, upvote=None, downvote=None):
        self.student_id = student_id
        self.message = message
        self.upvote = upvote
        self.downvote = downvote
    
    def to_json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'message': self.message,
            'upvote': self.upvote,
            'downvote': self.downvote,
        }
