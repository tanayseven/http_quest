from rest_test.utilities import get_translation_for

en_IN = {
    'user_not_found': 'User could not be found',
    'password_reset_instructions_sent_to_email': 'Password reset instructions successfully sent to your email address',
    'password_reset_mail_subject': 'Password Reset Instructions',
    'password_reset_mail_message': 'Use this token to reset your password, send a json_format to /user/new_password/<reset_token>',
}

hi_IN = {
    'user_not_found': 'यूजर नहीं मिल सका।',
    'password_reset_instructions_sent_to_email': 'पासवर्ड रीसेट निर्देश सफलतापूर्वक आपके ईमेल पते पर भेजे गए है।',
    'password_reset_mail_subject': 'पासवर्ड रीसेट सूचना',
    'password_reset_mail_message': 'अपना पासवर्ड रीसेट करने के लिए इस टोकन(token) का प्रयोग करें, json_format को /user/new_password/<reset_token> पर आपका नया पासवर्ड(new_password) भेजें।',
}

strings = {
    'en-IN': en_IN,
    'hi-IN': hi_IN,
}


def get_text(key):
    return get_translation_for(strings, key)
