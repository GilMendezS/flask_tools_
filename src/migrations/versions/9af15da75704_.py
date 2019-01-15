"""empty message

Revision ID: 9af15da75704
Revises: 
Create Date: 2019-01-14 18:07:23.922822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9af15da75704'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.add_column('post', sa.Column('date_modified', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'date_modified')
    op.drop_column('post', 'date_created')
    # ### end Alembic commands ###
