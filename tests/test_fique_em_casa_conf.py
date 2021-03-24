import json
import os

import pytest

YT_NEXT_PAGE_TOKEN_SSM = os.environ['YT_NEXT_PAGE_TOKEN_SSM']


@pytest.mark.usefixtures("ssm", "requests_mock")
def test_next_video(ssm, requests_mock):
    requests_mock.get(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=test&maxResults=1&pageToken=test&key=test",
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
    requests_mock.post(
        "https://api.telegram.org/bottest/sendMessage?chat_id=test&text=%23FiqueEmCasaConf%0A%0A%20https%3A//www.youtube.com/watch%3Fv%3Djke_qf6SgAg",
        text=''
    )
    from src.fique_em_casa_conf.lambda_function import lambda_handler

    lambda_handler(None, None)

    history = requests_mock.request_history
    assert len(history) == 2

    yt_next_page_token = ssm.get_parameter(
        Name=YT_NEXT_PAGE_TOKEN_SSM
    )

    assert yt_next_page_token['Parameter']['Value'] == 'CAEQAA'


@pytest.mark.usefixtures("ssm", "requests_mock")
def test_last_video(ssm, requests_mock):
    requests_mock.get(
        "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=test&maxResults=1&pageToken=test&key=test",
        text=json.dumps(
            {
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
    requests_mock.post(
        "https://api.telegram.org/bottest/sendMessage?chat_id=test&text=%23FiqueEmCasaConf%0A%0A%20https%3A//www.youtube.com/watch%3Fv%3Djke_qf6SgAg",
        text=''
    )
    from src.fique_em_casa_conf.lambda_function import lambda_handler

    lambda_handler(None, None)

    history = requests_mock.request_history
    assert len(history) == 2

    yt_next_page_token = ssm.get_parameter(
        Name=YT_NEXT_PAGE_TOKEN_SSM
    )

    assert yt_next_page_token['Parameter']['Value'] == 'CAEQAQ'
