from nicegui import ui

ui.label('NiceGUI Connection Display Test!')

counter = 0

with ui.row():
    ui.label('Counter: ')
    counter_value_label = ui.label(counter)

def increment():
    global counter
    counter += 1
    print(counter)
    counter_value_label.text = counter

ui.timer(1, increment)

ui.run()
