from aws_cdk import (
    core,
    aws_events as _events,
    aws_events_targets as _events_targets,
    aws_lambda as _lambda,
    aws_ssm as _ssm
)


class NovoDevopsBrBotStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        yt_api_key = _ssm.StringParameter(
            self,
            'YouTubeApiKey',
            parameter_name=f"/{id}/YouTubeApiKey",
            string_value='PLACEHOLDER'
        )

        yt_list_id = _ssm.StringParameter(
            self,
            'FiqueEmCasaConfPlayListId',
            parameter_name=f"/{id}/YouTubePlayListId",
            string_value='PLf-O3X2-mxDmn0ikyO7OF8sPr2GDQeZXk'
        )

        yt_next_page_token = _ssm.StringParameter(
            self,
            'NextPageToken',
            parameter_name=f"/{id}/NextPageToken",
            string_value='CAEQAQ'
        )

        telegram_bot_token = _ssm.StringParameter(
            self,
            'TelegramBotToken',
            parameter_name=f"/{id}/TelegramBotToken",
            string_value='PLACEHOLDER'
        )

        telegram_chat_id = _ssm.StringParameter(
            self,
            'TelegramChatId',
            parameter_name=f"/{id}/TelegramChatId",
            string_value='PLACEHOLDER'
        )

        function = _lambda.Function(
            self,
            'FiqueEmCasaConfPublisher',
            code=_lambda.Code.asset('src/fique_em_casa_conf/'),
            handler='lambda_function.lambda_handler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            timeout=core.Duration.seconds(30),
            retry_attempts=0,
            environment={
                'YT_API_KEY_SSM': yt_api_key.parameter_name,
                'YT_LIST_ID_SSM': yt_list_id.parameter_name,
                'YT_NEXT_PAGE_TOKEN_SSM': yt_next_page_token.parameter_name,
                'TELEGRAM_BOT_TOKEN_SSM': telegram_bot_token.parameter_name,
                'TELEGRAM_CHAT_ID_SSM': telegram_chat_id.parameter_name

            }
        )
        yt_api_key.grant_read(function)
        yt_list_id.grant_read(function)
        yt_next_page_token.grant_read(function)
        yt_next_page_token.grant_write(function)
        telegram_bot_token.grant_read(function)
        telegram_chat_id.grant_read(function)

        _events.Rule(
            self,
            'FiqueEmCasaConfSchedule',
            description="Sends one video from FiqueEmCasaConf to Telegram every day",
            enabled=True if 'Prod' in id else False,
            schedule=_events.Schedule.expression(
                expression='cron(0 12 * * ? *)'
            ),
            targets=[
                _events_targets.LambdaFunction(function)
            ]
        )

        # TODO: Error notifications
