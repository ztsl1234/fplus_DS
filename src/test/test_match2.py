import pytest
from src.user import User
from dataclasses import asdict

@pytest.fixture
def user1():
    data_source=[{"id":123, "name":20251009, "email":5,"age":123},
             {"id":124, "name":20251019, "email":5,"age":123},
             {"id":125, "name":20251029, "email":5,"age":123},
             {"id":126, "name":20251109, "email":5,"age":123}
             ]
    
    return [User.from_dict(r) for r in data_source]

@pytest.fixture
def user2():
    data_source=[{"id":123, "name":20251009, "email":5,"age":22},
             {"id":124, "name":20251019, "email":5,"age":123},
             {"id":125, "name":20251029, "email":5,"age":123},
             {"id":127, "name":20251109, "email":5,"age":123}
             ]
    return [User.from_dict(r) for r in data_source]

def index_by_pk(users) -> dict:
    #set of user id, not key-value pair so it is not dict but a set
    #{} can be dict or set depending on content
    #return {u.id for u in users} #set
    return {u.id: u for u in users}

#return missing in second list and data changed in matching id
def diff_users(users1, users2) -> dict:
    #diff in pk (id)
    user1_index_dict=index_by_pk(users1)
    user2_index_dict=index_by_pk(users2)

    diff_ids=set(user1_index_dict.keys()) - set(user2_index_dict.keys())
    match_ids=set(user1_index_dict.keys()) & set(user2_index_dict.keys())

    missing = [user1_index_dict[id] for id in diff_ids]

    #find any field changed,use extend to append instead of overwrite
    changed=[]
    changed.extend([user1_index_dict[id] for id in match_ids if asdict(user1_index_dict[id]) != asdict(user2_index_dict[id])])

    return {
        "missing": missing,
        "changed": changed
    }
    
def xxxtest_diff_user(user1, user2):
    diff_result = diff_users(user1, user2)

    missing = diff_result.get("missing")
    missing_ids = [u.id for u in missing]
    assert missing_ids == [126]

    changed = diff_result.get("changed")
    changed_ids = [u.id for u in changed]
    assert changed_ids == [123]
