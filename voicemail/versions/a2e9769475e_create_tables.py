# Copyright (C) 2013, Russell Bryant
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Create tables

Revision ID: a2e9769475e
Revises: None
Create Date: 2013-07-29 23:43:09.431668

"""

# revision identifiers, used by Alembic.
revision = 'a2e9769475e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'voicemail_messages',
        sa.Column('dir', sa.String(255), nullable=False),
        sa.Column('msgnum', sa.Integer, nullable=False),
        sa.Column('context', sa.String(80)),
        sa.Column('macrocontext', sa.String(80)),
        sa.Column('callerid', sa.String(80)),
        sa.Column('origtime', sa.Integer),
        sa.Column('duration', sa.Integer),
        sa.Column('recording', sa.LargeBinary),
        sa.Column('flag', sa.String(30)),
        sa.Column('category', sa.String(30)),
        sa.Column('mailboxuser', sa.String(30)),
        sa.Column('mailboxcontext', sa.String(30)),
        sa.Column('msg_id', sa.String(40))
    )
    op.create_primary_key('voicemail_messages_dir_msgnum',
            'voicemail_messages', ['dir', 'msgnum'])
    op.create_index('voicemail_messages_dir', 'voicemail_messages', ['dir'])


def downgrade():
    op.drop_table('voicemail_messages')
