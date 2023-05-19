from flask import Blueprint
from flask import jsonify

from services import example_services as example_services

example_bp = Blueprint(name='example',
                       import_name=__name__,
                       url_prefix='/example')

openai_bp = Blueprint(name='answer',
                      import_name=__name__,
                      url_prefix='/answer')

search_bp = Blueprint(name='docs_search',
                      import_name=__name__,
                      url_prefix='/docs_search')

query_bp = Blueprint(name='query',
                      import_name=__name__,
                      url_prefix='/query')

@example_bp.route('/', methods=['GET'])
def example_route() -> str:
    data = 'hello_world'
    result = example_services.example_route(data=data)
    return jsonify(result=result)

@example_bp.route('/<int:user_number>', methods=['GET'])
def example_route_add_param(user_number: int) -> str:
    result = example_services.example_route_add_param(user_number)
    return jsonify(result=result)

@openai_bp.route('/', methods=['GET']) # openai 답변 생성 요청 들어갈 곳
def answer_route() -> str:
    data = 'hello_world'
    result = example_services.answer_route(data=data)
    return jsonify(result=result)

@search_bp.route('/', methods=['GET']) # Flask <-> ElasticSearch
def docs_search() -> str:
    data = 'hello_world'
    result = example_services.docs_search(data=data)
    return jsonify(result=result)

@query_bp.route('/', methods=['POST']) # Android <-> Flask
def generate_answer() -> str:
    data = 'hello_world'
    result = example_services.generate_answer(data=data)
    return jsonify(answer=result)