import curses
import time
import random

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initial position of the soldier
    soldier_x = 0
    soldier_y = curses.LINES - 2
    bullets = []
    enemies = []

    while True:
        stdscr.clear()

        # Draw the soldier
        stdscr.addch(soldier_y, soldier_x, 'S')

        # Draw the bullets
        for bullet in bullets:
            stdscr.addch(bullet[1], bullet[0], '-')

        # Draw the enemies
        for enemy in enemies:
            stdscr.addch(enemy[1], enemy[0], 'E')

        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Update soldier's position
        if key == curses.KEY_RIGHT and soldier_x < curses.COLS - 1:
            soldier_x += 1
        elif key == curses.KEY_LEFT and soldier_x > 0:
            soldier_x -= 1
        elif key == ord(' '):
            bullets.append([soldier_x + 1, soldier_y])

        # Update bullets' positions
        new_bullets = []
        for bullet in bullets:
            bullet[0] += 1
            if bullet[0] < curses.COLS:
                new_bullets.append(bullet)
        bullets = new_bullets

        # Update enemies' positions
        new_enemies = []
        for enemy in enemies:
            enemy[0] -= 1
            if enemy[0] >= 0:
                new_enemies.append(enemy)
        enemies = new_enemies

        # Add new enemies at random positions
        if random.randint(0, 20) == 0:
            enemies.append([curses.COLS - 1, random.randint(0, curses.LINES - 1)])

        # Check for collisions between bullets and enemies
        new_bullets = []
        for bullet in bullets:
            hit = False
            for enemy in enemies:
                if bullet[0] == enemy[0] and bullet[1] == enemy[1]:
                    enemies.remove(enemy)
                    hit = True
                    break
            if not hit:
                new_bullets.append(bullet)
        bullets = new_bullets

        # Sleep for a short duration to control the game speed
        time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
