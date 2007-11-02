from satchmo.configuration import *
from django.utils.translation import ugettext_lazy as _

PAYMENT_MODULES = config_get('PAYMENT', 'MODULES')
PAYMENT_MODULES.add_choice(('PAYMENT_AUTOSUCCESS', _('Auto Success Module')))

PAYMENT_GROUP = ConfigurationGroup('PAYMENT_AUTOSUCCESS', 
    _('Payment Auto Success Module Settings'), 
    requires=PAYMENT_MODULES,
    ordering = 100)

config_register([        
    BooleanValue(PAYMENT_GROUP, 
        'LIVE', 
        description=_("Accept real payments"),
        help_text=_("False if you want to be in test mode"),
        default=False),

    BooleanValue(PAYMENT_GROUP, 
        'EMAIL', 
        description=_("Send order emails"),
        help_text=_("True if you want to send emails to customers on order"),
        default=False),
        
    ModuleValue(PAYMENT_GROUP,
        'MODULE',
        description=_('Implementation module'),
        hidden=True,
        default = 'satchmo.payment.modules.autosuccess'),
        
    StringValue(PAYMENT_GROUP,
        'KEY',
        description=_("Module key"),
        hidden=True,
        default = 'AUTOSUCCESS'),

    StringValue(PAYMENT_GROUP,
        'LABEL',
        description=_('English name for this group on the checkout screens'),
        default = 'Pay Now',
        help_text = _('This will be passed to the translation utility')),

    StringValue(PAYMENT_GROUP,
        'URL_BASE',
        description=_('The url base used for constructing urlpatterns which will use this module'),
        default = '^auto/'),
])
