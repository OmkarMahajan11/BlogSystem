"""empty message

Revision ID: e96acc60a75e
Revises: e8117629ddae
Create Date: 2020-09-23 00:10:40.878079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e96acc60a75e'
down_revision = 'e8117629ddae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commentsTree',
    sa.Column('ancestor', sa.Integer(), nullable=False),
    sa.Column('descendant', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ancestor'], ['comments.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['descendant'], ['comments.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ancestor', 'descendant')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commentsTree')
    op.drop_table('comments')
    # ### end Alembic commands ###
