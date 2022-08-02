from consoleme.default_plugins.plugins.internal_routes.handlers.internal_demo_route import (
    InternalDemoRouteHandler,
)


class InternalRoutes:
    ui_modules = {}

    def get_internal_routes(self, make_jwt_validator, jwt_validator=None):
        return [
            (r"/internal_demo_route/?", InternalDemoRouteHandler),
            # An example of serving static internal content is below, which would make use of the template path variable
            # You defined above.
            # (
            #     r"/static_internal/(.*)",
            #     NoCacheStaticFileHandler,
            #     dict(path=os.path.join(path, "static")),
            # ),
        ]


def init():
    """Initialize the internal routes plugin."""
    return InternalRoutes()
