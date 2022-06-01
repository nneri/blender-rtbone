# blender-rtbone
Blenderでキーフレームにベイクしたリジッドボディアニメーションなどをボーンアニメーションにベイクする

# 使い方の例
1. BlenderのアドオンのCell Fractureを有効にする
2. 壊したいオブジェクトをオブジェクト->クイックエフェクト->Cell Fractureで分割する
3. すべて選択して物理演算タブでリジッドボディ(アクティブ)を有効にする
4. フォースフィールドやパッシブのリジッドボディを配置して計算させる
5. 破壊させたオブジェクトをすべて選択し、オブジェクト->リジッドボディ->キーフレームにベイク
6. 破壊させたオブジェクトをすべて選択した状態でこのスクリプトを実行する
7. 生成されたArmatureのポーズモードから抜けて、先ほどのオブジェクトを全選択しなおして、Ctrl+Jで結合する
8. オブジェクトについたアニメーションは不要なのでキーフレームを全削除する
9. オブジェクトを選択したのち生成されたArmatureをさらに選択してアクティブにしてCtrl+P->空のグループで

# 既知の問題
オブジェクトの回転を最初の段階でいじっているとうまく動作しません

# 予定
コメント書いたり、ペアレントまでするようにしたい
