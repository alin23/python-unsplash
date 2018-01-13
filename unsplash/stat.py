from unsplash.client import Client
from unsplash.models import Stat as StatModel


class Stat(Client):
    """Unsplash Stat operations."""

    def __init__(self, **kwargs):
        super(Stat, self).__init__(**kwargs)

    async def total(self):
        """
        Get a list of counts for all of Unsplash

        :return [Stat]: The Unsplash Stat.
        """
        url = "/stats/total"
        result = await self._get(url)
        return StatModel.parse(result)

    async def month(self):
        """
        Get the overall Unsplash stats for the past 30 days.

        :return [Stat]: The Unsplash Stat.
        """
        url = "/stats/month"
        result = await self._get(url)
        return StatModel.parse(result)
