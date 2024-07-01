# from sqlalchemy import create_engine, text


# engine = create_engine(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM personal_website.projects"))
#     print(result.all())


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self, user=None, password=None, host=None, port=None, database=None, schema=None, pool_size=None, max_overflow=None, pool_timeout=None):
        self.user = user or 'postgres.qwuqgtmliguvllafbopz'
        self.password = password or '81Cwybvl1M5RZfZQ'
        self.host = host or 'aws-0-ap-south-1.pooler.supabase.com'
        self.port = port or 6543
        self.database = database or 'postgres'
        self.connect_timeout = 5
        self.schema = schema or 'personal_website'
        self.pool_size = pool_size or 10
        self.max_overflow = max_overflow or 10
        self.pool_timeout = pool_timeout or 30

        db_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

        self.db_engine = create_engine(
            db_string,
            connect_args={
                'connect_timeout': self.connect_timeout
            },
            hide_parameters=True,
            pool_timeout=self.pool_timeout,
            pool_size=self.pool_size,
            max_overflow=self.max_overflow
        )

    def get_session(self):
        return sessionmaker(bind=self.db_engine)


# db = DB()
# print(db)


# with db.db_engine.connect() as conn:
#     res = conn.execute(text("SELECT * FROM personal_website.projects"))
#     for a in res:
#         print(a)
