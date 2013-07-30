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

Revision ID: 4da0c5f79a9c
Revises: None
Create Date: 2013-07-28 12:28:03.091587

"""

# revision identifiers, used by Alembic.
revision = '4da0c5f79a9c'
down_revision = None

from alembic import op
import sqlalchemy as sa


YESNO_VALUES = ['yes', 'no']
TYPE_VALUES = ['friend', 'user', 'peer']

SIP_TRANSPORT_VALUES = ['udp', 'tcp', 'udp,tcp', 'tcp,udp']
SIP_DTMFMODE_VALUES = ['rfc2833', 'info', 'shortinfo', 'inband', 'auto']
SIP_DIRECTMEDIA_VALUES = ['yes', 'no', 'nonat', 'update']
SIP_PROGRESSINBAND_VALUES = ['yes', 'no', 'never']
SIP_SESSION_TIMERS_VALUES = ['accept', 'refuse', 'originate']
SIP_SESSION_REFRESHER_VALUES = ['uac', 'uas']
SIP_CALLINGPRES_VALUES = ['allowed_not_screened', 'allowed_passed_screen',
                          'allowed_failed_screen', 'allowed',
                          'prohib_not_screened', 'prohib_passed_screen',
                          'prohib_failed_screen', 'prohib']

IAX_REQUIRECALLTOKEN_VALUES = ['yes', 'no', 'auto']
IAX_ENCRYPTION_VALUES = ['yes', 'no', 'aes128']
IAX_TRANSFER_VALUES = ['yes', 'no', 'mediaonly']


def upgrade():
    op.create_table(
        'sippeers',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False,
                  autoincrement=True),
        sa.Column('name', sa.String(40), nullable=False, unique=True),
        sa.Column('ipaddr', sa.String(45)),
        sa.Column('port', sa.Integer),
        sa.Column('regseconds', sa.Integer),
        sa.Column('defaultuser', sa.String(40)),
        sa.Column('fullcontact', sa.String(80)),
        sa.Column('regserver', sa.String(20)),
        sa.Column('useragent', sa.String(20)),
        sa.Column('lastms', sa.Integer),
        sa.Column('host', sa.String(40)),
        sa.Column('type', sa.Enum(*TYPE_VALUES)),
        sa.Column('context', sa.String(40)),
        sa.Column('permit', sa.String(95)),
        sa.Column('deny', sa.String(95)),
        sa.Column('secret', sa.String(40)),
        sa.Column('md5secret', sa.String(40)),
        sa.Column('remotesecret', sa.String(40)),
        sa.Column('transport', sa.Enum(*SIP_TRANSPORT_VALUES)),
        sa.Column('dtmfmode', sa.Enum(*SIP_DTMFMODE_VALUES)),
        sa.Column('directmedia', sa.Enum(*SIP_DIRECTMEDIA_VALUES)),
        sa.Column('nat', sa.String(29)),
        sa.Column('callgroup', sa.String(40)),
        sa.Column('pickupgroup', sa.String(40)),
        sa.Column('language', sa.String(40)),
        sa.Column('disallow', sa.String(200)),
        sa.Column('allow', sa.String(200)),
        sa.Column('insecure', sa.String(40)),
        sa.Column('trustrpid', sa.Enum(*YESNO_VALUES)),
        sa.Column('progressinband', sa.Enum(*SIP_PROGRESSINBAND_VALUES)),
        sa.Column('promiscredir', sa.Enum(*YESNO_VALUES)),
        sa.Column('useclientcode', sa.Enum(*YESNO_VALUES)),
        sa.Column('accountcode', sa.String(40)),
        sa.Column('setvar', sa.String(200)),
        sa.Column('callerid', sa.String(40)),
        sa.Column('amaflags', sa.String(40)),
        sa.Column('callcounter', sa.Enum(*YESNO_VALUES)),
        sa.Column('busylevel', sa.Integer),
        sa.Column('allowoverlap', sa.Enum(*YESNO_VALUES)),
        sa.Column('allowsubscribe', sa.Enum(*YESNO_VALUES)),
        sa.Column('videosupport', sa.Enum(*YESNO_VALUES)),
        sa.Column('maxcallbitrate', sa.Integer),
        sa.Column('rfc2833compensate', sa.Enum(*YESNO_VALUES)),
        sa.Column('mailbox', sa.String(40)),
        sa.Column('session-timers', sa.Enum(*SIP_SESSION_TIMERS_VALUES)),
        sa.Column('session-expires', sa.Integer),
        sa.Column('session-minse', sa.Integer),
        sa.Column('session-refresher', sa.Enum(*SIP_SESSION_REFRESHER_VALUES)),
        sa.Column('t38pt_usertpsource', sa.String(40)),
        sa.Column('regexten', sa.String(40)),
        sa.Column('fromdomain', sa.String(40)),
        sa.Column('fromuser', sa.String(40)),
        sa.Column('qualify', sa.String(40)),
        sa.Column('defaultip', sa.String(45)),
        sa.Column('rtptimeout', sa.Integer),
        sa.Column('rtpholdtimeout', sa.Integer),
        sa.Column('sendrpid', sa.Enum(*YESNO_VALUES)),
        sa.Column('outboundproxy', sa.String(40)),
        sa.Column('callbackextension', sa.String(40)),
        sa.Column('timert1', sa.Integer),
        sa.Column('timerb', sa.Integer),
        sa.Column('qualifyfreq', sa.Integer),
        sa.Column('constantssrc', sa.Enum(*YESNO_VALUES)),
        sa.Column('contactpermit', sa.String(95)),
        sa.Column('contactdeny', sa.String(95)),
        sa.Column('usereqphone', sa.Enum(*YESNO_VALUES)),
        sa.Column('textsupport', sa.Enum(*YESNO_VALUES)),
        sa.Column('faxdetect', sa.Enum(*YESNO_VALUES)),
        sa.Column('buggymwi', sa.Enum(*YESNO_VALUES)),
        sa.Column('auth', sa.String(40)),
        sa.Column('fullname', sa.String(40)),
        sa.Column('trunkname', sa.String(40)),
        sa.Column('cid_number', sa.String(40)),
        sa.Column('callingpres', sa.Enum(*SIP_CALLINGPRES_VALUES)),
        sa.Column('mohinterpret', sa.String(40)),
        sa.Column('mohsuggest', sa.String(40)),
        sa.Column('parkinglot', sa.String(40)),
        sa.Column('hasvoicemail', sa.Enum(*YESNO_VALUES)),
        sa.Column('subscribemwi', sa.Enum(*YESNO_VALUES)),
        sa.Column('vmexten', sa.String(40)),
        sa.Column('autoframing', sa.Enum(*YESNO_VALUES)),
        sa.Column('rtpkeepalive', sa.Integer),
        sa.Column('call-limit', sa.Integer),
        sa.Column('g726nonstandard', sa.Enum(*YESNO_VALUES)),
        sa.Column('ignoresdpversion', sa.Enum(*YESNO_VALUES)),
        sa.Column('allowtransfer', sa.Enum(*YESNO_VALUES)),
        sa.Column('dynamic', sa.Enum(*YESNO_VALUES)),
        sa.Column('path', sa.String(256)),
        sa.Column('supportpath', sa.Enum(*YESNO_VALUES))
    )
    op.create_index('sippeers_name', 'sippeers', ['name'])
    op.create_index('sippeers_name_host', 'sippeers', ['name', 'host'])
    op.create_index('sippeers_ipaddr_port', 'sippeers', ['ipaddr', 'port'])
    op.create_index('sippeers_host_port', 'sippeers', ['host', 'port'])

    op.create_table(
        'iaxfriends',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False,
                  autoincrement=True),
        sa.Column('name', sa.String(40), nullable=False, unique=True),
        sa.Column('type', sa.Enum(*TYPE_VALUES)),
        sa.Column('username', sa.String(40)),
        sa.Column('mailbox', sa.String(40)),
        sa.Column('secret', sa.String(40)),
        sa.Column('dbsecret', sa.String(40)),
        sa.Column('context', sa.String(40)),
        sa.Column('regcontext', sa.String(40)),
        sa.Column('host', sa.String(40)),
        sa.Column('ipaddr', sa.String(40)),
        sa.Column('port', sa.Integer),
        sa.Column('defaultip', sa.String(20)),
        sa.Column('sourceaddress', sa.String(20)),
        sa.Column('mask', sa.String(20)),
        sa.Column('regexten', sa.String(40)),
        sa.Column('regseconds', sa.Integer),
        sa.Column('accountcode', sa.String(20)),
        sa.Column('mohinterpret', sa.String(20)),
        sa.Column('mohsuggest', sa.String(20)),
        sa.Column('inkeys', sa.String(40)),
        sa.Column('outkeys', sa.String(40)),
        sa.Column('language', sa.String(10)),
        sa.Column('callerid', sa.String(100)),
        sa.Column('cid_number', sa.String(40)),
        sa.Column('sendani', sa.Enum(*YESNO_VALUES)),
        sa.Column('fullname', sa.String(40)),
        sa.Column('trunk', sa.Enum(*YESNO_VALUES)),
        sa.Column('auth', sa.String(20)),
        sa.Column('maxauthreq', sa.Integer),
        sa.Column('requirecalltoken', sa.Enum(*IAX_REQUIRECALLTOKEN_VALUES)),
        sa.Column('encryption', sa.Enum(*IAX_ENCRYPTION_VALUES)),
        sa.Column('transfer', sa.Enum(*IAX_TRANSFER_VALUES)),
        sa.Column('jitterbuffer', sa.Enum(*YESNO_VALUES)),
        sa.Column('forcejitterbuffer', sa.Enum(*YESNO_VALUES)),
        sa.Column('disallow', sa.String(200)),
        sa.Column('allow', sa.String(200)),
        sa.Column('codecpriority', sa.String(40)),
        sa.Column('qualify', sa.String(10)),
        sa.Column('qualifysmoothing', sa.Enum(*YESNO_VALUES)),
        sa.Column('qualifyfreqok', sa.String(10)),
        sa.Column('qualifyfreqnotok', sa.String(10)),
        sa.Column('timezone', sa.String(20)),
        sa.Column('adsi', sa.Enum(*YESNO_VALUES)),
        sa.Column('amaflags', sa.String(20)),
        sa.Column('setvar', sa.String(200))
    )
    op.create_index('iaxfriends_name', 'iaxfriends', ['name'])
    op.create_index('iaxfriends_name_host', 'iaxfriends', ['name', 'host'])
    op.create_index('iaxfriends_name_ipaddr_port', 'iaxfriends',
                    ['name', 'ipaddr', 'port'])
    op.create_index('iaxfriends_ipaddr_port', 'iaxfriends', ['ipaddr', 'port'])
    op.create_index('iaxfriends_host_port', 'iaxfriends', ['host', 'port'])

    op.create_table(
        'voicemail',
        sa.Column('uniqueid', sa.Integer, primary_key=True, nullable=False,
                  autoincrement=True),
        sa.Column('context', sa.String(80), nullable=False),
        sa.Column('mailbox', sa.String(80), nullable=False),
        sa.Column('password', sa.String(80), nullable=False),
        sa.Column('fullname', sa.String(80)),
        sa.Column('alias', sa.String(80)),
        sa.Column('email', sa.String(80)),
        sa.Column('pager', sa.String(80)),
        sa.Column('attach', sa.Enum(*YESNO_VALUES)),
        sa.Column('attachfmt', sa.String(10)),
        sa.Column('serveremail', sa.String(80)),
        sa.Column('language', sa.String(20)),
        sa.Column('tz', sa.String(30)),
        sa.Column('deletevoicemail', sa.Enum(*YESNO_VALUES)),
        sa.Column('saycid', sa.Enum(*YESNO_VALUES)),
        sa.Column('sendvoicemail', sa.Enum(*YESNO_VALUES)),
        sa.Column('review', sa.Enum(*YESNO_VALUES)),
        sa.Column('tempgreetwarn', sa.Enum(*YESNO_VALUES)),
        sa.Column('operator', sa.Enum(*YESNO_VALUES)),
        sa.Column('envelope', sa.Enum(*YESNO_VALUES)),
        sa.Column('sayduration', sa.Integer),
        sa.Column('forcename', sa.Enum(*YESNO_VALUES)),
        sa.Column('forcegreetings', sa.Enum(*YESNO_VALUES)),
        sa.Column('callback', sa.String(80)),
        sa.Column('dialout', sa.String(80)),
        sa.Column('exitcontext', sa.String(80)),
        sa.Column('maxmsg', sa.Integer),
        sa.Column('volgain', sa.Numeric(precision=5, scale=2)),
        sa.Column('imapuser', sa.String(80)),
        sa.Column('imappassword', sa.String(80)),
        sa.Column('imapserver', sa.String(80)),
        sa.Column('imapport', sa.String(8)),
        sa.Column('imapflags', sa.String(80)),
        sa.Column('stamp', sa.DateTime())
    )
    op.create_index('voicemail_mailbox', 'voicemail', ['mailbox'])
    op.create_index('voicemail_context', 'voicemail', ['context'])
    op.create_index('voicemail_mailbox_context', 'voicemail', ['mailbox', 'context'])
    op.create_index('voicemail_imapuser', 'voicemail', ['imapuser'])


def downgrade():
    op.drop_table('sippeers')
    op.drop_table('iaxfriends')
    op.drop_table('voicemail')
