import boto3

class PersonalizeRecommender:
    def __init__(self):
        self.personalize = boto3.client('personalize')
        self.campaign_arn = 'your_campaign_arn'

    def get_recommendations(self, user_id):
        response = self.personalize.get_recommendations(
            campaignArn=self.campaign_arn,
            userId=user_id
        )
        return response['itemList']
