"""User custom word

Revision ID: 50c4c73abfb6
Revises: 6916858de03d
Create Date: 2022-06-12 03:10:20.624008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50c4c73abfb6'
down_revision = '6916858de03d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userword',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('word', sa.String(), nullable=True),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('ipa', sa.String(), nullable=True),
    sa.Column('mean', sa.String(), nullable=True),
    sa.Column('cluster', sa.String(), nullable=True),
    sa.Column('frequency', sa.String(), nullable=True),
    sa.Column('lemma', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userword')
    # ### end Alembic commands ###
