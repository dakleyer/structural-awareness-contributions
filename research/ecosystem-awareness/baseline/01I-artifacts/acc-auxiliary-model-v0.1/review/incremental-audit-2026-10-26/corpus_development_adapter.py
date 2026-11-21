"""Producer-side bridge from study #44 to composable resource claims.

Pass the existing intrinsic_abcd module as producer. World and native logs
stay on this producer side; a planning receiver consumes only (Action,budget).
"""
from generative_development import Action, resource_conflicts


def producer_offer(producer, world, record, *, now, minimum=8):
    if record is None:
        raise ValueError('a qualified source record is required')
    valid,reason=producer.receiver_B_valid(producer.public_outline(world),record,record.target,
                                          now=now,extra=record.question_input)
    if not valid:raise ValueError(reason)
    path=producer.path_to(world,record.target)
    logs=producer.source_current_log(world,producer.base_demand(world,minimum))
    amount=record.delivered_if_requested
    loads={};budget={}
    for node in path:
        if not node.source_can_assess:raise ValueError('source cannot assess this path')
        capacity=node.capacity if isinstance(node,producer.Leaf) else node.throughput_ceiling
        if capacity is not None:
            resource=node.name+'@'+node.version
            budget[resource]=max(0,capacity-logs[node.name]);loads[resource]=amount
    action=Action.make(record.target,loads,amount)
    if resource_conflicts((action,),budget):raise ValueError('record exceeds current native headroom')
    return action,budget


def common_budget(offers):
    result={}
    for action,budget in offers:
        for resource,amount in budget.items():
            if resource in result and result[resource]!=amount:
                raise ValueError('shared resource observations disagree: '+resource)
            result[resource]=amount
    return result
