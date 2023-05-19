from controllers.example_controllers import example_bp, openai_bp, search_bp, query_bp

def routes_list(app):
    app.register_blueprint(example_bp)
    app.register_blueprint(openai_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(query_bp)
    return app