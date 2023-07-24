from flask import current_app

from ..models import Top100Scores
from ..repositories.database import db


def get_top_documents(n):
    """Get the top N documents with the highest scores.

    Args:
        n (int): The number of documents to return.

    Returns:
        A list of TopScores objects, each representing a document and its score.
    """
    return db.session.query(Top100Scores).limit(n).all()
