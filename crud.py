from sqlalchemy.orm import Session
from . import models, schemas
import logging
import random
import string

logger = logging.getLogger(__name__)

def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    db_url = models.URL(
        target_url=url.target_url,
        is_active=url.is_active,
        key=random_string(6),
        secret_key=random_string(12)
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    logger.info(f"Created URL: {db_url}")
    return db_url

def random_string(length: int) -> str:
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return db.query(models.URL).filter(models.URL.key == url_key).first()
