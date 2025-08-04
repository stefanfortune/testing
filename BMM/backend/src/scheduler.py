from celery import Celery
from .database.models import SessionLocal, Post
from datetime import datetime, timezone
from src.X_content_poster import ContentPoster


celery = Celery(__name__, broker='redis://localhost:6379/0')
db = SessionLocal()
@celery.task
def post_content(post_id: int):
    with SessionLocal as db:
        try:
            post = db.query(Post).filter(Post.id == post_id).first()
            if post and post.status == 'scheduled':
                # Post to social media
                success = ContentPoster.post_to_x(
                    post_id=post_id
                )
                
                if success:
                    post.status = 'posted'
                    post.posted_at = datetime.now(timezone.utc)
                    post = Post.query.get(post_id)
                    post.posted = True
                    db.commit()
        finally:
            db.close()

def schedule_post(post_id: int, scheduled_time: datetime):
    # Calculate delay in seconds
    delay = (scheduled_time - datetime.now(timezone.utc)).total_seconds()
    
    if delay > 0:
        post_content.apply_async((post_id,), countdown=delay)
        
        # Update content status
        db = SessionLocal()
        post = db.query(Post).filter(Post.id == post_id).first()
        if post:
            Post.status = 'scheduled'
            db.commit()
        db.close()
        