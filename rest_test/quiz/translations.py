from rest_test.utilities import get_translation_for

en_IN = {
    'candidate_token_success': 'Token is successfully generated and sent by email to you and the candidate.',
    'candidate_token_mail_subject': 'Here is your new candidate token to be used for the quiz.',
}

hi_IN = {
    'candidate_token_success': 'टोकन सफलतापूर्वक जेनरेट और आपको और कैंडिडेट को ईमेल द्वारा भेजा गया है।',
    'candidate_token_mail_subject': 'क्विज के लिए उपयोग करने के लिए आपका नया कैंडिडेट टोकन यहां दिया गया है।',
}

strings = {
    'en-IN': en_IN,
    'hi-IN': hi_IN,
}


def get_text(key):
    return get_translation_for(strings, key)
