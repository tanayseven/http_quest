new_candidate_token_schema = {
    'type': 'object',
    'required': ['name', 'email', 'quiz_type', 'quiz_name'],
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'quiz_type': {'type': 'string'},
        'quiz_name': {'type': 'string'},
    },
    "additionalProperties": False,
}
