# Chess Assist

Chess assist is a website to help improve your chess game. The site will gather game data from LiChess's API for a given username, and recreate positions to practice from. For example: positions from your games just before you made a mistake, positions just after your opponent made a mistake, or positions before you missed a checkmate sequence. As well as a couple of others. Happy practicing.

# To Run This Website Locally

Clone the repository in the desired location on your machine.

cd into the cloned Repository:

```bash
cd ChessAssist
```

Create a virtual environment and activate it:

```bash
python3 -m venv virtenv
source virtenv/bin/activate
```

Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python run.py
```
