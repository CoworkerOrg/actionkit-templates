import datetime

contexts = {
    'signup.html': {
        'filename': 'signup.html',
        'page': {
            'title': 'Signup!',
            'name': 'signup',
            "custom_fields": {
                "entity": "pac"
            }
        },
        'form': {
            'introduction_text': 'Signup now!',
            'user_fields': {
                'first_name': 'Ann'
            }
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         },
            ],

    },
    'signup.smssubscribe': {
        'filename': 'signup.html',
        'page': {
            'title': 'Signup! sms-opt-out',
            'name': 'signup',
            "custom_fields": {
                "entity": "pac",
                "phone_mobile": "opt-out"
            }
        },
        'form': {
            'introduction_text': 'Signup now!',
            'user_fields': {
                'first_name': 'Ann'
            }
        },
        'user_fields': [
            {'field_name': 'name',
             'label_text': 'Name',
             'input_tag': '<input id="id_name" type="text" class="form-control mo-userfield-input ak-has-overlay" name="name" />',
         },
            {'field_name': 'email',
             'label_text': 'Email Address',
             'input_tag': '<input id="id_email" type="text" class="form-control mo-userfield-input ak-has-overlay"  name="email" />',
         },
            {'field_name': 'address1',
             'label_text': 'Street Address',
             'input_tag': '<input id="id_address1" type="text" class="form-control mo-userfield-input ak-has-overlay" />',
         },
            {'field_name': 'zip',
             'label_text': 'ZIP Code',
             'input_tag': '<input id="id_zip" type="text" class="form-control mo-userfield-input ak-has-overlay" name="zip" />',
         },
            {'field_name': 'phone',
             'label_text': 'Phone',
             'input_tag': '<input id="id_phone" type="text" class="form-control mo-userfield-input ak-has-overlay" name="phone" />',
         },
            ],

    },
    'recurring_update.html': {
        'filename': 'recurring_update.html',
        'page': {
            'title': 'Update Account Information',
            'name': 'recurring_page',
            'custom_fields': {
                'proxypassword': 'abc123'
            }

        },
        'logged_in_user': {
            'name': 'Daddy Warbucks',
            'address1': 'Easy Street',
            'email': 'daddy.warbucks@example.com',
            'city': 'New York',
            'state': 'NY',
            'phone': '555-123-1233',
            
        },
        'active': [{ #profile
            'id': '123',
            'payment_processor_information': {
                'use_cse': False,
                'cse_key': '123123',
                'use_tr': True,
            },
            'status': 'active', #get actual data
            'updated_at': datetime.datetime(2016, 1, 1), #get actual data
            'created_at': datetime.datetime(2016, 1, 1), #get actual data
            'start': datetime.datetime(2015, 1, 1), #get actual data
            'payment_count': 10,
            'get_period_display': 'Monthly', #get actual data
            'payment_total_amt': '$200.00', #get actual data
            'amt': '$20',
            'order': {
                'payment_method': 'cc'
            },
            'card_num': '1234',
            'display_expiration_date': '05/2060',
            'next_payment_date': datetime.datetime(2016, 9, 1),
            
        }],
        'inactive': [],
    },
}
