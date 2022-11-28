from alchemy.exceptions import AlchemyError
from alchemy.types import Settings, AlchemyApiType, Network

DEFAULT_ALCHEMY_API_KEY = 'demo'
DEFAULT_NETWORK = Network.ETH_MAINNET
DEFAULT_MAX_RETRIES = 5


class AlchemyConfig:
    api_key: str
    network: Network
    max_retries: int
    url: str

    def __init__(self, settings: Settings) -> None:
        self.api_key = settings.get('apiKey', DEFAULT_ALCHEMY_API_KEY)
        self.network = settings.get('network', DEFAULT_NETWORK)
        self.max_retries = settings.get('maxRetries', DEFAULT_MAX_RETRIES)
        self.url = settings.get('url')

    def get_request_url(self, api_type: AlchemyApiType):
        if self.url:
            return self.url
        elif api_type == AlchemyApiType.NFT:
            return f'https://{self.network}.g.alchemy.com/nft/v2/{self.api_key}'
        elif api_type == AlchemyApiType.BASE:
            return f'https://{self.network}.g.alchemy.com/v2/{self.api_key}'
        else:
            raise AlchemyError(f'Wrong api_type: {api_type}')



