import pandas as pd
from firebase_admin import firestore

def collect_user_data():
    # Firebaseからユーザーデータを収集
    db = firestore.client()
    users_ref = db.collection('users')
    users_data = users_ref.stream()
    
    # データをパンダスDataFrameに変換
    users_df = pd.DataFrame([doc.to_dict() for doc in users_data])
    return users_df

def preprocess_data(df):
    # データの前処理（正規化、エンコーディングなど）
    processed_df = df.copy()  # dfのコピーを作成
    # ここで必要な前処理を行う
    # 例: processed_df['new_column'] = processed_df['existing_column'].apply(some_function)

    return processed_df
