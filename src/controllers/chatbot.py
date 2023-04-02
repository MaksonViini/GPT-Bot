from fastapi import APIRouter
from starlette.responses import RedirectResponse

from src.resources.utils_chatbot import send_message_to_gpt
from src.schemas.chatbot import Message

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


class Initial:
    @router.get("/")
    async def main():
        """_summary_

        Returns:
            _type_: _description_
        """
        return RedirectResponse(url="/docs/")

    @router.get("/v1/health-checker")
    async def hello_world():
        """_summary_

        Returns:
            Message: _description_
        """
        return {"Ping": "Pong"}, 200


class Chatbot:
    @router.post("/v1/chatbot")
    async def chatbot(message: Message):
        gpt_response = send_message_to_gpt(message.message)

        return {"User": message.message, "Chatbot": gpt_response}
