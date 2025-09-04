import asyncio
import rich
from agents import Agent, Runner, RunContextWrapper, function_tool, trace
from connection import config
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# ================= Example for CartItems =================
# Agar future me tools banane hain to ye class use kar sakte ho
#
# class CartItems(BaseModel):
#     product: list
#     user_id: int
#     brand: str
#     total_amount: int
#
# cart = CartItems(product=["Mobile", "Laptop"], user_id=1, brand="Apple", total_amount=10000)
#
# async def MyPersonalFunction(wrapper: RunContextWrapper[CartItems]):
#     return wrapper
#
# @function_tool
# def products_info(wrapper: RunContextWrapper[CartItems]):
#     print("Checking Context", wrapper.context)
#     return f"{wrapper.context}"
# =========================================================

# Person context for dynamic instructions
class Person(BaseModel):
    name: str
    user_level: str

personOne = Person(
    name="Ali",
    user_level="mid_level"
)


def my_dynamic_instructions(ctx: RunContextWrapper[Person], agent: Agent):
    if ctx.context.user_level in ("junior", "mid_level"):
        return """
        Keep your answer simple and easy to understand.
        """
    elif ctx.context.user_level == "PHD":
        return """
        Keep your vocabulary advanced and very hard like you are talking to a PHD level person.
        """
    return "Be clear and concise."


personal_agent = Agent(
    name="Agent",
    instructions=my_dynamic_instructions,
    tools=[]  
)

async def main():
    with trace("Run Agent with Dynamic Instructions"):
        result = await Runner.run(
            personal_agent,
            "What is  light",
            run_config=config,
            context=personOne
        )

    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())



