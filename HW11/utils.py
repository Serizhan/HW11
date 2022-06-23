import json


def load_candidates_from_json() -> list[dict]:
    """Перенос данных из данных JSON в список кандидатов"""
    with open('candidates.json', 'r', encoding="utf-8") as file:
        candidates = json.loads(file.read())
    return candidates


def get_candidate(candidate_id: int) -> dict:
    """Возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Возвращает кандидатов по имени"""
    list_of_candidate = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate['name'].lower():
            list_of_candidate.append(candidate)
    return list_of_candidate


def get_candidates_by_skill(skill_name) -> list[dict]:
    """Возвращает кандидатов по навыку"""
    list_of_candidate = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            list_of_candidate.append(candidate)
    return list_of_candidate
