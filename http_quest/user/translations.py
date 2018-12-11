from http_quest.utilities import get_translation_for

en_IN = {
    'user_not_found': 'User could not be found',
    'user_created': 'The user has been created and the password information is sent to them',
    'user_already_exists': 'The user already exists',
    'login_instruction': 'To login, please POST `login_format` on /login',
    'your_email': '<your_email>',
    'your_password': '<your_password>',
    'password_successfully_reset': 'Your password has been successfully reset.',
    'invalid_password_token': 'You have submitted an invalid password token.',
    'password_reset_instructions_sent_to_email': 'Password reset instructions successfully sent to your email address',
    'password_reset_mail_subject': 'Password Reset Instructions',
    'password_reset_mail_message': 'Use this token to reset your password, send a json_format to /user/new_password/<reset_token>',
}

hi_IN = {
    'user_not_found': 'यूजर नहीं मिल सका।',
    'user_created': 'यूजर बनाया गया है और पासवर्ड जानकारी उन्हें भेजी गयी है।',
    'user_already_exists': 'यूजर पहले से मौजूद है।',
    'login_instruction': 'लॉगिन करने के लिए, कृपया `login_format` को POST /login पर भेजें।',
    'your_email': '<आपका_ईमेल>',
    'your_password': '<आपका_पासवर्ड>',
    'password_successfully_reset': 'आपका पासवर्ड सफलतापूर्वक रीसेट कर दिया गया है।',
    'invalid_password_token': 'आपने एक अवैध पासवर्ड टोकन सबमिट किया है।',
    'password_reset_instructions_sent_to_email': 'पासवर्ड रीसेट निर्देश सफलतापूर्वक आपके ईमेल पते पर भेजे गए है।',
    'password_reset_mail_subject': 'पासवर्ड रीसेट सूचना',
    'password_reset_mail_message': 'अपना पासवर्ड रीसेट करने के लिए इस टोकन(token) का प्रयोग करें, json_format को /user/new_password/<reset_token> पर आपका नया पासवर्ड(new_password) भेजें।',
}

strings = {
    'en': en_IN,
    'hi': hi_IN,
}


def get_text(key):
    return get_translation_for(strings, key)
