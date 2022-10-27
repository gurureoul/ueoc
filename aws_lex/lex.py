import boto3

DEFAULT_TIMEOUT = 300
BOT_ROLE = "arn:aws:iam::058368937332:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots"
LOCALE = "en_US"
CONFIDENCE_THRESHOLD = 0.40

class AWSLex():
    def __init__(self):
        self.lex = boto3.client('lexv2-models')

    def create_bot(self, name, desc=None, children=False, 
					role=BOT_ROLE, timeout=DEFAULT_TIMEOUT):
        print("Creating Bot")
        bot_names = self.get_bot_names()
        if name not in bot_names:
            response = self.lex.create_bot(
                botName = name,
                description = desc,
                dataPrivacy = {'childDirected': children},
                idleSessionTTLInSeconds = timeout,
                roleArn = role
                )
                
            bot_id = response["botId"]

            status = self.describe(bot_id)['botStatus']
            while status != "Available":
                status = describe(bot_id)['botStatus']
            print("Bot created...")
            self.create_locale(bot_id)	
        else:
            print(f'Bot name: "{name}" is already used')
        
        
    def create_locale(self, bot_id):
        print("Making Locale...")
        response = self.lex.create_bot_locale(
            botId = bot_id,
            botVersion = "DRAFT",
            localeId = LOCALE,
            nluIntentConfidenceThreshold=CONFIDENCE_THRESHOLD,
            voiceSettings={
                'voiceId': 'Ivy'
            }
        )
        status = response['botLocaleStatus']
        while status != "NotBuilt":
            status = self.lex.describe_bot_locale(
                botId = bot_id,
                botVersion = "DRAFT",
                localeId = LOCALE
            )['botLocaleStatus']
        print("Locale Made...")

    def get_bots(self):
        response = self.lex.list_bots()
        bots = []
        for bot in response['botSummaries']:
            bot_name = bot['botName']
            bot_id = bot['botId']
            bots.append((bot_name, bot_id))
        return bots

    def get_bot_names(self):
        bots = self.get_bots()
        bot_names = []
        for bot in bots:
            bot_names.append(bot[0])
        return bot_names

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