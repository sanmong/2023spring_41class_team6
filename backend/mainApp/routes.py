from .controllers.example_controllers import example_bp, openai_bp

def routes_list(app):
    app.register_blueprint(example_bp)
    app.register_blueprint(openai_bp)
    return app