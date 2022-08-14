"""empty message

Revision ID: ebcc99a15321
Revises: a85e68376bbe
Create Date: 2022-08-14 23:32:45.034428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebcc99a15321'
down_revision = 'a85e68376bbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('ShoporGarden', sa.Boolean(), nullable=True),
    sa.Column('seedingDate', sa.DateTime(), nullable=True),
    sa.Column('postCode', sa.String(length=10), nullable=True),
    sa.Column('forSale', sa.Boolean(), nullable=True),
    sa.Column('energyPlan', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('greenhouses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bookedForSale', sa.Boolean(), nullable=True),
    sa.Column('recordDateTime', sa.String(length=200), nullable=True),
    sa.Column('LightRelay', sa.Boolean(), nullable=True),
    sa.Column('LightCurrent', sa.Boolean(), nullable=True),
    sa.Column('FanRelay', sa.Boolean(), nullable=True),
    sa.Column('FanCurrent', sa.Boolean(), nullable=True),
    sa.Column('OutsideTemp', sa.Integer(), nullable=True),
    sa.Column('InsideTemp', sa.Integer(), nullable=True),
    sa.Column('Lightsensor', sa.Boolean(), nullable=True),
    sa.Column('AirheaterRelay', sa.Boolean(), nullable=True),
    sa.Column('AirHeaterCurrent', sa.Boolean(), nullable=True),
    sa.Column('WaterPumpCurrent', sa.Boolean(), nullable=True),
    sa.Column('WaterHeaterRelay', sa.Boolean(), nullable=True),
    sa.Column('WaterHeaterCurrent', sa.Boolean(), nullable=True),
    sa.Column('WaterTemp', sa.Integer(), nullable=True),
    sa.Column('AirPumpCurrent', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('greenhouses')
    op.drop_table('user')
    # ### end Alembic commands ###
