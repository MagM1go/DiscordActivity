import disnake

from .config import Request, Config


class Activity:
    
    def __init__(self, bot):
        self.__token = bot.http.token
        self.__config = Config()
        self.requester = Request(
            activities_config=self.__config,
            request_data={
                "method": "POST",
                "headers": {'Authorization': f'Bot {self.__token}', 'Content-Type': 'application/json'}
            }
        )
    
    async def send_activity(self, voice: disnake.VoiceChannel, name: str):
        requester = self.requester.update(url=f"{self.config.BASE_URl}/channels/{voice.id}/invites")
        return await requester.post_request(_id=self.__config.APPS[name])
