from http_quiz.utilities import get_translation_for

en_IN = {
    'root_welcome': 'This is the / . Please go to GET /login for any further activity'
}

hi_IN = {
    'root_welcome': 'यह / है. कृपया किसी और चीज़ के लिए GET /login पर जाएँ।'
}

strings = {
    'en-IN': en_IN,
    'en-US': en_IN,
    'hi-IN': hi_IN,
}


def get_text(key):
    return get_translation_for(strings, key)
