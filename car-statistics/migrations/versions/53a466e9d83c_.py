"""empty message

Revision ID: 53a466e9d83c
Revises: 
Create Date: 2018-09-16 20:17:01.395220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53a466e9d83c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('confirmed_date', sa.DateTime(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('files',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('hash_name', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('file_owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subsets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subset_name', sa.String(), nullable=False),
    sa.Column('hash_name', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('subset_rel', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['files.id'], ),
    sa.ForeignKeyConstraint(['subset_rel'], ['subsets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subsets')
    op.drop_table('files')
    op.drop_table('users')
    # ### end Alembic commands ###