import boto3
import logging
import os
import requests
import urllib

YT_API_KEY_SSM = os.environ['YT_API_KEY_SSM']
YT_LIST_ID_SSM = os.environ['YT_LIST_ID_SSM']
YT_NEXT_PAGE_TOKEN_SSM = os.environ['YT_NEXT_PAGE_TOKEN_SSM']
TELEGRAM_BOT_TOKEN_SSM = os.environ['TELEGRAM_BOT_TOKEN_SSM']
TELEGRAM_CHAT_ID_SSM = os.environ['TELEGRAM_CHAT_ID_SSM']

logger = logging.getLogger()
logger.setLevel(os.getenv('LOGLEVEL') or 'INFO')

ssm = boto3.client('ssm')


def get_ssm_parameter_value(parameter_name):
    logger.debug(f"Retrieving SSM parameter {parameter_name}")
    parameter = ssm.get_parameter(
        Name=parameter_name,
        WithDecryption=True
    )
    logger.debug("Parameter retrieved successfully")
    return parameter['Parameter']['Value']


def get_youtube_video():
    logger.debug("Retrieving video data from YouTube")
    yt_api_key = get_ssm_parameter_value(YT_API_KEY_SSM)
    yt_list_id = get_ssm_parameter_value(YT_LIST_ID_SSM)
    next_page_token = get_ssm_parameter_value(YT_NEXT_PAGE_TOKEN_SSM)
    response = requests.get(
        f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={yt_list_id}&maxResults=1&pageToken={next_page_token}&key={yt_api_key}"
    ).json()
    logger.debug(f"Retrieved the following data: {response}")
    return response


def send_telegram_message(video_id):
    telegram_bot_token = get_ssm_parameter_value(TELEGRAM_BOT_TOKEN_SSM)
    chat_id = get_ssm_parameter_value(TELEGRAM_CHAT_ID_SSM)
    message = f"#FiqueEmCasaConf\n\n https://www.youtube.com/watch?v={video_id}"
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={chat_id}&text={urllib.parse.quote(message)}"
    logger.debug(f"Posting Telegram message to URL {url}")
    requests.post(url).raise_for_status()
    logger.debug("Message sent successfully")


def update_next_page_token(response):
    token = response['nextPageToken'] if 'nextPageToken' in response else 'CAEQAQ'
    logger.debug(f"Updating next page token with value {token}")
    parameter = ssm.put_parameter(
        Name=YT_NEXT_PAGE_TOKEN_SSM,
        Value=token,
        Type='String',
        Overwrite=True
    )
    logger.debug("Token updated successfully")


def lambda_handler(event, context):
    logger.info("Processing request")
    response = get_youtube_video()
    video_id = response['items'][0]['snippet']['resourceId']['videoId']
    send_telegram_message(video_id)
    update_next_page_token(response)
    logger.info("Request processed successfully")
