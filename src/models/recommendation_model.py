import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense, Concatenate
from tensorflow.keras.models import Model

def create_recommendation_model(num_users, num_items, embedding_size=50):
    # ユーザー入力
    user_input = Input(shape=(1,), name='user_input')
    user_embedding = Embedding(num_users, embedding_size, name='user_embedding')(user_input)
    user_vec = Flatten(name='flatten_users')(user_embedding)

    # アイテム入力
    item_input = Input(shape=(1,), name='item_input')
    item_embedding = Embedding(num_items, embedding_size, name='item_embedding')(item_input)
    item_vec = Flatten(name='flatten_items')(item_embedding)

    # 特徴量の結合
    concat = Concatenate()([user_vec, item_vec])

    # 全結合層
    fc1 = Dense(128, activation='relu')(concat)
    fc2 = Dense(64, activation='relu')(fc1)
    fc3 = Dense(32, activation='relu')(fc2)

    # 出力層
    output = Dense(1, activation='sigmoid', name='prediction')(fc3)

    model = Model(inputs=[user_input, item_input], outputs=output)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

if __name__ == "__main__":
    model = create_recommendation_model(num_users=10000, num_items=50000)
    model.summary()
    