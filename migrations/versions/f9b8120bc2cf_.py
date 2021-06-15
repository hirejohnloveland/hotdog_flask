"""empty message

Revision ID: f9b8120bc2cf
Revises: f260e9f34f57
Create Date: 2021-06-13 14:46:45.224294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b8120bc2cf'
down_revision = 'f260e9f34f57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu__item', sa.Column('img_url', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('menu__item', 'img_url')
    # ### end Alembic commands ###