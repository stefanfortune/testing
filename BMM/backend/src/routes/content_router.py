from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from ..database.db import (get_user_contents,
                           create_content,
                           create_business_profile,
                           get_business_profile,)
from ..database.models import get_db
from ..authentication import authenticate_and_get_user_details
from ..caption_curator import curate_caption
from ..schemas import CaptionRequest, BusinessProfileCreate, ScheduleRequest
from ..scheduler import schedule_post 
from ..database.models import Post
from ..X_content_poster import ContentPoster


from datetime import datetime

router = APIRouter()

@router.get("/business-profile")
async def my_business_profile(request: Request, db: Session = Depends(get_db)):
    try:
        print("Fetching business profile...")
        user_details = authenticate_and_get_user_details(request)
        user_id = user_details.get("user_id")
        print(f"User ID: {user_id}")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="User ID not found")
            
        business_profile = get_business_profile(db, user_id)
        print(f"Business profile found: {business_profile}")
        
        if not business_profile:
            return {"message": "No business profile found", "profile": None}
        
        return {
            "id": business_profile.id,
            "user_id": business_profile.user_id,
            "business_name": business_profile.business_name,
            "description": business_profile.description,
            "website": business_profile.website,
            "tone": business_profile.tone,
            "created_at": business_profile.created_at
        }
    except Exception as e:
        raise
    except Exception as e:
        print(f"Unexpected error in business profile endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/create-business-profile")
async def your_business_profile(request: BusinessProfileCreate, request_obj: Request, db: Session = Depends(get_db)):
    try:
        print("Creating business profile...")
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        print(f"User ID: {user_id}")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="User ID not found")
            
        # Check if profile already exists
        existing_profile = get_business_profile(db, user_id)
        if existing_profile:
            # Update existing profile instead of creating new one
            existing_profile.business_name = request.business_name
            existing_profile.description = request.description
            existing_profile.website = request.website
            existing_profile.tone = request.tone
            db.commit()
            db.refresh(existing_profile)
            
            return {
                "id": existing_profile.id,
                "user_id": existing_profile.user_id,
                "business_name": existing_profile.business_name,
                "description": existing_profile.description,
                "website": existing_profile.website,
                "tone": existing_profile.tone,
                "created_at": existing_profile.created_at
            }
            
        now = datetime.now()
        new_business_profile = create_business_profile(db=db,
                                                       user_id=user_id,
                                                       business_name=request.business_name,
                                                       description=request.description,
                                                       website=request.website,
                                                       created_at=now,
                                                       tone=request.tone
                                                       )

        return {
            "id": new_business_profile.id,
            "user_id": new_business_profile.user_id,
            "business_name": new_business_profile.business_name,
            "description": new_business_profile.description,
            "website": new_business_profile.website,
            "tone": new_business_profile.tone,
            "created_at": new_business_profile.created_at
        }
    except HTTPException:
        print(f"Error creating business profile: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/create-content")
async def generate_content(request: CaptionRequest, request_obj: Request, db: Session = Depends(get_db)):
    try:
        print("Generating content...")
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        print(f"User ID: {user_id}")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="User ID not found")
            
        business_profile = get_business_profile(db, user_id)
        if not business_profile:
            raise HTTPException(status_code=404, detail="Business profile not found. Please create one first.")
            
        generate_caption = curate_caption(
            business_name=business_profile.business_name,
            business_description=business_profile.description,
            raw_text=request.raw_text,                                           
            tone=business_profile.tone,
            )
        media_path = request.media_path
        generated_content = generate_caption
        now = datetime.now()
        new_content = create_content(db=db, user_id=user_id,
                                     raw_text=request.raw_text,
                                     media_path=media_path,
                                     created_at=now,
                                     is_curated=True)
        
        # Update the generated content
        new_content.generated_content = generated_content
        db.commit()
        db.refresh(new_content)

        return {
            "id": new_content.id,
            "generated_content": generated_content,
            "raw_text": new_content.raw_text,
            "media_path": new_content.media_path,
            "created_at": new_content.created_at
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/content-history")
async def content_history(request: Request, db: Session = Depends(get_db)):
    try:
        print("Fetching content history...")
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        print(f"User ID: {user_id}")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="User ID not found")
            
        contents = get_user_contents(db, user_id)
        
        # Convert to serializable format
        content_list = []
        for content in contents:
            content_list.append({
                "id": content.id,
                "generated_content": content.generated_content,
                "raw_text": content.raw_text,
                "media_path": content.media_path,
                "is_curated": content.is_curated,
                "created_at": content.created_at,
                "posted_to_x": content.posted_to_x,
                "x_post_id": content.x_post_id,
                "x_status": content.x_status
            })
        
        return {"contents": content_list}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error fetching content history: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.post("/schedule")
def schedule_and_post_content(request: ScheduleRequest, request_obj: Request, db: Session = Depends(get_db)):
    try:
        print("Scheduling content...")
        user_details = authenticate_and_get_user_details(request)
        user_id = user_details.get("user_id")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="User ID not found")
            
        contents = get_user_contents(db, user_id)
        return {"contents": contents}
    except Exception as e:
        print(f"Error fetching content history: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    


@router.post("/schedule")
def schdeule_and_post_content(request: ScheduleRequest, request_obj: Request, db: Session=Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        print(f"User ID: {user_id}")

        content = generate_content(request, request_obj, db)
        posts = []
        

        # Generate schedule times
  
        scheduled_times = schedule_post(request)
        platforms = request.platforms
     
        # Create content in DB
        for post_time in scheduled_times:
             posts.append(Post(owner_id=user_id,
                                  content=content,
                                  platform=platforms,
                                  scheduled_time=post_time
            ))       

        db.add(posts)
        db.commit()

           
        # Post to selected platforms
        post_results = []
        for post in posts:
            result = {"post_id": post.id, "platforms": {}}
            
            if 'x' in platforms or 'both' in platforms:
                result["platforms"]["x"] = ContentPoster.post_to_x(post.id, db)
            
            if 'instagram' in platforms or 'both' in platforms:
                result["platforms"]["instagram"] = post_to_instagram(post.id, db)
                pass

            
            post_results.append(result)
            
        
        
        return {
        db.rollback()
        print(f"Error scheduling content: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")