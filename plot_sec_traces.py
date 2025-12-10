import pandas as pd
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description="Plot SEC UV traces from a CSV file.")
    parser.add_argument("csv_file", help="Path to CSV file")
    parser.add_argument("--xmin", type=float, default=None, help="Minimum X-axis value (mL)")
    parser.add_argument("--xmax", type=float, default=None, help="Maximum X-axis value (mL)")
    parser.add_argument("--ymin", type=float, default=None, help="Minimum Y-axis value (mAU)")
    parser.add_argument("--ymax", type=float, default=None, help="Maximum Y-axis value (mAU)")
    parser.add_argument("--save", action="store_true", help="Save plot as sec_traces.png")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_file)

    x = df.iloc[:, 0]
    y_traces = df.iloc[:, 1:]

    plt.figure(figsize=(10, 6))

    for col in y_traces.columns:
        plt.plot(x, y_traces[col], label=col)

    plt.xlabel("Volume (mL)")
    plt.ylabel("Absorbance (mAU)")
    plt.title("SEC UV Traces")
    plt.legend()
    plt.grid(True)

    # Apply axis limits if provided
    if args.xmin is not None or args.xmax is not None:
        plt.xlim(args.xmin, args.xmax)

    if args.ymin is not None or args.ymax is not None:
        plt.ylim(args.ymin, args.ymax)

    plt.tight_layout()

    if args.save:
        plt.savefig("sec_traces.png", dpi=300)

    plt.show()


if __name__ == "__main__":
    main()


