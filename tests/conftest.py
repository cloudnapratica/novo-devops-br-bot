import boto3
import json
from moto import mock_ssm
import os
import pytest
import requests_mock

YT_API_KEY_SSM = os.environ['YT_API_KEY_SSM']
YT_LIST_ID_SSM = os.environ['YT_LIST_ID_SSM']
YT_NEXT_PAGE_TOKEN_SSM = os.environ['YT_NEXT_PAGE_TOKEN_SSM']
TELEGRAM_BOT_TOKEN_SSM = os.environ['TELEGRAM_BOT_TOKEN_SSM']
TELEGRAM_CHAT_ID_SSM = os.environ['TELEGRAM_CHAT_ID_SSM']


@pytest.fixture(scope='module')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope='function')
def ssm(aws_credentials):
    with mock_ssm():
        ssm = boto3.client('ssm')
        for parameter in [YT_API_KEY_SSM, YT_LIST_ID_SSM, YT_NEXT_PAGE_TOKEN_SSM, TELEGRAM_BOT_TOKEN_SSM, TELEGRAM_CHAT_ID_SSM]:
            ssm.put_parameter(
                Name=parameter,
                Value='test',
                Type='String'
            )
        yield ssm


@pytest.fixture(scope='function')
def web_requests():
    with requests_mock.Mocker() as web_requests:
        web_requests.get(
            "https://www.googleapis.com:443/youtube/v3/playlistItems?part=snippet&playlistId=test&maxResults=1&pageToken=test&key=test",
            text=json.dumps(
                {
                    "nextPageToken": "CAEQAA",
                    "items": [
                        {
                            "snippet": {
                                "resourceId": {
                                    "videoId": "jke_qf6SgAg"
                                }
                            }
                        }
                    ]
                }
            )
        )
        web_requests.post(
            "https://api.telegram.org/bottest/sendMessage?chat_id=test&text=%23FiqueEmCasaConf%0A%20https%3A//www.youtube.com/watch%3Fv%3Djke_qf6SgAg",
            text=''
        )
