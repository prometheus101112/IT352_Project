import pandas as pd


def main():
    dataset1 = pd.read_csv('dataset/extra data/sampled_dataset1.csv', low_memory=False)
    dataset2 = pd.read_csv('dataset/extra data/sampled_dataset2.csv', low_memory=False)
    dataset3 = pd.read_csv('dataset/extra data/sampled_dataset3.csv', low_memory=False)
    dataset4 = pd.read_csv('dataset/extra data/sampled_dataset4.csv', low_memory=False)
    dataset5 = pd.read_csv('dataset/extra data/sampled_dataset5.csv', low_memory=False)
    dataset6 = pd.read_csv('dataset/extra data/sampled_dataset6.csv', low_memory=False)
    dataset7 = pd.read_csv('dataset/extra data/sampled_dataset7.csv', low_memory=False)
    dataset8 = pd.read_csv('dataset/extra data/sampled_dataset8.csv', low_memory=False)
    dataset9 = pd.read_csv('dataset/extra data/sampled_dataset9.csv', low_memory=False)

    datasets = [dataset1, dataset2, dataset3, dataset4, dataset5, dataset6, dataset7, dataset8, dataset9]

    d = pd.concat(datasets, ignore_index=True)
    d.to_csv('dataset/sampled_full_dataset.csv')


if __name__ == '__main__':
    main()
