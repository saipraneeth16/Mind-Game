import time
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Maze levels
levels = [
    [
        ['S', '.', '.', '#'],
        ['#', '#', '.', '#'],
        ['.', '.', '.', 'E']
    ],
    [
        ['S', '.', '#', '.', '.'],
        ['#', '.', '#', '#', '.'],
        ['.', '.', '.', '.', '#'],
        ['#', '#', '.', '#', 'E']
    ]
]

# Controls
moves = {
    'W': (-1, 0),
    'A': (0, -1),
    'S': (1, 0),
    'D': (0, 1)
}

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return i, j

def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def play_level(maze, level_num):
    clear()
    print(f"LEVEL {level_num}")
    print("Memorize the maze carefully!")
    print_maze(maze)

    time.sleep(3)  # Memorization time
    clear()

    x, y = find_start(maze)
    print("Maze hidden. Use memory to escape!")

    while True:
        print(f"\nCurrent position: ({x}, {y})")
        move = input("Move (W/A/S/D): ").upper()

        if move not in moves:
            print("Invalid input!")
            continue

        dx, dy = moves[move]
        nx, ny = x + dx, y + dy

        # Bounds check
        if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze[0]):
            print("❌ You hit the boundary! Game Over.")
            sys.exit()

        # Wall check
        if maze[nx][ny] == '#':
            print("💥 You crashed into a wall! Game Over.")
            sys.exit()

        x, y = nx, ny

        # Exit check
        if maze[x][y] == 'E':
            print("🎉 Level Cleared!")
            time.sleep(1)
            return

def main():
    clear()
    print("🧠 MIND MAZE – MEMORY ESCAPE 🧠")
    input("Press Enter to begin...")

    for i, level in enumerate(levels):
        play_level(level, i + 1)

    clear()
    print("🏆 Congratulations! You escaped all mazes!")

if __name__ == "__main__":
    main()

