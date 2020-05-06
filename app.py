#!/usr/bin/env python3

from aws_cdk import core

from novo_devops_br_bot.novo_devops_br_bot_stack import NovoDevopsBrBotStack


app = core.App()
NovoDevopsBrBotStack(app, "novo-devops-br-bot")

app.synth()
