"""add assignment association table

Revision ID: 15a8cb5b4837
Revises: 2ec196a9c8ef
Create Date: 2024-04-03 17:40:32.017287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15a8cb5b4837'
down_revision = '2ec196a9c8ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_assignments_employee_id_employees')),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name=op.f('fk_assignments_project_id_projects')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments')
    # ### end Alembic commands ###
