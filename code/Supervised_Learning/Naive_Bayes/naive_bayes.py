from sklearn.naive_bayes import MultinomialNB

# データの生成
# X_trainは特徴量のデータセット
X_train = [
    [1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,1,0,0,0,0,0,0,0,0,0]
]

model = MultinomialNB()
# y_predは予測されたクラス
# 0は宇宙、1は映画
model.fit(X_train, [0,1,0,1,0,1,0])
pridiction = model.predict([[1,0,0,0,0,0,1,0,0,0,0,0]]) 
print(pridiction) # [0]

"""
天気予報の降水確率のように確率そのものを予測したい場合には向かない。
文脈によって単語の意味が変わるとき、すべての特徴量は独立しているという仮定が単純には成り立たない。
別のモデルを必要とする。
 隠れマルコフモデル (HMM)、条件付き確率場 (CRF)、再帰神経ネットワーク (RNN) とその拡張 (LSTM, GRU)、 トランスフォーマーモデルなどがある。

"""