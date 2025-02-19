from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from src.config import ELEVENLABS_API_KEY, ELEVENLABS_AGENT_ID
# from redis_client import redis_client

app = Flask(__name__)
CORS(app)

HEADERS = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}


# /hello endpoint
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "hello, our API is working..."})


@app.route("/create-agent", methods=["POST"])
def create_agent():
    data = request.json
    
    required_fields = ["name", "voice_id", "model", "temperature", "stability", "style_exaggeration", "system_prompt", "tools"]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    agent = {
        "name": data["name"],
        "voice_id": data["voice_id"],
        "model": data["model"],
        "temperature": data["temperature"],
        "stability": data["stability"],
        "style_exaggeration": data["style_exaggeration"],
        "system_prompt": data["system_prompt"],
        "tools": data["tools"]
    }
    
    # # Simulating agent creation (You can integrate this with a database or external API)
    return jsonify({"message": "Agent created successfully", "agent": agent}), 201
    # Call ElevenLabs API to create the agent
    # create_agent_url = f"https://api.elevenlabs.io/v1/agents"  # This is an example; check ElevenLabs docs for exact URL
    # try:
    #     response = requests.post(create_agent_url, json=agent, headers=HEADERS)
        
    #     if response.status_code == 201:
    #         return jsonify({"message": "Agent created successfully", "agent": response.json()}), 201
    #     else:
    #         return jsonify({"error": "Failed to create agent", "details": response.json()}), response.status_code
    # except requests.exceptions.RequestException as e:
    #     return jsonify({"error": "Error while making request to ElevenLabs", "details": str(e)}), 500



knowledge_bases = {}
@app.route('/knowledge-bases', methods=['POST'])
def add_knowledge_base():
    data = request.json
    
    # Validate input
    required_keys = ["agent_id", "files", "chunk_size", "chunk_overlap"]
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"Missing required field: {key}"}), 400
    
    agent_id = data["agent_id"]
    
    # Store the knowledge base (simulating ElevenLabs API)
    knowledge_bases[agent_id] = {
        "files": data["files"],
        "chunk_size": data["chunk_size"],
        "chunk_overlap": data["chunk_overlap"]
    }
    
    return jsonify({"message": "Knowledge base added successfully", "agent_id": agent_id}), 200

# /start-conversation endpoint
# @app.route("/start-conversation", methods=["POST"])
# def start_conversation():
#     user_id = request.json["user_id"]
#     session_id = f"session_{user_id}"
    
#     redis_client.set(session_id, "active", ex=3600)  # Expires in 1 hour

#     return jsonify({"message": "Conversation started", "session_id": session_id})



# /stop-conversation endpoint
# @app.route("/stop-conversation", methods=["POST"])
# def stop_conversation():
#     session_id = request.json["session_id"]

#     redis_client.delete(session_id)
#     return jsonify({"message": "Conversation stopped"})



# debug mode
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)