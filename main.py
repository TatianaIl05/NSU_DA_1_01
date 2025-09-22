from sklearn.datasets import load_iris
from io import StringIO
import pandas as pd
import sys

def load_dataset():
    """
    Function reads the dataset 
    Returns:
        A loaded data frame
    """
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    return df


def dataset_analytics(data_frame):
    """
    Function prints the main analytics of a data frame
    Parameters: 
        data_frame - the data frame for which the analitics are displayed
    Returns:
        dictionary of main analytics of a data frame
    """
    buffer = StringIO()
    data_frame.info(buf=buffer, memory_usage=False)
    info_output = buffer.getvalue()

    analytics = {
        "head": data_frame.head(5),
        "info": info_output,
        "describe": data_frame.describe(),
        "shape": data_frame.shape
    }

    return analytics
       
def save_to_file(analytics, filename):
    """
    Function saves the analytics to a specified file
    Parameters:
        analytics - the analytics data to save
        filename - the name of the file to save the analytics
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write("Основная информация о датафрейме:\n")

        f.write("Первые пять элементов датафрейма:\n")
        f.write(str(analytics["head"]) + "\n")

        f.write("Информация о типах и пропусках:\n")
        f.write(str(analytics["info"]) + "\n")

        f.write("Статистические данные:\n")
        f.write(str(analytics["describe"]) + "\n")

        f.write("Размер датафрейма:\n")
        f.write(f'Количество строк - {analytics["shape"][0]}\nКоличество столбцов - {analytics["shape"][1]}\n')

def main(dataset_name, output_file):
    """
    Main function of the project
    Parameters:
        dataset_name - name of the used dataset
        output_file - file where the analytics are saved
    """
    if dataset_name == "iris": data_set = load_dataset()
    else: raise ValueError("Неизвестный датасет")

    analytics = dataset_analytics(data_set)
    save_to_file(analytics, output_file)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise ValueError("Введите данные в виде: python main.py <имя_датасета> <имя_файла>")
        
        dataset_name = sys.argv[1]
        output_file = sys.argv[2]

        main(dataset_name, output_file)
        sys.exit(0)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)
