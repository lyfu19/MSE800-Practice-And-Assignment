from pydantic import BaseModel

class SocialMediaPlatform(BaseModel):
    name: str
    follower_count: int
    description: str
    country: str
