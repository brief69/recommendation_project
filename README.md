# ハイブリッドレコメンデーションシステム

## プロジェクト概要

このプロジェクトは、Amazon Personalize、TensorFlow Lite、およびFirebase ML Kitを組み合わせた高度なハイブリッドレコメンデーションシステムを実装しています。このシステムは、複数のアプローチを統合することで、より正確で個別化された推奨を提供することを目的としています。

## 主要コンポーネント

1. **データ収集と前処理** (`src/data_processing/`)
   - Firebaseからユーザーデータを収集
   - データの前処理と正規化

2. **Amazon Personalize統合** (`src/recommenders/personalize_recommender.py`)
   - Amazon Personalizeを使用した推奨の生成

3. **TensorFlow Liteモデル** (`src/models/tf_lite_model.py`)
   - カスタムTensorFlow Liteモデルの作成と使用

4. **Firebase ML Kit統合** (`src/ml_kit/firebase_ml_kit.py`)
   - Firebase ML Kitを使用したオンデバイス推論

5. **ハイブリッドレコメンダー** (`src/recommenders/hybrid_recommender.py`)
   - 複数のレコメンデーションソースを組み合わせた最終的な推奨の生成

## セットアップ手順

1. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

2. Firebase、Amazon Personalize、TensorFlow Liteの認証情報を設定します。

3. TensorFlow Liteモデルを作成し、`model.tflite`として保存します。

4. Firebase ML Kitにモデルをデプロイします。

## 使用方法

1. データ収集：
   ```python
   from src.data_processing.data_collector import collect_user_data, preprocess_data

   raw_data = collect_user_data()
   processed_data = preprocess_data(raw_data)
   ```

2. レコメンデーションの取得：
   ```python
   from src.recommenders.hybrid_recommender import HybridRecommender

   recommender = HybridRecommender()
   recommendations = recommender.get_recommendations(user_id, user_data)
   ```

## 開発ガイドライン

1. コードスタイル：PEP 8ガイドラインに従ってください。
2. テスト：新機能を追加する際は、対応するユニットテストを`tests/`ディレクトリに追加してください。
3. ドキュメント：関数やクラスには適切なドキュメンテーション文字列を追加してください。

## 今後の改善点

1. モデルの性能評価と最適化
2. より高度な推奨結合アルゴリズムの実装
3. リアルタイムフィードバックの統合
4. スケーラビリティの向上

## ライセンス

このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
