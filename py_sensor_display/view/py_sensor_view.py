from math import log10, ceil

from model.py_sensor_model import Model
#from gi.repository import Gtk

class View():
    def __init__(self, model):
        self.model = model
        # win = Gtk.Window()
        # win.connect("delete-event", GTK.main_quit)
        # win.show_all()
        # GTK.main()

    def get_machines(self):
        return self.model.get_machines()

    def get_machine_status(self, id):
        return self.model.get_machine_status(id)

    def get_machine_location(self, id):
        return self.model.get_machine_location(id)

    def get_machine_type(self, id):
        return self.model.get_machine_type(id)

    def format_line(self, args):
        return "| {0:3} | {1:15} |\n".format(args[0], args[1])

    def display_status(self):
        final_list = self.format_line(["ID", "Machine Type"])

        for id in self.get_machines().keys():
            final_list += self.format_line([id, self.get_machine_type(id)])

        return final_list

    def display_locations(self):
        """
        Prints off a grid of the locations of current machines

        :returns: A string with `\n` separated lines with the location of the each machine

        """
        final_list = list()

        # TODO: Add in the third dimension handler eventually.
        current_machines = self.get_machines()

        current_locations = {}
        for m in current_machines.keys():
            current_locations[m] = current_machines[m].get_location()

        x_max = None
        x_min = None

        y_max = None
        y_min = None

        machine_width = 0

        for loc_ind in current_locations:
            loc = current_locations[loc_ind]
            if any(num is None for num in [x_max, x_min, y_max, y_min]):
                x_min, x_max = loc[0], loc[0]
                y_min, y_max = loc[1], loc[1]

            if loc[0] > x_max:
                x_max = loc[0]

            if loc[0] < x_min:
                x_min = loc[0]

            if loc[1] > y_max:
                y_max = loc[1]

            if loc[1] < y_min:
                y_min = loc[1]

            temp_width = ceil(log10(loc_ind))
            if  temp_width > machine_width:
                machine_width = temp_width

        if machine_width % 2 == 0:
            machine_width += 1

        surround_str = " "
        border_str = '-' * (machine_width + 2 * len(surround_str))

        num_side_char = 2
        left_border = border_str[0:num_side_char] + (len(border_str) - num_side_char) * surround_str
        right_border = left_border[::-1]

        y_range = y_max + 2
        x_range = x_max + 2
        for y in range(0, y_range):
            # Initialize the current row
            current_row = []

            # If y is the top or bottom row
            if y in [0, y_range - 1]:
                # Write a string of border_strings
                for temp in range(0, x_range):
                    current_row.append(border_str)
            else:
                for x in range(0, x_range):
                    if x == 0:
                        current_row.append(left_border)
                    elif x == x_max + 1:
                        current_row.append(right_border)
                    else:
                        # We have not yet found a match
                        found = False
                        for loc_ind, loc in current_locations.items():
                            if [x, y] == loc[0:2]:
                                # We found a match
                                found = True

                                # Handle colorful strings
                                c_machine = current_machines[loc_ind]

                                if c_machine.color:
                                    additional = 10
                                else:
                                    additional = 0

                                # Add the machine number in the picture
                                current_row.append("{sur}{mac:^{width}}{sur}".format(sur=surround_str, mac=str(c_machine), width=machine_width + additional))
                                break

                        if not found:
                            current_row.append(surround_str * (machine_width + 2 * len(surround_str)))

            final_list.append(current_row)

        # print([row for row in final_list])
        # final_string = "\n".join(["{0}{1}{0}".format(surround_str, var) for row in final_list for var in row])

        # TODO: One-liner
        place_holder = []
        for row in final_list:
            temp = "".join(var for var in row)
            place_holder.append(temp)

        final_string = "\n".join(row for row in place_holder)

        return final_string
