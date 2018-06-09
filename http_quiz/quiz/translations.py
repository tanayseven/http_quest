from http_quiz.utilities import get_translation_for

en_IN = {
    'candidate_token_success': 'Token is successfully generated and sent by email to you and the candidate.',
    'candidate_token_mail_subject': 'Here is your new candidate token to be used for the quiz.',
    'candidate_token_mail_body': 'Use the following token as an HTTP header called `Authorization`',
}

hi_IN = {
    'candidate_token_success': 'टोकन सफलतापूर्वक जेनरेट और आपको और कैंडिडेट को ईमेल द्वारा भेजा गया है।',
    'candidate_token_mail_subject': 'क्विज के लिए उपयोग करने के लिए आपका नया कैंडिडेट टोकन यहां दिया गया है।',
    'candidate_token_mail_body': 'निम्नलिखित टोकन का उपयोग `Authorization` नामक HTTP Header के रूप में करें|',
}

strings = {
    'en': en_IN,
    'hi': hi_IN,
}


def get_text(key):
    return get_translation_for(strings, key)
