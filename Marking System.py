from graphics import Line, Point, Text, GraphWin, Rectangle, GraphicsError
import random
import os

progression_data = []
total = 0
option = "y"
progress = 0
trailer = 0
retriever = 0
exclude = 0

# Part 1
# Functioning the main logic.
def Main_log():
    global progress, trailer, retriever, exclude  # Declare global variables.

    while True:
        try:
            while True:
                pass_crd = int(input("Please enter the credit at pass:"))   # Get input for pass credits, ensuring it is within the valid range.
                if pass_crd not in (0, 20, 40, 60, 80, 100, 120):
                    print("Out of range")
                else:
                    break
            while True:
                defer_crd = int(input("Please enter the credit at defer:")) # Get input for Defer credits, ensuring it is within the valid range.
                if defer_crd not in (0, 20, 40, 60, 80, 100, 120):
                    print("Out of range")
                else:
                    break
            while True:
                fail_crd = int(input("Please enter the credit at fail:"))   # Get input for Fail credits, ensuring it is within the valid range.
                if fail_crd not in (0, 20, 40, 60, 80, 100, 120):
                    print("Out of range")
                else:
                    break
                
            # Adding pass credit,Defer credit and fail credit.
            total = pass_crd + defer_crd + fail_crd

            if total != 120:    # Check if the total credits do not add up to 120.
                print("Total incorrect")
            else:
                if pass_crd == 120:     # All credit list with their progresson outcomes.  
                    print('progress')
                    progression_data.append(('progress', pass_crd, defer_crd, fail_crd))
                    progress += 1
                elif pass_crd == 100:
                    print('Progress(module trailer)')
                    progression_data.append(('Progress(module trailer)', pass_crd, defer_crd, fail_crd))
                    trailer += 1
                elif fail_crd >= 80 and fail_crd <= 120:
                    print('Exclude')
                    progression_data.append(('Exclude', pass_crd, defer_crd, fail_crd))
                    exclude += 1
                else:
                    print("Do not progress (module retriever)")
                    progression_data.append(('module retriever', pass_crd, defer_crd, fail_crd))
                    retriever += 1

                result_str = f"{progression_data[-1][0]}-{pass_crd},{defer_crd},{fail_crd}"
                print(result_str)
        
                # Append a tuple containing the detailed data to progression_data.
                progression_data.append((total, pass_crd, defer_crd, fail_crd))

            break  # Exit the loop after processing one set of data.

        except ValueError:
            print("Please enter a valid integer.")   # Handle the possibility of a ValueError if the user enters a non-integer.
        except KeyboardInterrupt:
            print("\nOperation interrupted by the user. Exiting...")    # Exit the loop if the user interrupts the program.
            break  

# Including the Staff mode. 
def staff_mode():
    while True:
        Main_log()

        response = input(
            "Would you like to enter another set of data set? Enter 'y' to continue or 'q' to quit\nPlease enter: "
        ).lower()
        print()

        if response == 'q':
            break    
# Part 2   
# Print output as a list at end of the program.
def show_results():
    draw_histogram(progress, trailer, retriever, exclude)   # Calling the histogram function.

    print("-" * 100)
    print("Part 2:")
    for data in progression_data:
        if isinstance(data[0], str) and data[0] != "120":
            print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")
    print("-" * 100)

# Drawing the histogram.
def draw_histogram(progress, trailer, retriever, exclude):
    
    # Create a graphics window.
    win = GraphWin("Histogram", 360, 320)

    # Name for the window.
    label = Text(Point(80, 25), 'Histogram Results')
    label.draw(win)

    # Setting and calculating bar height.
    def draw_column(x, height, value, color):
        label = Text(Point(x - 15, height - 15), value)
        box = Rectangle(Point(x - 36, 260), Point(x + 36, height))
        box.setFill(color)
        box.draw(win)
        label.draw(win)
        
    # Creating the 1st bar for progress.
    height_1 = 260 - (progress * 10)
    draw_column(60, height_1, progress, "blue")

    # Creating 2nd bar for trailer.
    height_2 = 260 - (trailer * 10)
    draw_column(145, height_2, trailer, "green")

    # Creating 3rd bar for retriever.
    height_3 = 260 - (retriever * 10)
    draw_column(230, height_3, retriever, "gray")  
    
    # Creating 3rd bar for retriever.
    height_4 = 260 - (exclude * 10)
    draw_column(310, height_4, exclude, "red")

    line = Line(Point(24, 261), Point(360, 261))
    line.draw(win)

    # Names for bars.
    label = Text(Point(60, 270), "Progress")
    label.draw(win)
    label = Text(Point(145, 270), "Trailer")
    label.draw(win)
    label = Text(Point(230, 270), "Retriever")
    label.draw(win)
    label = Text(Point(310, 270), "Exclude")
    label.draw(win)
    label = Text(Point(90, 300), f"{progress + trailer + retriever + exclude}  Outcomes in Total")
    label.draw(win)
    try:
        win.getMouse()
    except GraphicsError:
        pass
    win.close()

# Creating a text file with all the outputs.
def create_file(progression_data):
    rand_no = random.randint(0000, 10000)
    file_name = f"Progression_Date_{rand_no}.txt"

    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, file_name)

    with open(file_path, 'w') as file:
        file.write("Part 3:\n")
        for data in progression_data:
            if isinstance(data[0], str):
                file.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")
# Selectiong Modes.
user = input(
    "Enter '1' If you are a student member.\nEnter '2' If you are a staff member.\nPlease Select a mode: ")

if user == "1":
    print("Student version \n")
    Main_log()

elif user == "2":
    print("Staff Version")
    staff_mode()
    show_results()  # Display final results after quitting.

else:
    print("Invalid input")
    
# Calling the text file function.
create_file(progression_data)
