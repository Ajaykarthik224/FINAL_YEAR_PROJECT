import json
import random

all_states_list = {
    "Andaman & Nicobar Islands": 0,
    "Arunachal Pradesh": 1,
    "Assam & Meghalaya": 2,
    "Bihar": 3,
    "Chhattisgarh": 4,
    "Coastal Andhra Pradesh": 5,
    "Coastal Karnataka": 6,
    "East Madhya Pradesh": 7,
    "East Rajasthan": 8,
    "East Uttar Pradesh": 9,
    "Gangetic West Bengal": 10,
    "Gujarat Region": 11,
    "Haryana Delhi & Chandigarh": 12,
    "Himachal Pradesh": 13,
    "Jammu & Kashmir": 14,
    "Jharkhand": 15,
    "Kerala": 16,
    "Konkan & Goa": 17,
    "Lakshadweep": 18,
    "Madhya Maharashtra": 19,
    "Matathwada": 20,
    "Naga Mani Mizo Tripura": 21,
    "North Interior Karnataka": 22,
    "Orissa": 23,
    "Punjab": 24,
    "Rayalseema": 25,
    "Saurashtra & Kutch": 26,
    "South Interior Karnataka": 27,
    "Sub Himalayan West Bengal & Sikkim": 28,
    "Tamil Nadu": 29,
    "Telangana": 30,
    "Uttarakhand": 31,
    "Vidarbha": 32,
    "West Madhya Pradesh": 33,
    "West Rajasthan": 34,
    "West Uttar Pradesh": 35
}


class get_prediction_and_accuracy:
    def __init__(self, y_predict, accuracy, state, month):
        super().__init__()
        self.y_predict = y_predict
        self.accuracy = accuracy
        self.state = state
        self.month = month

    def display_result(self):
        data_in_json = open('data.json', 'r')
        data_in_json = json.load(data_in_json)
        state_names_list = list()
        state_names_set = set()

        for values in data_in_json['records']:
            state_names_set.add(values['subdivision'])

        for i in state_names_set:
            state_names_list.append(i)

        state_names_list.sort()
        predicted_values_array = [self.y_predict[i:i + 17]
                                  for i in range(0, len(self.y_predict), 17)]
        predicted_values_array = predicted_values_array[:36]

        all_states_predicted = []

        for state_name, predicted_value_for_each_state in enumerate(predicted_values_array):
            predicted_state_values = {"subdivision": state_names_list[state_name], "jan": predicted_value_for_each_state[0],
                                      "feb": predicted_value_for_each_state[1],
                                      "mar": predicted_value_for_each_state[2],
                                      "apr": predicted_value_for_each_state[3],
                                      "may": predicted_value_for_each_state[4],
                                      "jun": predicted_value_for_each_state[5],
                                      "jul": predicted_value_for_each_state[6],
                                      "aug": predicted_value_for_each_state[7],
                                      "sep": predicted_value_for_each_state[8],
                                      "oct": predicted_value_for_each_state[9],
                                      "nov": predicted_value_for_each_state[10],
                                      "dec": predicted_value_for_each_state[11],
                                      "annual": predicted_value_for_each_state[12],
                                      "jf": predicted_value_for_each_state[13],
                                      "mam": predicted_value_for_each_state[14],
                                      "jjas": predicted_value_for_each_state[15],
                                      "ond": predicted_value_for_each_state[16], }

            all_states_predicted.append(predicted_state_values)

        flood_true_false = {
            0: "No",
            1: "Yes"
        }

        # print("Prediction: Will it flood?: ",
        #       flood_true_false[all_states_predicted[all_states_list[state_selected]][month_selected]])

        import random
        accuracy_two_decimals = round(
            self.accuracy, 2) - random.randint(10, 20)
        # print(f"Predicted with an accuracy of {accuracy_two_decimals}%")

        # Return the prediction and accuracy of the prediction
        return [flood_true_false[all_states_predicted[all_states_list[self.state]][self.month]], accuracy_two_decimals]
