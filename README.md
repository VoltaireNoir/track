# track
#### "_A Minimalistic Activity Tracker for Those Who Live in the Terminal_"

![s1](https://github.com/VoltaireNoir/track/blob/main/screenshots/ss1.png)
![s2](https://github.com/VoltaireNoir/track/blob/main/screenshots/ss2.png)

## Instructions
- **Dependency**: [Urwid](https://pypi.org/project/urwid/)
  - `pip install urwid`
- Make sure "track" is executible
  - `chmod +x track`
- Add at least one activity using the command `track add [name]`, the TUI won't launch otherwise

## Commands and Shortcuts
> Example: track log activityName
- `track add activity / track a activity`
  - Add new activity to the tracker
- `track del activity / track delete activity`
  - Delete existing activity
- `track list`
  - List all existing activites in the tracker
- `track sel activity / track select activity`
  - Select default activity (puts given activity in the first position when running the program)
- `track log activityName`
  - Show logs for the given activity
- `track logs`
  - Show all logs for all activities
- `track today activity`
  - Show today's log for given activity
- `track clean activity / track clean all`
  - Clear log for given activity or all of them
- `track flush`
  - Delete all activities
#### Keyboard Shortcuts
- `q` Quit
- `s` Start/Stop
- `l` Show log for selected activity
- `D` Delete selected activity
- `c` Clear today's log for selected activity
- `C` Clear all logs for all activities
- `1-0, !-)` Switch between activities (max 20)

## Roadmap / Features to be added
- [ ] Manual log entries
- [ ] Delete specific log entry (by date)
- [ ] Modify order of activites
- [ ] Set everyday goal and display whether or not the goal has been reached
- [ ] Track activity from the commandline
- [ ] Export logs to CSV
- [ ] Generate graph based on logs (stats)
