from pydantic import BaseModel

class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    key: str
    long_url: str
    short_url: str
