🧑‍💻 Dynamic Agent Example
Yeh project ek AI Agent framework ka example hai jo user ke context (jaise junior, mid_level, PHD) ke hisaab se apni instructions dynamically change karta hai.

🚀 Features
Dynamic Instructions: User level ke basis par answer simple ya advanced hota hai.
Context Handling: RunContextWrapper ke zariye user ka data agent ko milta hai.
Tracing: trace ka use karke agent ke runs track kiye ja sakte hain.
Environment Config: .env file ke through configs load hote hain.
📦 Requirements
Python 3.9+ recommended.

Install dependencies:

pip install -r requirements.txt
Minimum dependencies:

nginx
Copy code
rich
pydantic
python-dotenv
⚠️ Iske alawa agents aur connection modules ka code aapke project me hona chahiye (jo yaha import kiya gaya hai).

▶️ Usage
.env file banayein aur apna config usme set karein (jo connection/config.py use karta hai).

Program run karein:

bash
Copy code
python main.py
👤 Example Context
python
Copy code
personOne = Person(
    name="Ali",
    user_level="mid_level"
)
junior / mid_level → Simple explanation

PHD → Advanced explanation

🛠️ Extend Example
Ek template diya gaya hai CartItems class ka jo aapke tools ke liye use ho sakta hai:

python
Copy code
class CartItems(BaseModel):
    product: list
    user_id: int
    brand: str
    total_amount: int
Aur function_tool decorator ke saath naye tools define kiye ja sakte hain.

💡 Sample Output
text
Copy code
Q: What is light?

junior / mid_level → "Light is a form of energy that helps us see things."
PHD → "Electromagnetic radiation visible to the human eye, with quantum and wave-particle duality."
📂 Project Structure
arduino
Copy code
.
├── main.py
├── agents/        # custom agent framework
├── connection/    # configs (uses dotenv)
├── requirements.txt
