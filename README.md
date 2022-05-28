# track
#### "_A Minimalistic Activity Tracker for Those Who Live in the Terminal_"

![s1](https://github.com/VoltaireNoir/track/blob/main/screenshots/ss1.png)
![s2](https://github.com/VoltaireNoir/track/blob/main/screenshots/ss2.png)

_track_ is designed in such a way as to let you spend more time being productive instead of making you spend time fiddling with the program that helps you track your actvities.
Configure the program using simple self-explainatory commands, and use the fast and ultra-minimal TUI to start tracking your activities using keyboard shortcuts.

## Instructions
- Clone repository (for now)
  - `git clone https://github.com/VoltaireNoir/track.git`
- Make sure "track" is executible
  - `chmod +x track`
- Add at least one activity using the command `track add [name]`, the UI won't launch otherwise
- **Dependency**: [Urwid](https://pypi.org/project/urwid/)
  - `pip install urwid`

## Commands and Shortcuts
> Example: track log activityName
- `track add activity / track a activity`
  - Add new activity to the tracker
- `track del activity / track delete activity`
  - Delete existing activity
- `track list`
  - List all existing activites in the tracker
- `track sel activity / track select activity`
  - Select activity to track using the commandline interface
- `track start` 
  - Start tracking selected activity
- `track status` 
  - Show status information of selected activity (active/inactive/log)
- `track stop` 
  - Stop tracking selected activity
- `track log activity`
  - Show logs for the given activity
- `track logs`
  - Show all logs for all activities
- `track today activity`
  - Show only today's log for given activity
- `track clean activity / track clean all / track clean activity [date/today]`
  - Clear log of given activity or all activities
  - Only specific log will be cleared if 'today' or a date is specified after activity name
    - Date format dd-mm-yyyy
- `track map activity key`
  - Maps activity to the specified keyboard key (options: "1-0" and "!-)")
- `track keymap`
  - Shows current keymap
- `track export`
  - Export logs to a csv file in working directory
- `track flush`
  - Delete all activities including their logs (cannot be recovered)
#### Keyboard Shortcuts
- `q` Quit
- `s` Start/Stop
- `l` Show log for selected activity
- `D` Delete selected activity
- `c` Clear today's log for selected activity
- `C` Clear all logs for selected activity
- `r` Refresh/restart timer if stuck
- `1-0, !-)` Switch between activities (max 20)

## Roadmap / Features to be added
- [ ] Manual log entries
- [x] ~~Delete specific log entry (by date)~~
- [x] ~~Modify order of activites~~
  - Introduced Custom Key-mapping
- [ ] Set everyday goal and display whether or not the goal has been reached
- [x] ~~Track activity from the commandline~~
- [x] ~~Export logs to CSV~~
- [ ] Generate graph based on logs (stats)
