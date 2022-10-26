import boto3

DEFAULT_TIMEOUT = 300
BOT_ROLE = "arn:aws:iam::058368937332:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots"
LOCALE = "en_US"
CONFIDENCE_THRESHOLD = 0.40

class AWSLex():
    def __init__(self):
        pass

    def get_bots(self):
        lex = boto3.client('lexv2-models')
        response = lex.list_bots()
        bots = []
        for bot in response['botSummaries']:
            bot_name = bot['botName']
            bot_id = bot['botId']
            bots.append((bot_name, bot_id))
        return bots