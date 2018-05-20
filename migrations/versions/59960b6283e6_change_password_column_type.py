"""change password column type

Revision ID: 59960b6283e6
Revises: ffc021d174b1
Create Date: 2018-05-20 13:25:12.065736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from http_quiz.app import app
from http_quiz.extensions import db
from http_quiz.user.model import User
from http_quiz.user.user import reset_password_for_user

revision = '59960b6283e6'
down_revision = 'ffc021d174b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users = before_password_column_change()
    op.batch_alter_table('user', sa.Column('password', sa.String(length=64), nullable=True))
    after_password_column_change(users)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users = before_password_column_change()
    op.batch_alter_table('user', sa.Column('password', sa.Binary(length=128), nullable=True))
    after_password_column_change(users)
    # ### end Alembic commands ###


def before_password_column_change():
    users = db.session.query(User).all()
    for user in users:
        user.password = None
        db.session.add(user)
        db.session.commit()
    return users


def after_password_column_change(users):
    with app.app_context():
        for user in users:
            reset_password_for_user(user)