from pydantic import BaseModel, Field
from datetime import datetime, time
from typing import Optional,List

# Post Schemas


class PostBase(BaseModel):
    platform: str 
    scheduled_time:datetime


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    timestamp: datetime = Field(default_factory=datetime.now)
    owner_id: int

    class Config:
        from_attributes = True


class BusinessProfileBase(BaseModel):
    business_name: str
    description: str
    #industry: Optional[str] = None
    website: Optional[str] = None
    tone: Optional[str] = "professional"


class BusinessProfileCreate(BusinessProfileBase):
    pass

class BusinessProfile(BusinessProfileBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ContentBase(BaseModel): 
    text: str
    raw_text: str
    media_path: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    auto_curate: bool = Field(False, description="Auto curate caption")
    post_to_x: bool = Field(False, description="Post to X immediately or schedule time")
    

class ContentCreate(ContentBase):
    pass

class Content(ContentBase):
    id: int
    user_id: int
    created_at: datetime
    posted_to_x: Optional[datetime] = None
    x_post_id: Optional[str]= None
    x_status: Optional[str] = None
    is_curated: bool = Field(False, description="Whether the content is curated")
    
    
    class Config:
        from_attributes = True



class CaptionRequest(BaseModel):
    business_name: str
    business_description: str
    raw_text: str
    media_path: Optional[str] = None
    tone: Optional[str] = "professional"  # professional, casual, humorous



class ScheduleBase(BaseModel):
    id: int
    post_id: int
    scheduled_time: datetime
    timezone: str
    created_at: datetime

    class Config:
        from_attributes = True


class ScheduleRequest(ScheduleBase):
    
    frequency: str  # 'once', 'twice', 'three', 'five'
    random: bool = False
    start_time: Optional[time] = None
    interval_hours: Optional[int] = None
    platforms: List[str] = Field(..., description="Platforms to post to: ['x','instagram','both']")
    timestamp: datetime = Field(default_factory=datetime.now)  #check

    class config:
        arbitrary_types_allowed=True
    


class Socials(BaseModel):
    post_to_x: bool = False
    post_to_instagram: bool = False
    



