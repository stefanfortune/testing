import tweepy
import os
from dotenv import load_dotenv
from .database.models import Post, XCredentials
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from tweepy.media import Media, MEDIA_FIELDS

from tweepy.tweet import (
    PUBLIC_TWEET_FIELDS, ReferencedTweet, Tweet, TWEET_FIELDS
)
from tweepy.user import User, USER_FIELDS

load_dotenv()

class ContentPoster:
    def __init__(self, db: Session):
        self.db = db
        
    def post_to_x(self, post_id: int):
        """Post content to X (Twitter)"""
        post = self.db.query(Post).filter(Post.id == post_id).first()
        if not post:
            return False
        
        # Get user's X credentials
        creds = self.db.query(XCredentials).filter(XCredentials.user_id == post.user_id).first()
        if not creds:
            return False
        
        # Initialize Twitter API
        auth = tweepy.OAuth1UserHandler(
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            creds.access_token,
            creds.access_token_secret
        )
        api = tweepy.API(auth)
          
        try:
            # Post with optional media
            if post.media_path:
                media = api.media_upload(post.media_path)
                tweet = api.update_status(status=post.text, media_ids=[media.media_id])
            else:
                tweet = api.update_status(status=post.text)
                
            # Update content status
            post.posted_to_x = datetime.now(timezone.utc)
            post.x_post_id = tweet.id_str
            post.x_status = 'posted'
            self.db.commit()
            return True
            
        except tweepy.TweepyException as e:
            print(f"X posting failed: {e}")
            return False