"""

This module fills a previously created warehouse with random items.

Built 2017 by Bastian Burger for blik and shared with Solopex.

"""

# Imports
import random as r
import datetime, time, json

from loadcarrier import *
from handlingdevice import *
from warehouse import *

from tkinter import *


# Parameters
filling_level = 0.1 # Be aware that maximum filling level is 33%

scaling_factor = 10.00

DEBUG = True
VERSION = "0.1"


# Global functions
def populate(level):
    """
    The main function that populates the specified warehouse with random boxes of a specific type.
    """
    canvas = []
    actual_level = 0
    actual_area = warehouse_width * warehouse_length
    while actual_level < level:
        new_item = spawn_new_item(MeshBox)
        if not colission(new_item, canvas):
            canvas.append(new_item)
            new_item_area = new_item.area()
            actual_level = (actual_level*actual_area + new_item_area) / actual_area
    return canvas

def spawn_new_item(item_type):
    (x,y,z) = (r.random()*warehouse_width, r.random()*warehouse_length, r.random()*warehouse_height)
    return item_type((x,y,z))

def colission(item, items):
    # could be optimised by moving items to closed location
    for i in items:
        colission_i = 0
        for d in range(0,2):
            proximity = abs(i.coordinates[d] - item.coordinates[d])
            forbidden = abs((i.dimensions[d] + item.dimensions[d]) / 2.0)
            if proximity < forbidden:
                colission_i += 1
        if colission_i == 2:
            return True
    return False

def export(input_list, timestamp):
    """
    The main function to write the results of the simulation in a JSON file.
    """
    filename = "blik_simulation_v" + VERSION + "_" + timestamp + ".json"
    f = open(filename, "w")
    api_like_list = []
    fake_id = 1
    for list_item in input_list:
        dict_item = {"ID": fake_id, "Coordinates":list(list_item.coordinates)}
        api_like_list.append(dict_item)
        fake_id += 1
    json.dump(api_like_list, f)
    f.close()
    return filename

def create_timestamp():
    current_time = time.time()
    timestamp = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d_%H:%M:%S')
    return timestamp


# Test functions
def visualize(box_list):
    # Not very much optimised!!!
    master = Tk()
    visual = Canvas(master, width=warehouse_width*scaling_factor, height=warehouse_length*scaling_factor)
    for box in box_list:
        x0 = (box.coordinates[0] - (box.dimensions[0] / 2.0)) * scaling_factor
        x1 = (box.coordinates[0] + (box.dimensions[0] / 2.0)) * scaling_factor
        y0 = (box.coordinates[1] - (box.dimensions[1] / 2.0)) * scaling_factor
        y1 = (box.coordinates[1] + (box.dimensions[1] / 2.0)) * scaling_factor
        visual.create_rectangle(x0, y0, x1, y1, fill="grey")
    visual.pack(expand=YES)
    mainloop()
    return

def summary(box_list):
    print("––––SUMMARY–––––")
    print("boxes created: " + str(len(item_list)))
    total_area = warehouse_width * warehouse_length
    print("total area: " + str(total_area))
    box_area = 0
    for box in box_list:
        box_area = box_area + box.area()
    print("box area: " + str(box_area))
    x_values = [x.coordinates[0] for x in box_list]
    y_values = [y.coordinates[0] for y in box_list]
    print("x-values range between " + str(min(x_values)) + " & " + str(max(x_values)) + ".")
    print("y-values range between " + str(min(y_values)) + " & " + str(max(y_values)) + ".")
    print("–––––––––––––––––")


# Main Execute
if __name__ == "__main__":
    filling_level = min(filling_level, 1./3.) # maximum number of available spots randomised lower bound

    item_list = populate(filling_level)
    timestamp = create_timestamp()
    export_file = export(item_list, timestamp)
    print("JSON has been written to " + export_file)

    if DEBUG:
        summary(item_list)
        visualize(item_list)
