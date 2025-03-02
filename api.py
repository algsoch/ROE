from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import httpx

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def proxy(url: str = None):
    if not url:
        raise HTTPException(status_code=400, detail="URL parameter is required")
    
    try:
        # Fetch data from the provided URL
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        
        # Prepare headers, filtering out ones that FastAPI will set
        headers = {}
        for name, value in response.headers.items():
            if name.lower() not in ("content-length", "content-encoding", "transfer-encoding"):
                headers[name] = value
        
        # Add CORS header
        headers["Access-Control-Allow-Origin"] = "*"
        
        # Return the response with the original content and status code
        return Response(
            content=response.content,
            status_code=response.status_code,
            media_type=response.headers.get("content-type", "text/plain"),
            headers=headers
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching URL: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
if __name__ == "__main__":
    import uvicorn
    from pyngrok import ngrok
    
    # Start a tunnel to port 8000
    public_url = ngrok.connect(8000).public_url
    print(f"Public URL: {public_url}/api")
    
    # Start the server
    uvicorn.run(app, host="127.0.0.1", port=8000)