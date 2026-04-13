from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database
import main  # We import main to potentially access the bot object
import uvicorn
import requests
from fastapi.responses import RedirectResponse

CLIENT_ID = "1491352704931467415"
CLIENT_SECRET = "_zIn9Hgnc5YO-ifjyMfS_rJjVPKDfea4"
REDIRECT_URI = "http://localhost:8000/auth/callback"

app = FastAPI(title="Dev Ticketing System Bridge")

@app.get("/login")
async def login():
    # URL to send the user to Discord
    discord_url = (
        f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify"
    )
    return RedirectResponse(discord_url)

@app.get("/auth/callback")
async def auth_callback(code: str):
    # Exchange the code for an access token
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    token = r.json().get('access_token')

    # Use the token to get User Info
    user_r = requests.get("https://discord.com/api/users/@me", headers={
        'Authorization': f'Bearer {token}'
    })
    user_data = user_r.json()

    # This returns the ID and Username to the browser/Java app
    return {
        "id": user_data['id'],
        "username": user_data['username']
    }
# Data model for the claim request
class ClaimRequest(BaseModel):
    thread_id: int
    user_id: int
    username: str

@app.get("/tickets/open")
async def get_open_tickets():
    """Fetches all tickets currently in OPEN status."""
    try:
        status_groups = database.get_threads_by_status()
        return status_groups.get("OPEN", [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tickets/claim")
async def claim_ticket(request: ClaimRequest):
    """Claims a ticket for a user in the database."""
    try:
        # 1. Check if the ticket is still open
        thread = database.get_thread(request.thread_id)
        if not thread:
            raise HTTPException(status_code=404, detail="Ticket not found")
        
        if thread['status'] != 'OPEN':
            raise HTTPException(status_code=400, detail="Ticket is already claimed or closed")

        # 2. Update the database using your existing logic
        # We need to update the status and the claimed_by fields
        conn = database.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE threads 
            SET status = 'CLAIMED', 
                claimed_by_id = ?, 
                claimed_by_username = ? 
            WHERE thread_id = ?
        """, (request.user_id, request.username, request.thread_id))
        conn.commit()
        conn.close()

        return {"message": f"Ticket {request.thread_id} claimed by {request.username}"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Run the API on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
