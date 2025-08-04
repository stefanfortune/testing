from openai import OpenAI
from sqlalchemy.orm import Session
from .database.models import BusinessProfile
from dotenv import load_dotenv
import os

load_dotenv()

# Configure with your OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")
model = "deepseek/deepseek-r1-0528:free"
client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key)
    

def curate_caption(business_name: str, business_description: str, raw_text: str, tone: str = "professional")-> str:
    prompt = f"""
    **Business Profile**:
    name: {business_name}
    description: {business_description}
    Tone: {tone}    
    **Raw Content**: {raw_text}   
    Create a {tone}-tone social media caption for X that:
    1. Incorporates key elements from the business profile
    2. Transforms the raw content into compelling marketing copy
    3. Includes 1-3 relevant hashtags using: {business_description}
    4. Includes appropriate CTAs and engagement prompts
    5. Is optimized for maximum reach and brand consistency     
    Output ONLY the final caption text.
    """
        
    try:
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://marketing-agent-app.com",
                "X-Title": "Business Marketing Agent",
            },
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert social media marketing assistant skilled at creating engaging, "
                               "platform-optimized captions that drive business results."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=300,
            temperature=0.7
        )
            
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"Caption generation failed: {str(e)}")
        # Fallback to simple caption
        return f"{raw_text}\n\n#YourBusiness" #comeback

# Singleton instance for easy import
#caption_curator = CaptionCurator()

