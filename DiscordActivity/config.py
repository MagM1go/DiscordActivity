import aiohttp
from abc import ABC, abstractmethod


class ActivityRequest(ABC):
    @abstractmethod
    async def post_request(self, _id: int) -> None: ...


class Config:

    def activity(self, target_application_id: int, max_age: int = 604800, max_uses: int = 100) -> None:
        return {
            'max_age': max_age,
            'max_uses': 100,
            'target_application_id': target_application_id,
            'target_type': 2,
            'temporary': False,
            'validate': None
        }
    
class Request(aiohttp.ClientSession, ActivityRequest):

    def __init__(self, request_data: dict, activities_config: Config):
        self.request_data = request_data
        self.activities_config = activities_config
        super().__init__()
    
    async def post_request(self, _id: int) -> None:
        response = await self.request(**self.request_data, json=self.activities_config.activity(target_application_id=_id))
        return await response.json()
