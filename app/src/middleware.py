# async def get_request_body(request: Request) -> bytes:
#     body = await request.body()

#     request._receive = ReceiveProxy(receive=request.receive, cached_body=body)
#     return body


# @dataclasses.dataclass
# class ReceiveProxy:
#     """Proxy to starlette.types.Receive.__call__ with caching first receive call."""

#     receive: starlette.types.Receive
#     cached_body: bytes
#     _is_first_call: ClassVar[bool] = True

#     async def __call__(self):
#         # First call will be for getting request body => returns cached result
#         if self._is_first_call:
#             self._is_first_call = False
#             return {"type": "http.request", "body": self.cached_body, "more_body": False}

#         return await self.receive()