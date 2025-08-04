from sqlalchemy import create_engine
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import models
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional



def get_user_contents(db: Session, user_id: str):
    return db.query(models.Content).filter(models.Content.user_id == user_id).all()


def create_content(
    db: Session,
    user_id: str,
    raw_text: str,
    media_path: str = None,
    created_at: datetime,
    is_curated: bool = False,
):

    db_content = models.Content(
        user_id=user_id,
        generated_content="",  # Will be updated later
        raw_text=raw_text,
        media_path=media_path,
        created_at=created_at,
        is_curated=is_curated,
    )
    # Validate (optional)
    if not raw_text:
        raise HTTPException(status_code=400, detail="raw_text cannot be empty")

    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content


def create_business_profile(
    db: Session,
    user_id: str,
    business_name: str,
    description: str,
    website: str,
    created_at: datetime,
    tone: Optional[str] = "professional"

):

    db_business_profile = models.BusinessProfile(
        user_id=user_id,
        business_name=business_name,
        description=description,
        website=website,
        created_at=created_at,
        tone=tone,


    )
    if not business_name:
        raise HTTPException(status_code=400, detail="business_name cannot be empty")
    if not description:
        raise HTTPException(status_code=400, detail="description cannot be empty")

    db.add(db_business_profile)
    db.commit()
    db.refresh(db_business_profile)
    return db_business_profile


def get_business_profile(db: Session, user_id: str):
    return (db.query(models.BusinessProfile)
            .filter(models.BusinessProfile.user_id == user_id)
            .first())



'''
    # Auto-generate curated caption if requested
    text = content.text
    raw_text = content.raw_text
    if content.auto_curate:
        try:
            curator = CaptionCurator(db)
            text = curator.curate_caption(
                user_id=current_user.id, raw_content=content.raw_text
            )
        except Exception as e:
            print(f"caption generation failed: {e}")
            # fall back to original text
            raw_text = content.raw_text

    if content.post_to_x:
        if content.scheduled_time:  # Schedule if scheduled_time is provided
            scheduler.schedule_post(
                content_id=db_content, scheduled_time=content.scheduled_time
            )
            db_content.x_status = "scheduled"
            db.commit()
            db.refresh(db_content)
        else:
            poster = ContentPoster(db)
            if not poster.post_to_x(db_content.id):
                raise HTTPException(status_code=500, detail="could not post to X")
            db.refresh(db_content)

    return db_content




@router.get("/", response_model=List[schemas.Content])
def display_content_uploaded(db: db_dependency, skip: int = 0, limit: int = 10):

    return db.query(models.Content).offset(skip).limit(limit).all()
'''
