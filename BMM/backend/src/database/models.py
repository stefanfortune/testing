from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text,
    Boolean,
    create_engine
)
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

Database_url = ("sqlite:///database.db")
engine = create_engine(Database_url, echo=True)


class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
#   user_id = Column(Integer, ForeignKey("users.id"))
    user_id = Column(String, nullable=False)
    generated_content = Column(Text, nullable=False)
    raw_text = Column(Text, nullable=False)
    media_path = Column(String(255))  # Path to uploaded media
    is_curated = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    # X posting status
    posted_to_x = Column(DateTime)  # Timestamp when posted
    x_post_id = Column(String(100))  # Twitter's post ID
    x_status = Column(
        String(20), default="pending"
    )  # pending, scheduled, posted, failed
#    user = relationship("User", back_populates="contents")

    """New models Below"""

class BusinessProfile(Base):
    __tablename__ = "business_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    #user_id = Column(Integer, ForeignKey("users.id"))
    user_id = Column(String, nullable=False)
    business_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    industry_niche = Column(String(50))
    website = Column(String(255))
    tone = Column(String(20), default="professional")  # Added tone preference
    hashtags = Column(String(255))  # Brand-specific hashtags
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    
#    user = relationship("User", back_populates="business_profile")




class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(String, nullable=False)
    content = Column(String(280), nullable=False)
    scheduled_time = Column(DateTime)
    platform = Column(String(20), nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    status = Column(String(20), default="pending")
    posted = Column(Boolean, default=False)
#    owner_id = Column(Integer, ForeignKey("users.id"))

#    owner = relationship("User", back_populates="posts")



  

class XCredentials(Base):
    __tablename__ = 'x_credentials'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False, unique=True)
#    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    access_token = Column(String(255), nullable=False)
    access_token_secret = Column(String(255), nullable=False)
    x_user_id = Column(String(100), nullable=False)  # Twitter's user ID
    screen_name = Column(String(100), nullable=False)  # Twitter handle
    
    # Relationship back to User
#    user = relationship("User", back_populates="x_credentials")


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
