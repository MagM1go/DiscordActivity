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

    def __init__(self, **kwargs):
        self.request = kwargs.get('request')
        self.__config = kwargs.get('config')
    
    async def post_request(self, _id: int) -> None:
        response = await self.request(**self.request, json=self.__config.activity(_id))
        return await response.json()
