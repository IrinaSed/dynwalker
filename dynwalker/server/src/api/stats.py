import random

from sanic.response import HTTPResponse, json
from sanic.request import Request


async def get_stats(request: Request) -> HTTPResponse:
    return json({
        'description': 'Модель хождения от точки до точки.',
        'populations': {
            'species': ['walker', 'interrupter'],
            'fitness': [
                {'walker': random.randint(i, i + 20), 'interrupter': random.randint(80 - i, 100 - i)} for i in range(100)
            ],
        },
    })
