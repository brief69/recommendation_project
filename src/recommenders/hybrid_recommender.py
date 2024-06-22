from .personalize_recommender import PersonalizeRecommender
from ..models.tf_lite_model import load_tf_lite_model, predict_with_tf_lite
from ..ml_kit.firebase_ml_kit import get_recommendations_from_firebase

class HybridRecommender:
    def __init__(self):
        self.personalize = PersonalizeRecommender()
        self.tf_lite_model = load_tf_lite_model()

    def get_recommendations(self, user_id, user_data):
        # Amazon Personalizeからの推奨
        personalize_recs = self.personalize.get_recommendations(user_id)
        
        # TensorFlow Liteモデルからの推奨
        tf_lite_recs = predict_with_tf_lite(self.tf_lite_model, user_data)
        
        # Firebase ML Kitからの推奨
        firebase_recs = get_recommendations_from_firebase(user_data)
        
        # 3つの推奨結果を組み合わせて最終的な推奨リストを生成
        final_recs = self.combine_recommendations(personalize_recs, tf_lite_recs, firebase_recs)
        
        return final_recs

    def combine_recommendations(self, personalize_recs, tf_lite_recs, firebase_recs):
        # 推奨結果を組み合わせるロジックを実装
        # 例：重み付け、ランキング、フィルタリングなど
        final_recs = personalize_recs + tf_lite_recs + firebase_recs  # 単純な結合例
        return final_recs
