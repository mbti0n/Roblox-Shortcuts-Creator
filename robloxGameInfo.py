import re, requests, json

def robloxFind(urlInput):
    match = re.search(r"/games/(\d+)", urlInput)
    if not match:
        raise ValueError

    placeId = match.group(1)

    # Get universe ID
    getUniverseId = requests.get(f"https://apis.roblox.com/universes/v1/places/{placeId}/universe")
    universeId = json.loads(getUniverseId.text)["universeId"]

    uriScheme = f"roblox://placeId={placeId}"

    # Get thumbnail URL
    getThumbnailURLRaw = requests.get(f"https://thumbnails.roblox.com/v1/games/icons?universeIds={universeId}&size=512x512&format=Png")
    getThumbnailURL = json.loads(getThumbnailURLRaw.text)["data"][0]["imageUrl"]
    
    # Get game name (without emojis / special characters)
    getName = urlInput.rstrip("/").split("/")[-1].replace("-", " ")
    
    return uriScheme, getThumbnailURL, getName, placeId

