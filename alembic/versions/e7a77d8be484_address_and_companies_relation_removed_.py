"""Address and Companies Relation Removed on User 3 

Revision ID: e7a77d8be484
Revises: d0a8333cf216
Create Date: 2024-10-20 10:50:05.554212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7a77d8be484'
down_revision: Union[str, None] = 'd0a8333cf216'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('geo')
    op.drop_table('companies')
    op.drop_table('addresses')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('addresses_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('street', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('suite', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('zipcode', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], name='addresses_userId_fkey'),
    sa.PrimaryKeyConstraint('id', name='addresses_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('companies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('catchPhrase', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('bs', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], name='companies_userId_fkey'),
    sa.PrimaryKeyConstraint('id', name='companies_pkey')
    )
    op.create_table('geo',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('lat', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('lng', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('addressId', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['addressId'], ['addresses.id'], name='geo_addressId_fkey'),
    sa.PrimaryKeyConstraint('id', name='geo_pkey')
    )
    # ### end Alembic commands ###
