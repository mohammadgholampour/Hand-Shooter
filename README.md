Certainly! Here’s the README file in English:

---

# Hand Shooter

**Hand Shooter** is an action game where you use hand gestures to control a gun and shoot down enemies. The game utilizes hand tracking technology with MediaPipe and OpenCV, and features engaging graphics powered by Pygame.

## Features

- **Gesture-based Shooting:** The gun only shoots when your hand is closed into a fist.
- **Gun Movement with Hand:** The gun moves left and right according to your hand movements.
- **Enemy Generation:** Enemies randomly appear from the top of the screen and move downward.
- **Scoring:** Earn points by shooting down enemies.
- **Game End:** The game ends after 30 seconds, displaying your final score.

## Requirements

- Python 3.x
- Required libraries:
  - OpenCV
  - MediaPipe
  - Pygame

## Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/hand-shooter.git
   cd hand-shooter
   ```

2. **Install Required Libraries:**

   ```bash
   pip install opencv-python mediapipe pygame
   ```

3. **Add Images and Sounds:**

   - `background.png`: Background image for the game
   - `gun.png`: Image of the gun
   - `enemy.png`: Image of the enemies
   - `bullet.png`: Image of the bullets

   Place these images in the project directory.

4. **Run the Game:**

   ```bash
   python game.py
   ```

## How to Play

1. **Shooting Mode:** To shoot, close your hand into a fist.
2. **Gun Movement:** Move your hand left or right to move the gun accordingly.
3. **Targeting:** Aim to shoot down the enemies that appear randomly from the top of the screen.

## Contributing

If you want to contribute to this project, please follow these steps:

1. **Fork the Repository:** Fork the repository.
2. **Create a New Branch:** Create a new branch for your feature or fix.
3. **Submit a Pull Request:** Apply your changes to the new branch and submit a pull request.

## Acknowledgements

This project uses the [OpenCV](https://opencv.org/), [MediaPipe](https://mediapipe.dev/), and [Pygame](https://www.pygame.org/) libraries.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to adjust the information as needed for your project.
