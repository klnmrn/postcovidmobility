import os

from data_processing.apple import read_apple_data
from data_processing.facebook import read_facebook_data
from data_processing.google import read_google_data
from data_processing.merge import merge_data
from data_visualization.plot import plot_data


def main():
    # Get the folder
    script_dir = os.getcwd()

    # Read and process data
    fb_data = read_facebook_data(script_dir)
    g_data = read_google_data(script_dir)
    a_data = read_apple_data(script_dir)

    # Plot the processed data
    merged_data = merge_data(fb_data, g_data, a_data)
    figure_path = plot_data(merged_data, script_dir)

    # Print statement with folder path
    print(f"Figure plotted and stored in '{os.path.dirname(figure_path)}' folder.")


if __name__ == "__main__":
    main()
