from flask import Blueprint, request, jsonify
from schemas.talk_schema import DeveloperInput, TalkOutput
from application.use_cases.generate_daily_talk import GenerateDailyTalkUseCase

bp = Blueprint("talk", __name__)
use_case = GenerateDailyTalkUseCase()

@bp.route("/daily", methods=["POST"])
def daily_talk():
    data = DeveloperInput(**request.json)
    message = use_case.execute(data.name, data.done, data.todo, data.blockers)
    return jsonify(TalkOutput(message=message).dict())
