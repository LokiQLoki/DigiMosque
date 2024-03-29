"""empty message

Revision ID: aa979ce82ea2
Revises: 
Create Date: 2019-08-28 17:58:28.299849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa979ce82ea2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mosques',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('lat', sa.String(), nullable=True),
    sa.Column('lon', sa.String(), nullable=True),
    sa.Column('FA', sa.String(), nullable=True),
    sa.Column('ZU', sa.String(), nullable=True),
    sa.Column('AS', sa.String(), nullable=True),
    sa.Column('MA', sa.String(), nullable=True),
    sa.Column('IS', sa.String(), nullable=True),
    sa.Column('contact', sa.String(), nullable=True),
    sa.Column('image_folder_name', sa.String(), nullable=True),
    sa.Column('uploader_id', sa.String(), nullable=True),
    sa.Column('image_names', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mosques')
    # ### end Alembic commands ###
