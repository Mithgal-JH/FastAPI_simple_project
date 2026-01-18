from sqlalchemy import create_engine

SQLALCHAMY_DATABASE = "sqlite:/// ./blog.db"
connect_args = {"check_same_thread": False}

engine = create_engine(SQLALCHAMY_DATABASE, connect_args=connect_args)
