class frontend_gui:

    def state_and_month_selection(self):
        state_selected = input("Enter the state name: ")  # From GUI Form
        month_selected = input("Enter the month: ")  # From GUI Form

        return [state_selected, month_selected]
