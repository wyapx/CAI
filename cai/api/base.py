from cai.client import OnlineStatus
from cai.client.session import Session


class BaseAPI:
    session: Session

    async def _executor(
        self, func_name: str, *args, uncaught_error=False, **kwargs
    ):
        if not hasattr(self.session, func_name):
            raise AttributeError(f"client has no attribute '{func_name}'")
        try:
            return await getattr(self.session, func_name)(*args, **kwargs)
        except Exception:
            if uncaught_error:
                await self.session.close()
            raise

    @property
    def device_type(self) -> str:
        return self.session.apk_info.device_type

    @property
    def uin(self) -> int:
        return self.session.uin

    @property
    def nick(self) -> str:
        return self.session.nick

    @property
    def status(self) -> OnlineStatus:
        return self.session.status

    @property
    def connected(self) -> bool:
        return self.session.connected

    async def wait_closed(self):
        return await self.session.wait_closed()
