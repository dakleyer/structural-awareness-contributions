"""Responses API adapter, standard library only; no default model or credentials."""
import json
import urllib.error
import urllib.request

ENDPOINT = 'https://api.openai.com/v1/responses'
FIELDS = {
    'action': {'type': 'string', 'enum': ['authority', 'applicability', 'reports', 'wait',
                                       'commit', 'requalify', 'inspect', 'submit', 'stop']},
    'task': {'type': ['string', 'null'], 'enum': ['T0', 'T1', None]},
    'basis': {'type': 'array', 'items': {'type': 'string'}},
    'decision_id': {'type': ['string', 'null']},
    'attempt_id': {'type': ['string', 'null']},
    'total': {'type': ['integer', 'null']},
    'until': {'type': ['integer', 'null']},
}
TOOL = {'type': 'function', 'name': 'step', 'description': 'Query or act in the bounded task environment.',
        'strict': True, 'parameters': {'type': 'object', 'properties': FIELDS,
                                     'required': list(FIELDS), 'additionalProperties': False}}


class ModelAccessError(RuntimeError):
    pass


class ResponsesClient:
    def __init__(self, model, key, instructions, timeout=45, max_output_tokens=2048):
        self.model, self.key, self.instructions = model, key, instructions
        self.timeout, self.max_output_tokens = timeout, max_output_tokens

    def respond(self, items, previous=None):
        body = {'model': self.model, 'instructions': self.instructions, 'input': items,
                'tools': [TOOL], 'tool_choice': 'auto', 'parallel_tool_calls': False,
                'max_output_tokens': self.max_output_tokens, 'store': True}
        if previous:
            body['previous_response_id'] = previous
        request = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode(),
            headers={'Authorization': 'Bearer ' + self.key, 'Content-Type': 'application/json'}, method='POST')
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = response.read(4_000_001)
                if len(data) > 4_000_000:
                    raise ModelAccessError('response_size_limit')
                return json.loads(data)
        except urllib.error.HTTPError as exc:
            # Do not persist headers/keys or potentially sensitive provider error bodies.
            raise ModelAccessError('http_status_' + str(exc.code)) from None
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
            raise ModelAccessError(type(exc).__name__) from None
