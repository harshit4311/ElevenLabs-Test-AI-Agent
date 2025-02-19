import os

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "your-api-key-here")
ELEVENLABS_AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID", "your-agent-id-here")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
JWT_SECRET = os.getenv("JWT_SECRET", "your-jwt-secret-here")