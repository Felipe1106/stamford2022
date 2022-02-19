# To explore how to visualize and plot data, we wrote the data stream into a csv file and used the loal csv file name
# We used pandas to read the csv and plot data.
if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('xbt.usd.2018.csv', nrows=100)
    df.columns = ['type', 'price', 'quantity', 'time']
    df.sort_values(by=['time'], inplace=True)
    # print(df)
    df.plot(x='time', y='price')
    # df['price'].hist(bins=10)
    # df.plot.bar(x='time', y='price')
    plt.show()

