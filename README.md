# Coin Collector Game

A simple 2D game built with Python and Pygame where players collect coins while avoiding obstacles.

## 🎮 Game Description

In Coin Collector, you control a white square and navigate through the game window to collect yellow coins while avoiding red obstacles. Each coin collected adds to your score, but touching any obstacle ends the game.

### Features
- Simple and intuitive arrow key controls
- Score tracking system
- Dynamic coin respawning
- Obstacle avoidance gameplay
- Game over state

## 🛠️ Prerequisites

Before running the game, make sure you have:
- Python 3.x installed
- pip (Python package installer)

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/nxr-deen/2d-coin-collection-game.git
cd 2d-coin-collection-game
```

2. Create and activate a virtual environment (optional but recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

## 🎯 How to Play

1. Run the game:
```bash
python src/main.py
```

2. Controls:
- ⬆️ Up Arrow: Move up
- ⬇️ Down Arrow: Move down
- ⬅️ Left Arrow: Move left
- ➡️ Right Arrow: Move right

3. Gameplay:
- Collect yellow squares (coins) to increase your score
- Avoid red squares (obstacles)
- Game ends if you hit an obstacle

## 📁 Project Structure
```
2d-coin-collection-game/
├── assets/
│   ├── images/
│   └── sounds/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── game.py
│   └── sprites.py
└── requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by classic arcade games
- Play online: https://replit.com/@NoureddineBoude/2d-coin-collection-game
