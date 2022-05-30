import aiohttp


class Config:

    BASE_URl = 'https://discord.com/api/v10'
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

    def activity(self, target_application_id: int, max_age: int = 604800, max_uses: int = 100) -> dict:
        return {
            'max_age': max_age,
            'max_uses': 100,
            'target_application_id': target_application_id,
            'target_type': 2,
            'temporary': False,
            'validate': None
        }


class Request:

    def __init__(self, request_data: dict, activities_config: Config):
        self.request_data = request_data
        self.activities_config = activities_config
        self._http = aiohttp.ClientSession()
    
    async def post_request(self, _id: int) -> dict:
        response = await self._http.request(**self.request_data, json=self.activities_config.activity(target_application_id=_id))
        return await response.json()
