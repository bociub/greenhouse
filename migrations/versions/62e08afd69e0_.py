"""empty message

Revision ID: 62e08afd69e0
Revises: 76580e5eb1d9
Create Date: 2022-08-11 00:20:08.994811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62e08afd69e0'
down_revision = '76580e5eb1d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'testtime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('testtime', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
