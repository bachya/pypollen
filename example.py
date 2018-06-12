"""Run an example script to quickly test."""
import asyncio

from aiohttp import ClientSession

from pypollencom import Client
from pypollencom.errors import RequestError


async def allergens(client: Client) -> None:
    """Output allergen-related information."""
    print('CURRENT ALLERGENS')
    print(await client.allergens.current())

    print()
    print('EXTENDED ALLERGENS')
    print(await client.allergens.extended())

    print()
    print('HISTORIC ALLERGENS')
    print(await client.allergens.historic())

    print()
    print('ALLERGY OUTLOOK')
    print(await client.allergens.outlook())


async def disease(client: Client) -> None:
    """Output disease-related information."""
    print('EXTENDED DISEASE INFO')
    print(await client.disease.extended())


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        await run(websession)


async def run(websession):
    """Run."""
    try:
        # Create a client:
        client = Client('80238', websession)

        # Work with allergen data:
        await allergens(client)

        # Work with disease data:
        print()
        await disease(client)
    except RequestError as err:
        print(err)


asyncio.get_event_loop().run_until_complete(main())