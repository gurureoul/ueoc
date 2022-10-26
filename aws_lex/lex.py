import boto3

DEFAULT_TIMEOUT = 300
BOT_ROLE = "arn:aws:iam::058368937332:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots"
LOCALE = "en_US"
CONFIDENCE_THRESHOLD = 0.40

class AWSLex():
    def __init__(self):
        self.lex = boto3.client('lexv2-models')

    def get_bots(self):
        response = self.lex.list_bots()
        bots = []
        for bot in response['botSummaries']:
            bot_name = bot['botName']
            bot_id = bot['botId']
            bots.append((bot_name, bot_id))
        return bots

    def delete_bot(self,bot_id):
        print("Deleting bot...")
        response = self.lex.delete_bot(
            botId = bot_id,
            skipResourceInUseCheck=True
        )
        try:
            status = response['botStatus']
            while status == 'Deleting':
                status = self.describe(bot_id)['botStatus']
        except:
            pass
        print("Bot deleted...")

    def describe(self, bot_id):
        return self.lex.describe_bot(botId = bot_id)