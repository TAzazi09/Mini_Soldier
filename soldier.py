Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import curses
... import time
... 
... def main(stdscr):
...     # Clear screen
...     stdscr.clear()
...     curses.curs_set(0)
... 
...     # Initial position of Mario
...     mario_x = 0
...     mario_y = curses.LINES - 2
... 
...     while True:
...         stdscr.clear()
... 
...         # Draw Mario
...         stdscr.addch(mario_y, mario_x, 'M')
... 
...         stdscr.refresh()
... 
...         # Get user input
...         key = stdscr.getch()
... 
...         # Update Mario's position
...         if key == curses.KEY_RIGHT:
...             mario_x += 1
...         elif key == curses.KEY_LEFT:
...             mario_x -= 1
... 
...         # Sleep for a short duration to control the game speed
...         time.sleep(0.1)
... 
... if __name__ == '__main__':
...     curses.wrapper(main)
