from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime
"""
テーブルのカラム情報を定義するためのクラスを格納します。
テーブル操作を行う際のレコード生成もこのクラスを通して行います。
今回は神社に対しての「お願い」を格納するためのテーブルを作成したいと思います。
カラム構成は

ID（int：キー情報）
title（String(128)：お願いのタイトル）
body（text：お願いの内容）
date（datetime：お願いの投稿日時） にします。
"""

class OnegaiContent(Base):
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)