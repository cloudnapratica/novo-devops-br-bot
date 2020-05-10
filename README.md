# Novo DevOps BR Telegram Bot

> Um bot para o grupo Novo DevOps BR no Telegram

Esse projeto provisiona os recursos utilizados pelo bot do grupo [Novo DevOps BR](https://t.me/novodevopsbr) no Telegram.

## Instalação

Para rodar esse projeto, você vai precisar ter o AWS CDK instalado na sua máquina.

```sh
npm install -g aws-cdk
cdk --version
```

## Ambiente de Desenvolvimento

Para criar um ambiente de desenvolvimento, siga os seguintes passos:

Primeiro, você vai precisar de um ambiente virtual Python.

```
$ python3 -m venv .env
```

Depois que o ambiente estiver criado, você pode ativá-lo executando o comando abaixo.

```
$ source .env/bin/activate
```

Se você estiver utilizando Windows, você pode ativer o ambiente com o comando abaixo.

```
% .env\Scripts\activate.bat
```

Uma vez que o ambiente virtual estiver ativado, você precisa instalar as dependências do projeto executando o seguinte comando:

```
$ pip install -r requirements.txt
$ pip install -r src/fique_em_casa_conf/requirements.txt --target=src/fique_em_casa_conf/ --upgrade
```

O último passo antes de poder fazer o deploy do projeto na AWS é configurar as váriveis de ambiente que indicam em qual conta e em qual região da AWS o deploy deve ser feito:

```
export CDK_DEFAULT_ACCOUNT={ID_DA_SUA_CONTA_NA_AWS}
export CDK_DEFAULT_REGION=sa-east-1
```

Depois que todas as dependências estiverem instaladas, você deve conseguir sintetizar o template CloudFormation com o comando abaixo.

```
$ cdk synth
```

Para adicionar outras dependências, por exemplo outros módulos do CDK, basta adicioná-las a lista `install_requires` no arquivo [setup.py](setup.py) e rodar novamente o comando `pip install -r requirements.txt`.

## Meta

Desenvolvido por Fernando Gonçalves – [LinkedIn](https://www.linkedin.com/in/fgoncalves-io/)

Distribuído sob a licença do [MIT](LICENSE).

## Contribuições

1. Crie um fork desse repositório
2. Crie um _feature branch_ (`git checkout -b feature/fooBar`)
3. Faça o commit das suas mudanças (`git commit -am 'Add some fooBar'`)
4. Faça o push para o seu _feature branch_ (`git push origin feature/fooBar`)
5. Crie um _Pull Request_
