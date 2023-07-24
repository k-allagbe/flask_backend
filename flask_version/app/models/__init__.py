import os

from sqlalchemy import Date, Float, Text
from sqlalchemy.dialects.postgresql import UUID

from ..repositories.database import db


class Top100Scores(db.Model):
    __tablename__ = f"{os.getenv('DB_TOP_100_VIEW')}"
    __table_args__ = {"schema": os.getenv("DB_SCHEMA_2"), "extend_existing": True}

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    url = db.Column(Text, nullable=True)
    title = db.Column(Text, nullable=True)
    lang = db.Column(db.String(2), nullable=True)
    html_content = db.Column(Text, nullable=True)
    last_crawled = db.Column(Text, nullable=True)
    last_updated = db.Column(Text, nullable=True)
    last_updated_date = db.Column(Date, nullable=True)
    score = db.Column(Float, nullable=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "url": self.url,
            "title": self.title,
            "lang": self.lang,
            "html_content": self.html_content,
            "last_crawled": self.last_crawled,
            "last_updated": self.last_updated,
            "last_updated_date": self.last_updated_date.isoformat()
            if self.last_updated_date
            else None,
            "score": self.score,
        }
