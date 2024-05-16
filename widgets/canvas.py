import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Create a new window with border
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.border(0)

    # Refresh the screen
    stdscr.refresh()
    win.refresh()

    # Wait for user input
    win.getch()

# Initialize curses
curses.wrapper(main)