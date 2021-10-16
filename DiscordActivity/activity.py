import aiohttp
import nextcord
from nextcord.ext import commands
import requests


apps = { 
    'youtube': '755600276941176913',
    'poker': '755827207812677713',
    'betrayal': '773336526917861400',
    'fishing': '814288819477020702',
    'chess': '832012774040141894',
    'letter-tile': '879863686565621790',
    'word-snack': '879863976006127627',
    'doodle-crew': '878067389634314250',
}

class Sessions:

    def __init__(self, **kwargs):
        self._async_session = aiohttp.ClientSession()
        self._session = requests
        self.token = kwargs.get('token')

class AsyncActivity(Sessions):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    async def get_activity(self, activity_name: str, author: nextcord.Member):
        data = {
            'max_age': 604800,
            'max_uses': 100,
            'target_application_id': apps[activity_name],
            'target_type': 2,
            'temporary': False,
            'validate': None
        }
        async with self._async_session.post(f"https://discord.com/api/v8/channels/{author.voice.channel.id}/invites", 
                                    json=data, 
                                    headers={'Authorization': f'Bot {self.token}', 'Content-Type': 'application/json'}
        ) as response:
            code = await response.json()
        return code['code']

class SyncActivity(Sessions):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_activity(self, activity_name: str, author: nextcord.Member):
        data = {
            'max_age': 604800,
            'max_uses': 100,
            'target_application_id': apps[activity_name],
            'target_type': 2,
            'temporary': False,
            'validate': None
        }
        code = self._session.post(f"https://discord.com/api/v8/channels/{author.voice.channel.id}/invites", 
                                    json=data, 
                                    headers={'Authorization': f'Bot {self.token}', 'Content-Type': 'application/json'}
        )
        return code.json()['code']
