"""remove unnessary fields and tables

Revision ID: a8f9df45ac5c
Revises: 70ad2335f716
Create Date: 2018-05-06 12:55:22.422772

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a8f9df45ac5c'
down_revision = '70ad2335f716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_users')
    op.drop_table('role')
    op.drop_column('user', 'confirmed_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_table('role',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
        sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='role_pkey'),
        sa.UniqueConstraint('name', name='role_name_key'),
    )
    op.create_table('roles_users',
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='roles_users_role_id_fkey'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='roles_users_user_id_fkey'),
    )
    # ### end Alembic commands ###
