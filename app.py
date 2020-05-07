#!/usr/bin/env python3
import os
from aws_cdk import core

from novo_devops_br_bot.novo_devops_br_bot_stack import NovoDevopsBrBotStack

env = core.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]
)

app = core.App()
dev = NovoDevopsBrBotStack(app, "NovoDevOpsBRBot-Dev", env=env)
core.Tag.add(dev, 'app', 'novo-devops-br-bot')
core.Tag.add(dev, 'env', 'dev')

prod = NovoDevopsBrBotStack(app, "NovoDevOpsBRBot-Prod", env=env)

core.Tag.add(prod, 'app', 'novo-devops-br-bot')
core.Tag.add(prod, 'env', 'prod')


app.synth()
