import cwiid

def connect_to_wiimote():
    try:
        print("Press buttons 1 and 2 on your Wiimote simultaneously...")
        wiimote = cwiid.Wiimote()
        wiimote.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_EXT
        print("Connected to Wiimote!")
        return wiimote
    except RuntimeError:
        print("Failed to connect to Wiimote. Please try again.")
        return None

wiimote = connect_to_wiimote()

if wiimote:
    while True:
        try:
            state = wiimote.state
            if 'nunchuk' in state:
                nunchuk_state = state['nunchuk']
                # Read nunchuck data
                stick = nunchuk_state['stick']
                buttons = nunchuk_state['buttons']
                print("Nunchuck Stick:", stick)
                print("Nunchuck Buttons:", buttons)
        except RuntimeError:
            print("Connection to Wiimote interrupted.")
            break
