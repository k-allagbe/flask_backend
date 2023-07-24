import random
import uuid

from faker import Faker
from sqlalchemy import create_engine, text

# Set up Faker
fake = Faker()

# Create SQLAlchemy engine
engine = create_engine("postgresql://postgres:password@localhost:5432/stagiaires")

# Open a connection
with engine.begin() as connection:
    # Generate data for the crawl table
    for _ in range(100):
        # Generate random values for the columns
        crawl_id = str(uuid.uuid4())
        url = fake.url()
        title = fake.sentence(nb_words=6)
        lang = fake.random_element(elements=("en", "fr", "es", "de", "it"))
        html_content = fake.text(max_nb_chars=200)
        last_crawled = fake.date_time_this_month(
            before_now=True, after_now=False, tzinfo=None
        )
        last_updated = fake.date_time_this_month(
            before_now=True, after_now=False, tzinfo=None
        )
        last_updated_date = last_updated.date()

        # Build the SQL statement
        crawl_insert = text(
            "INSERT INTO test_schema_2.crawl (id, url, title, lang, html_content, last_crawled, last_updated, last_updated_date) "
            "VALUES (:id, :url, :title, :lang, :html_content, :last_crawled, :last_updated, :last_updated_date)"
        )

        # Execute the SQL statement with the generated values
        connection.execute(
            crawl_insert,
            {
                "id": crawl_id,
                "url": url,
                "title": title,
                "lang": lang,
                "html_content": html_content,
                "last_crawled": last_crawled,
                "last_updated": last_updated,
                "last_updated_date": last_updated_date,
            },
        )

with engine.begin() as connection:
    # Get all IDs from the crawl table
    result = connection.execute(text("SELECT id FROM test_schema_2.crawl"))
    crawl_ids = [row[0] for row in result]

    # Generate data for the score table
    for crawl_id in crawl_ids:
        # Generate random values for the columns
        score = random.uniform(0, 1)
        score_type = random.choice(["recency", "traffic"])

        # Build the SQL statement
        score_insert = text(
            "INSERT INTO test_schema_2.score (entity_id, score, score_type) VALUES (:entity_id, :score, :score_type)"
        )

        # Execute the SQL statement with the generated values
        connection.execute(
            score_insert,
            {
                "entity_id": crawl_id,
                "score": score,
                "score_type": score_type,
            },
        )
