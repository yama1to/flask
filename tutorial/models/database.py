from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

"""
次の５行でDBへの接続情報を定義しています。
上から順に、

database.pyと同じパスにonegai.dbというファイルを絶対パスで定義
SQLiteを利用して1.で定義した絶対パスにDBを構築
DB接続用インスタンスを生成
Baseオブジェクトを生成して、
そこにDBの情報を流し込む
というイメージです。
ここで生成されたBaseオブジェクトを前述のOnegaiContentクラスの引数に渡すことで、
DB接続情報とテーブル定義を紐付けることができます。
逆に言うと、DB接続情報（接続先のDB等）を変えたい場合はdatabase.pyを、
テーブル定義を変えたい場合はmodels.pyをいじればOKということです。

また、最後３行でDB初期化のための関数を定義しています。
import文でDB初期化対象のテーブル定義を指定して、
Base.metadata.create_all(bind=engine)でテーブルを作成しています。

"""
# database.pyと同じパスにonegai.dbというファイルを絶対パスで定義
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'onegai.db')

# SQLiteを利用して1.で定義した絶対パスにDBを構築
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)

# DB接続用インスタンスを生成
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

# Baseオブジェクトを生成して、
Base = declarative_base()

# そこにDBの情報を流し込む
Base.query = db_session.query_property()


def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)