"""Responses API transport. No retries, default model, SDK or secret logging."""
import json
import urllib.error
import urllib.request

ENDPOINT = 'https://api.openai.com/v1/responses'
FIELDS = {
    'action': {'type':'string', 'enum':['resolve','read','deliver','stop']},
    'frame': {'type':['string','null'], 'enum':['FRAME_A','FRAME_B',None]},
    'receipts': {'type':'array', 'items':{'type':'string'}},
    'total': {'type':['integer','null']},
    'signal_id': {'type':['string','null']},
}
TOOL = dict(type='function', name='step', strict=True,
            description='Query evidence, read synthetic report values, deliver a report, or stop. Unused fields must be null or an empty list. signal_id optionally acknowledges an actually received advisory; it grants no permission.',
            parameters=dict(type='object', properties=FIELDS, required=list(FIELDS), additionalProperties=False))


class AccessError(RuntimeError):
    pass


class Client:
    def __init__(self, model, key, instructions):
        self.model, self.key, self.instructions = model, key, instructions
        self.timeout, self.max_output_tokens = 45, 2048

    def body(self, items, previous=None):
        result = dict(model=self.model, instructions=self.instructions, input=items,
                      tools=[TOOL], tool_choice='auto', parallel_tool_calls=False,
                      max_output_tokens=self.max_output_tokens, store=True)
        if previous:
            result['previous_response_id'] = previous
        return result

    def respond(self, items, previous=None):
        request = urllib.request.Request(ENDPOINT, data=json.dumps(self.body(items,previous)).encode(),
                headers={'Authorization':'Bearer '+self.key,'Content-Type':'application/json'}, method='POST')
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read(4_000_001)
                if len(raw)>4_000_000:
                    raise AccessError('response_size_limit')
                return json.loads(raw)
        except urllib.error.HTTPError as exc:
            raise AccessError('http_status_'+str(exc.code)) from None
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
            raise AccessError(type(exc).__name__) from None
