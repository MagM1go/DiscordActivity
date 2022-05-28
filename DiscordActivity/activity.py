import disnake

from .config import Request, Config

APPS = { 
    'youtube': 755600276941176913,
    'poker': 755827207812677713,
    'betrayal': 773336526917861400,
    'fishing': 814288819477020702,
    'chess': 832012774040141894,
    'letter-tile': 879863686565621790,
    'word-snack': 879863976006127627,
    'doodle-crew': 878067389634314250,
}

class Activity:
    
    def __init__(self, bot):
        self.__token = bot.http.token
    
    async def send_activity(self, voice: disnake.VoiceChannel, name: str):
        requester = Request(
            activities_config=Config(),
            request_data={
                "method": "POST", 
                "url": f"https://discord.com/api/v10/channels/{voice.id}/invites",
                "headers": {'Authorization': f'Bot {self.__token}', 'Content-Type': 'application/json'}
            }
        )
        return await requester.post_request(_id=APPS[name]) 
