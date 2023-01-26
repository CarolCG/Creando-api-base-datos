"""empty message

Revision ID: 1ba9208ee399
Revises: d11aa8fc734b
Create Date: 2023-01-26 15:12:55.090945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ba9208ee399'
down_revision = 'd11aa8fc734b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('personajes_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'personajes', ['personajes_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('personajes_id')

    # ### end Alembic commands ###
