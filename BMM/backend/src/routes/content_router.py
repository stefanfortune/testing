from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from ..database.db import (get_user_contents,
                           create_content,
                           create_business_profile,
                           get_business_profile,)
from ..database.models import get_db
from ..authentication import authenticate_and_get_user_details
from ..caption_curator import curate_caption
from ..schemas import CaptionRequest,BusinessProfile,ScheduleRequest
from ..scheduler import schedule_post 
from ..database.models import Post
from ..X_content_poster import ContentPoster


from datetime import datetime

router = APIRouter()

@router.get("/business-profile")
async def my_business_profile(request: Request, db: Session = Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request)
        user_id = user_details.get("user_id")
        business_profile = get_business_profile(db, user_id)
        if not business_profile:
            raise HTTPException(status_code=400, detail="business profile does not exist")
        return business_profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create-business-profile")
async def your_business_profile(request:BusinessProfile, request_obj: Request, db: Session= Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        now = datetime.now()
        new_business_profile = create_business_profile(db=db,
                                                       user_id=user_id,
                                                       business_name=request.business_name,
                                                       description=request.description,
                                                       website=request.website,
                                                       created_at=now,
                                                       tone=request.tone
                                                       )

        db.commit()
        return new_business_profile
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/Create content")
async def generate_content(request: CaptionRequest, request_obj: Request, db: Session = Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        business_profile = get_business_profile(db, user_id)
        if not business_profile:
            business_profile = create_business_profile(db, user_id)
            return business_profile
        generate_caption = curate_caption(
            business_name=request.business_name,
            business_description=request.business_description,
            raw_text=request.raw_text,                                           
            tone=request.tone,
            )
        media_path = request.media_path
        generated_content = generate_caption, media_path
        now = datetime.now()
        new_content = create_content(db=db, user_id=user_id,
                                     raw_text=request.raw_text,
                                     media_path=media_path,
                                     generated_content=generated_content,
                                     created_at=now,
                                     is_curated=True)
        db.commit()
        return new_content.generated_content
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/Content history")
async def content_history(request: Request, db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")
    contents = get_user_contents(db, user_id)
    return {"contents": contents}

    


@router.post("/schedule")
def schdeule_and_post_content(request: ScheduleRequest, request_obj: Request, db: Session=Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")

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
            "scheduled_times": [t.isoformat() for t in scheduled_times],
            "post_results": post_results
        }    
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
 

    
        


