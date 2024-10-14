# プロジェクトの立ち上げ方

このプロジェクトはAWS SAMを使用してローカルでLambda関数を実行します。

## 前提条件

- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS SAM CLI](https://aws.amazon.com/serverless/sam/)
- [Docker](https://www.docker.com/)

## セットアップ手順
1.依存関係のインストール
```
pip install -r requirements.txt
```
2.SAMテンプレートをビルド
```
sam build
```
3. ローカルでAPIを起動
```
sam local start-api
```
4. エンドポイントにアクセス
```
curl http://127.0.0.1:3000/hoge
```
## DB接続手順
* DockerImageビルド方法
```
docker-compose build
```

* MySQLコンテナの起動
```
docker-compose up -d
```

* MySQLコンテナへの接続
```
docker exec -it personal_trainer_bot-db-1 mysql -u bot -p
```